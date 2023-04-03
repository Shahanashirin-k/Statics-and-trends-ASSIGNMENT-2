# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 04:26:56 2023

@author: SHAHANA SHIRIN
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats


def read_data(fn):
   """
  Reads a CSV file and returns a pandas DataFrame.
  
  Parameters:
  fn (str): The filename of the CSV file to be read.
  
  Returns:
  df (pandas.DataFrame): The DataFrame containing the data read from the CSV file.
  """

   address = "C:/Users/SHAHANA SHIRIN/Desktop/ADS/assignment 2/" + fn
   df = pd.read_csv(address)
   df = df.drop(df.columns[:2], axis=1)
   df_transpose = df.transpose()
   return df


def bargraph_1():
   """
    Reads methane emission data from 'agri_metth_kmt' CSV file and creates a bar graph of the data. 
    Calculates the mean, median, and mode of the data and prints the results.
   """

   # Read data from csv file and select columns of interest
   df_meth = read_data('agri_metth_kmt.csv')
   CH4 = df_meth[['Country Name', '1990 [YR1990]', '1994 [YR1994]', '1998 [YR1998]', '2002 [YR2002]', '2006 [YR2006]', '2010 [YR2010]', '2014 [YR2014]', '2018 [YR2018]']]
   CH4 = CH4.dropna()

   # Define countries, country codes, years, and colors for the bar graph
   countries = ['India', 'China', 'Bangladesh', 'Pakistan', 'Nigeria', 'Indonesia','United Kingdom', 'Brazil', 'United States', 'Mexico', 'Russia', 'Japan']
   country_code = ['BGD', 'BRA', 'CHN', 'IND', 'IDN', 'JPN', 'MEX', 'NGA', 'PAK', 'GBR', 'USA']
   years = [1990, 1994, 1998, 2002, 2006, 2010, 2014,2018]
   C = ['grey', 'orange', 'red', 'green', 'steelblue', 'yellow', 'violet']

   # Select data for the specified countries and convert to numeric values
   CH4_df = CH4[CH4['Country Name'].isin(countries)].copy()
   CH4_df = CH4_df.set_index('Country Name')
   CH4_df = CH4_df.apply(pd.to_numeric, errors='coerce')

   # Create the bar graph
   CH4_df.plot(kind='bar', figsize=(10, 7), width=0.5,color=C, edgecolor='black', fontsize=11)
   plt.legend(title='Years', labels=years,bbox_to_anchor=(1.01, 1), fontsize=11)
   plt.xticks(range(len(CH4_df.index)), country_code)
   plt.xlabel('countries',fontsize=12)
   plt.ylabel('Agricultural Methane Emission',fontsize=11)
   plt.title("Agricultural Methane emissions in KMT of CO2 eq")
   plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

   # Save the plot to a file and print the mean,median and mode
   plt.savefig('myplot.png', dpi=300, bbox_inches='tight')
   _mean = CH4_df.mean()
   _median = CH4_df.median()
   _mode = stats.mode(CH4_df, keepdims=False)
   print("Mean of methane emission:\n", _mean)
   print("Median of methane emission:\n", _median)
   print("Mode of methane emission:\n", _mode.mode[0])

   # Display the plot
   plt.show()
   

def bargraph_2():
    """
     Reads methane emission data from 'agri_metth_kmt' CSV file and creates a bar graph of the data. 
     Calculates the mean, median, and mode of the data and prints the results.
    """

    # Read data from csv file and select columns of interest
    df_meth = read_data('metane_kt.csv')
    CH4_df_meth = df_meth[['Country Name', '1990 [YR1990]', '1994 [YR1994]', '1998 [YR1998]', '2002 [YR2002]', '2006 [YR2006]', '2010 [YR2010]', '2014 [YR2014]', '2018 [YR2018]']]
    CH4_df_meth = CH4_df_meth.dropna()

    # Define countries, country codes, years, and colors for the bar graph
    countries = ['India', 'China', 'Bangladesh', 'Pakistan', 'Nigeria', 'Indonesia','United Kingdom', 'Brazil', 'United States', 'Mexico', 'Russia', 'Japan']
    country_code = ['BGD', 'BRA', 'CHN', 'IND', 'IDN', 'JPN', 'MEX', 'NGA', 'PAK', 'GBR', 'USA']
    years = [1990, 1994, 1998, 2002, 2006, 2010, 2014,2018]
    C = ['grey', 'orange', 'red', 'green', 'steelblue', 'yellow', 'violet']

    # Select data for the specified countries and convert to numeric values
    meth_df = CH4_df_meth[CH4_df_meth['Country Name'].isin(countries)].copy()
    meth_df =  meth_df.set_index('Country Name')
    meth_df =  meth_df.apply(pd.to_numeric, errors='coerce')

    # Create the bar graph
    meth_df.plot(kind='bar', figsize=(10, 7), width=0.5,color=C, edgecolor='black', fontsize=11)
    plt.legend(title='Years', labels=years,bbox_to_anchor=(1.01, 1), fontsize=11)
    plt.xticks(range(len(meth_df.index)), country_code)
    plt.xlabel('countries')
    plt.ylabel('Methane Emission',fontsize=12)
    plt.title("Total Methane emissions in KT of CO2 eq")
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    # Save the plot to a file and print the mean,median and mode
    plt.savefig('barplot.png', dpi=300, bbox_inches='tight')
    _mean = meth_df.mean()
    _median = meth_df.median()
    _mode = stats.mode(meth_df, keepdims=False)
    print("Mean of methane emission:\n", _mean)
    print("Median of methane emission:\n", _median)
    print("Mode of methane emission:\n", _mode.mode[0])

    # Display the plot
    plt.show()


    
if __name__ == '__main__':
    """
    Main function that calls the other functions to create the plots.
    """
    # Calling the bargraph_1&2 function to visualise the barplot
    bargraph_1()
    bargraph_2()










