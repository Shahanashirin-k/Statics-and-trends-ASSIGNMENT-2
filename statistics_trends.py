# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 04:26:56 2023

@author: SHAHANA SHIRIN
"""
import matplotlib.pyplot as plt
import pandas as pd
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
    CH4 = df_meth[['Country Name', '1990 [YR1990]', '1994 [YR1994]', '1998 [YR1998]',
                   '2002 [YR2002]', '2006 [YR2006]', '2010 [YR2010]', '2014 [YR2014]', '2018 [YR2018]']]
    CH4 = CH4.dropna()

    # Define countries, country codes, years, and colors for the bar graph
    countries = ['India', 'China', 'Bangladesh', 'Pakistan', 'Nigeria', 'Indonesia',
                 'United Kingdom', 'Brazil', 'United States', 'Mexico', 'Russia', 'Japan']
    country_code = ['BGD', 'BRA', 'CHN', 'IND', 'IDN',
                    'JPN', 'MEX', 'NGA', 'PAK', 'GBR', 'USA']
    years = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
    C = ['grey', 'orange', 'red', 'green',
         'steelblue', 'yellow', 'violet', 'khaki']

    # Select data for the specified countries and convert to numeric values
    CH4_df = CH4[CH4['Country Name'].isin(countries)].copy()
    CH4_df = CH4_df.set_index('Country Name')
    CH4_df = CH4_df.apply(pd.to_numeric, errors='coerce')

    # Create the bar graph
    CH4_df.plot(kind='bar', figsize=(10, 7), width=0.7,
                color=C, edgecolor='black', fontsize=11)
    plt.legend(title='Years', labels=years,
               bbox_to_anchor=(1.01, 1), fontsize=11)
    plt.xticks(range(len(CH4_df.index)), country_code)
    plt.xlabel('countries', fontsize=12)
    plt.ylabel('Agricultural Methane Emission', fontsize=11)
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
      Reads methane emission data from 'energy_meth' CSV file and creates a bar graph of the data. 
      Calculates the mean, median, and mode of the data and prints the results.
     """

    # Read data from csv file and select columns of interest
    df_meth_ener = read_data('enrgy meth.csv')
    CH4_ener = df_meth_ener[['Country Name', '1990 [YR1990]', '1994 [YR1994]', '1998 [YR1998]',
                             '2002 [YR2002]', '2006 [YR2006]', '2010 [YR2010]', '2014 [YR2014]', '2018 [YR2018]']]
    CH4_ener = CH4_ener.dropna()

    # Define countries, country codes, years, and colors for the bar graph
    countries = ['India', 'China', 'Bangladesh', 'Pakistan', 'Nigeria', 'Indonesia',
                 'United Kingdom', 'Brazil', 'United States', 'Mexico', 'Russia', 'Japan']
    country_code = ['BGD', 'BRA', 'CHN', 'IND', 'IDN',
                    'JPN', 'MEX', 'NGA', 'PAK', 'GBR', 'USA']
    years = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
    C = ['yellow', 'red', 'orange', 'deeppink',
         'red', 'violet', 'coral', 'green']

    # Select data for the specified countries and convert to numeric values
    CH4_df_ener = CH4_ener[CH4_ener['Country Name'].isin(countries)].copy()
    CH4_df_ener = CH4_df_ener.set_index('Country Name')
    CH4_df_ener = CH4_df_ener.apply(pd.to_numeric, errors='coerce')

    # Create the bar graph
    CH4_df_ener.plot(kind='bar', figsize=(10, 7), width=0.8,
                     color=C, edgecolor='black', fontsize=11)
    plt.legend(title='Years', labels=years,
               bbox_to_anchor=(1.01, 1), fontsize=11)
    plt.xticks(range(len(CH4_df_ener.index)), country_code)
    plt.xlabel('countries', fontsize=12)
    plt.ylabel('Energy Methane Emission', fontsize=12)
    plt.title("Energy Methane emissions in KMT of CO2 eq")
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    # Save the plot to a file and print the mean,median and mode
    plt.savefig('energy meth.png', dpi=300, bbox_inches='tight')

    # Display the plot
    plt.show()


def bargraph_3():
    """
     Reads methane emission data from 'metane_kt' CSV file and creates a bar graph of the data. 
     Calculates the mean, median, and mode of the data and prints the results.
    """

    # Read data from csv file and select columns of interest
    df_meth = read_data('metane_kt.csv')
    CH4_df_meth = df_meth[['Country Name', '1990 [YR1990]', '1994 [YR1994]', '1998 [YR1998]',
                           '2002 [YR2002]', '2006 [YR2006]', '2010 [YR2010]', '2014 [YR2014]', '2018 [YR2018]']]
    CH4_df_meth = CH4_df_meth.dropna()
    # Define countries, country codes, years, and colors for the bar graph
    countries = ['India', 'China', 'Bangladesh', 'Pakistan', 'Nigeria', 'Indonesia',
                 'United Kingdom', 'Brazil', 'United States', 'Mexico', 'Russia', 'Japan']
    country_code = ['BGD', 'BRA', 'CHN', 'IND', 'IDN',
                    'JPN', 'MEX', 'NGA', 'PAK', 'GBR', 'USA']
    years = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
    C = ['khaki', 'orange', 'red', 'greenyellow',
         'green', 'steelblue', 'violet', 'coral']

    # Select data for the specified countries and convert to numeric values
    meth_df = CH4_df_meth[CH4_df_meth['Country Name'].isin(countries)].copy()
    meth_df = meth_df.set_index('Country Name')
    meth_df = meth_df.apply(pd.to_numeric, errors='coerce')

    # Create the bar graph
    meth_df.plot(kind='bar', figsize=(10, 7), width=0.7,
                 color=C, edgecolor='black', fontsize=11)
    plt.legend(title='Years', labels=years,
               bbox_to_anchor=(1.01, 1), fontsize=11)
    plt.xticks(range(len(meth_df.index)), country_code)
    plt.xlabel('countries', fontsize=12)
    plt.ylabel('Methane Emission', fontsize=12)
    plt.title("Total Methane emissions in KT of CO2 eq")
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    # Save the plot to a file and print the mean,median and mode
    plt.savefig('barplot.png', dpi=600, bbox_inches='tight')
    _mean = meth_df.mean()
    _median = meth_df.median()
    _mode = stats.mode(meth_df, keepdims=False)
    print("Mean of methane emission:\n", _mean)
    print("Median of methane emission:\n", _median)
    print("Mode of methane emission:\n", _mode.mode[0])

    # Display the plot
    plt.show()

    # Use describe method to generate descriptive statistics
    meth_df_describe = meth_df.describe()
    print(meth_df_describe)

    # Use group by method to generate group by mean of the year 2014 and 2018
    meth_df = CH4_df_meth[CH4_df_meth['Country Name'].isin(
        countries)][['Country Name', '2014 [YR2014]', '2018 [YR2018]']].copy()
    meth_df_grouped = meth_df.groupby(['Country Name']).mean().reset_index()
    print(meth_df_grouped)
    

def lineplot_1():
    """
    Reads the 'energy use.csv' file and creates a line plot of energy use for selected countries
    from 1990 to 2014.
    """
    # Read the data
    df_ener = read_data("energy use.csv")

    # Drop columns for years 2015 to 2021
    df_ener.drop(
        ['Country Code', '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]',
            '2018 [YR2018]', '2019 [YR2019]', '2020 [YR2020]', '2021 [YR2021]'],
        axis=1,
        inplace=True
    )

    # Remove the string of year from column names
    df_ener.columns = df_ener.columns.str.replace(' \[YR\d{4}\]', '', regex=True)

    # Select the countries for the plot
    countries = ['India', 'China', 'Bangladesh', 'Pakistan', 'Nigeria',
                 'Indonesia', 'United Kingdom', 'Brazil', 'United States', 'Mexico', 'Japan']

    # Create a DataFrame with data for selected countries
    energy_df = df_ener[df_ener['Country Name'].isin(countries)]

    # Set the index to 'Country Name' and transpose the DataFrame
    energy_df = energy_df.set_index('Country Name').T

    # Replace missing values with NaN and convert values to float
    energy_df = energy_df.replace('..', float('NaN')).astype(float)

    # Drop rows with missing values
    energy_df = energy_df.dropna()

    # Create the line plot
    energy_df.plot(figsize=(10, 6))
    plt.xlabel("Year", fontsize=13)
    plt.ylabel("Energy Use", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title("Energy Use (kg of oil equivalent per capita)\n", fontsize=14)
    plt.legend(title='Countries', bbox_to_anchor=(
        1.01, 1), fontsize=12, title_fontsize=12)

    # Save the plot as a png file and display it
    plt.savefig('Energy use.png', dpi=600, bbox_inches='tight')
    plt.show()
    

def lineplot_2():
    """
    Reads in a CSV file of electric power consumption data and creates a line plot of the data for selected countries.
    Saves the plot as a PNG file and displays it in the console.
    """
    # Read in the CSV file and drop unnecessary columns
    df_elec = read_data("electric pwr.csv")
    df_elec.drop(['Country Code', '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]',
                 '2018 [YR2018]', '2019 [YR2019]', '2020 [YR2020]', '2021 [YR2021]'], axis=1, inplace=True)

    # Remove year strings from column names
    df_elec.columns = df_elec.columns.str.replace(
        ' \[YR\d{4}\]', '', regex=True)  # Remove string of year from column names

    # Select countries of interest and transpose the data
    countries = ['India', 'China', 'Bangladesh', 'Pakistan', 'Nigeria',
                 'Indonesia', 'United Kingdom', 'Brazil', 'United States', 'Mexico', 'Japan']
    elect_df = df_elec[df_elec['Country Name'].isin(countries)]
    elect_df = elect_df.set_index('Country Name').T

    # Convert 'no data' strings to NaN and convert data to floats
    elect_df = elect_df.replace('..', float('NaN')).astype(float)

    # Create a line plot of the data
    elect_df.plot(figsize=(10, 6))

    # Set plot labels and title
    plt.xlabel("Year", fontsize=13)
    plt.ylabel("Electric power consumption", fontsize=13)
    plt.title("Electric power consumption (kWh per capita)", fontsize=14)

    # Set font sizes for tick labels and legend
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(title='Countries', bbox_to_anchor=(
        1.01, 1), fontsize=12, title_fontsize=12)
    
    # Save the plot as a PNG file and display in the console
    plt.savefig('Electric.png', dpi=600, bbox_inches='tight')
    plt.show()

    
# main function for visualization:
if __name__ == '__main__':
    """
    Main function that calls the other functions to create the plots.
    """
    # Calling the bargraph_1&2 function to visualise the barplot
    bargraph_1()
    bargraph_2()
    bargraph_3() 
    
    # Calling the bargraph_1&2 function to visualise the lineplot      
    lineplot_1()
    lineplot_2()