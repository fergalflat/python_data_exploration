# -*- coding: utf-8 -*-
"""
Student ID: A00291231
Purpose: Create dictionary of dates and values. Perform calcuations on these dates and values
"""
import re
import datetime
import matplotlib.pyplot as plt

dates_data = {}
dates_data2 = {}

try: 
    with open("nba2k20_players.csv") as data_file:
        _ = data_file.readline()
        contents = data_file.read()
            
        file_list = re.findall("(\d{2}/\d{2}/\d{4},\d{3})", contents, re.M) #regex to find all the dates and heights 
        
        for line in file_list: #For each of the dates
            try:
                line, height =line.split(",")
                time = datetime.datetime.strptime(line, "%m/%d/%Y") #Convert the string date to a date object
                date_object = time.date() #Remove the time from the date time object
                new_format = date_object.strftime('%B') #Get the dates in month format
                
                if date_object not in dates_data:
                    # insert into dictionary. If a date has more than one value per date, sum the values
                    dates_data[date_object] = int(height)
                else:
                    dates_data[date_object] += int(height)
                    
                if new_format not in dates_data2:
                    # insert into dictionary. If a month has more than one value per date, sum the values
                    dates_data2[new_format] = int(height)
                else:
                    dates_data2[new_format] += int(height)
            except ValueError:
                print("Your input is not in correct format")
    
    def earliest_date(dates_data):
        '''     
        Get the earliest date in the dictionary

        Parameters
        ----------
        dates_data : dictionary{int}
            dictionary of dates along with their associated values.

        Returns
        -------
        early_date : datetime
            the earliest date in the dictionary.

        '''
        try:
            early_date = min(dates_data)
            return early_date
        except ValueError:
            print("Incorrect value type")
             
    def latest_date(dates_data):
        '''       
        Get the latest date in the dictionary

        Parameters
        ----------
        dates_data : dictionary{int}
            dictionary of dates along with their associated values.

        Returns
        -------
        late_date : datetime
            the latest date in the dictionary.

        '''
        try:
            late_date = max(dates_data)
            return late_date
        except ValueError:
            print("Incorrect value type")
    
    def delta_fn(dates_data):
        '''      
        Get the difference, in days, between the earliest and latest dates

        Parameters
        ----------
        dates_data : dictionary{int}
            dictionary of dates along with their associated values.

        Returns
        -------
        delta.days: int
            the difference in days between the earliest and latest days.

        '''
        try:
            #The number of days between the earliest and latest dates
            delta = max(dates_data) - min(dates_data)
            return delta
        except ValueError:
            print("Incorrect value type")
    
    def date_high_value(dates_data):
        '''       
        Get the date with the highest value associated with it

        Parameters
        ----------
        dates_data : dictionary{int}
            dictionary of dates along with their associated values.

        Returns
        -------
        high_value : datetime
            date with the highest value associated with it

        '''
        try:
        #The date with the highest value
            high_value = max(dates_data, key=dates_data.get)
            return high_value
        except ValueError:
            print("Incorrect value type")
   
    def date_low_value(dates_data):
        '''       
        Get the date with the lowest value associated with it

        Parameters
        ----------
        dates_data : dictionary{int}
            dictionary of dates along with their associated values.

        Returns
        -------
        low_value : datetime
            date with the lowest value associated with it.

        '''
        try:
            #The date with the lowest value
            low_value = min(dates_data, key=dates_data.get)
            return low_value
        except ValueError:
            print("Incorrect value type")
    
    def average_value(dates_data):
        '''        
        Get the average value per date

        Parameters
        ----------
        dates_data : dictionary{int}
            dictionary of dates along with their associated values.

        Returns
        -------
        average : float
            average value associated with each date.

        '''
        try:
            #The average value per date
            #First get the sum of all the values
            values_total = sum(dates_data.values())
            #Number of dates
            num_dates = len(dates_data)
            #Divide the total of values by the number of dates to get the average value per date
            average = values_total/num_dates
            return average
        except ValueError:
            print("Incorrect value type")
    
    def date_plot(dates_data): 
        '''       
        date plot of all heights in the dictionary

        Parameters
        ----------
        dates_data : dictionary{int}
            dictionary of dates along with their associated values.

        Returns
        -------
        None.

        '''
        try:
            #A date plot, showing the values on each date
            fig, ax = plt.subplots()
            ax.set_xlabel("Date")
            ax.set_ylabel("Height(cm)")
            ax.set_title("Values on each Date")
            ax.plot_date(dates_data.keys(), dates_data.values(), marker = ".", linestyle="-")
            plt.show()
        except ValueError:
            print("Incorrect value type")
        
    def bar_chart(dates_data2):
        '''       
        bar chart of all months and their cumulative height

        Parameters
        ----------
        dates_data2 : dictionary{int}
            dictionary of months along with their cumulative heights.

        Returns
        -------
        None.

        '''
        try:
        #A bar chart, showing the total values by month
            fig, ax = plt.subplots()
            ax.set_xlabel("Month")
            ax.set_ylabel("Height(cm)")
            ax.set_title("Total values by month")
            plt.xticks( ha='right', rotation=55, fontsize=10, fontname='monospace')
            plt.bar(dates_data2.keys(), dates_data2.values())
            plt.show()
        except ValueError:
            print("Incorrect value type")


except (FileNotFoundError, PermissionError):
    print("Unable to open the file: nba2k20_players.csv")

if __name__ == "__main__":
    print("Earliest Date:", earliest_date(dates_data))
    print("Latest Date:", latest_date(dates_data))
    print("The number of days between the earliest and latest dates:", delta_fn(dates_data))
    print("The date with the highest value:", date_high_value(dates_data))
    print("The date with the lowest value:", date_low_value(dates_data))
    print(f"The average value per date: {average_value(dates_data):.1f}")
    date_plot(dates_data)
    bar_chart(dates_data2)