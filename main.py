#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse SEA region over a span of 10 years from 2007 to 2017 (10Years)
#Name: <Nasifa Fathima>
#Group Name: <NS>
#Class: <PN2004Y>
#Date: <16/07/2021>
#Version: <V1>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd

#import matplotlib
import matplotlib.pyplot as plot

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):
    #load excel data (CSV format) to dataframe - 'df'
    df = pd.read_csv('MonthyVisitors.csv')
    
    #print number of rows in dataframe
    print("There are " + str(len(df)) + " data rows read. \n")

    #print total number of countries in dataframe by counting the number of columns 
    print("Total number of countries:", str(len    (df.columns) - 2))

    #display dataframe (rows and columns)
    print("The following dataframe are read as follows: \n")
    
    
    # initializing dataframe for SEA region
    sea_region = df.iloc[348:, 0:9]

    #Display all the SEA regions from 2007 to 2017 on the console
    print(sea_region)

    #Remove the columns Year and Month on the sea_region variable
    NewSEA = sea_region.drop(columns=['Year', 'Month'])

    #Converts all values from sea_region from object to integer for calculation
    NewSEA[NewSEA.columns] = NewSEA[NewSEA.columns].astype(int)
    
    #Calculate the total visitors of each countries by summing up the values
    TotalSEA = NewSEA.sum()

    #sort the region to descending order
    sea_region = TotalSEA.sort_values(ascending=False)

    #revert the index
    sea_region = sea_region.reset_index()

    #Add the columns Countries and Visitors to display on the console
    sea_region.columns = ['Countries', 'Visitors']

    #Display the top 3 countries in the SEA region with highest visitors
    print(sea_region.head(3))

    #Call the display chart function
    displayChart(sea_region)
      
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################

def displayChart(df):
  #Initialise the 2 list Countries and Visitors
  Countries = df['Countries']
  Visitors = df['Visitors']

  figure1,chart = plot.subplots()

  #Visualise the list with a pie chart with the proper properties
  chart.pie(Visitors,
          labels=Countries,
          startangle=100,
          shadow=True,
          explode = (0, 0, 0, 0, 0.3, 0.2, 0.1),
          autopct='%1.2f%%')

  chart.axis('equal')
  #Show legend on the pie chart
  plot.legend()

  #display the pie chart
  plot.show()
  return



#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################
