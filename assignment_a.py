# -*- coding: utf-8 -*-
"""
Student ID: A00291231
Purpose: Perform calcualations on single variable that has its values in a list
"""
from math import sqrt
import matplotlib.pyplot as plt

height_list = []
weight_list = []

try:       
    #Open the data set and initialise it to "csv_file"
    with open ("nba2k20_players.csv") as data_file:
        headers = data_file.readline()
    #for each line in the csv, split each variable by a comma. The add the value from the height row(row 6) to the list.
        for line in data_file:
            try:
                fullName, rating, jersey, team, bDay, height, weight, salary, country = line.split(",")
                                  
                height_list.append(int(height))
                weight_list.append(int(weight))
            except ValueError:
                print("Your input is not in correct format")

    #Number if instances of heights/number of rows
    def number_of_values(height_list):
        '''        
        Get the number of values from the height list     

        Parameters
        ----------
        height_list : list[int]
            list of heights.

        Returns
        -------
        int
            the number of values in the list.
        '''
        try:
            number = len(height_list)
            return number  
        except ValueError:
            print("Incorrect value type")
    
    #The height of everyone in the list added together
    def total_height(height_list):
        '''
        Get the total height of everyone in the list of heights
        
        Parameters
        ----------
        height_list : list[int]
            List of heights.

        Returns
        -------
        int
            the sum of all the heights in the list.

        '''
        try:
            total = sum(height_list)
            return total
        except ValueError:
                print("Incorrect value type")
    #Mean
    def calc_mean(height_list):
        '''        
        Get the mean of the values from the list of heights

        Parameters
        ----------
        height_list : list[int]
            List of heights.

        Returns
        -------
        mean_height : float
            the average/mean of the list of numbers.

        '''
        try:
            mean_height = sum(height_list)/len(height_list)
            return mean_height # The average height of everyone in the list (6.55 feet!)
        except ValueError:
                print("Incorrect value type")
    #Median
    def calc_median(height_list):
        '''        
        Get the median from the list of heights

        Parameters
        ----------
        height_list : list[int]
            list of heights.

        Returns
        -------
        median : float
            the median value from the list of numbers.

        '''
        try:
            height_list_sorted = sorted(height_list)  
            mid_index_median = int(len(height_list_sorted)/2)
            if len(height_list) %2 ==1:
                median = height_list_sorted[mid_index_median]
            else:
                median = (height_list_sorted[mid_index_median - 1] + height_list_sorted[mid_index_median])/2
                return median 
        except ValueError:
                print("Incorrect value type")
    
    #Mode
    def calc_mode(height_list):
        '''       
        Get the mode from the list of heights

        Parameters
        ----------
        height_list : list[int]
            list of heights.

        Returns
        -------
        mode : int
            The mode from the list of heights.

        '''
        try:
            distinct_height = sorted(list(set(height_list)))   
            frequencies = [height_list.count(height) for height in distinct_height ]
            max_freq = max(frequencies)
            max_index = frequencies.index(max_freq)
            mode = distinct_height[max_index]
            return mode
        except ValueError:
                print("Incorrect value type")
    
    #Maximum
    def calc_max(height_list):
        '''        
        Get the maximum value from the list of heights

        Parameters
        ----------
        height_list : list[int]
            List of integers.

        Returns
        -------
        maximum : int
            maximum value from the list of heights.

        '''
        try:
            maximum = max(height_list)
            return maximum
        except ValueError:
                print("Incorrect value type")

    #Minimum
    def calc_min(height_list):
        '''       
        Get the minimum value from the list of heights

        Parameters
        ----------
        height_list : list[int]
            list of integers.

        Returns
        -------
        minimum : int
            minimum value from the list of heights.

        '''
        try:
            minimum = min(height_list)
            return minimum
        except ValueError:
                print("Incorrect value type")
    
    #Standard Deviation
    def calc_std_dev(height_list):
        '''        
        Get the standard deviation from the list of heights

        Parameters
        ----------
        height_list : list[int]
            list of integers.

        Returns
        -------
        std_dev : float
            the standard deviation from the list of integers.

        '''
        try:
            mean_height = sum(height_list)/len(height_list)
            squared_deviations = [(height - mean_height) ** 2 for height in height_list]
            std_dev = sqrt(sum(squared_deviations)/(len(height_list)-1))
            return std_dev
        except ValueError:
                print("Incorrect value type")
    
    #Inter-Quartile Range 25%
    def calc_iqr(height_list):
        '''       
        Get the interquartile range from the list of heights. 
        Get the 25th percentile and the 75th percentile and subtract them to get the interquartile

        Parameters
        ----------
        height_list : list[int]
            list of integers.

        Returns
        -------
        IQR : int
            the interquartile range from the list of heights.

        '''
        try:
            sort_data_25 = sorted(height_list)
            index_25 = len(sort_data_25)*.25
            rounded_25 = round(index_25)
            sort_data_25[rounded_25] 
            #Inter-Quartile Range 75%
            sort_data_75 = sorted(height_list)
            index_75 = len(sort_data_75)*.75
            rounded_75 = round(index_75)
            sort_data_75[rounded_75]  
            #IQR
            IQR = (sort_data_75[rounded_75]) - (sort_data_25[rounded_25])
            return IQR
        except ValueError:
                print("Incorrect value type")
    #Skewness
    def calc_skewness(height_list):
        '''       
        Calcualte the skewness of the data. Get the mode and median skewness 

        Parameters
        ----------
        mean_height : float
            average height from the height_list
        mode : int
            mode from the heightlist.
        std_dev : float
            the standard deviation of the data calculated above.
        median : float
            the median of the height_list calcualted above.

        Returns
        -------
        mode_skewness : float
            mode skewness of the data.
        median_skewness : float
            median skewness of the data.

        '''
        try:
            #Get the standard deviation
            mean_height = sum(height_list)/len(height_list)
            squared_deviations = [(height - mean_height) ** 2 for height in height_list]
            std_dev = sqrt(sum(squared_deviations)/(len(height_list)-1))
            #Get the mode
            distinct_height = sorted(list(set(height_list)))   
            frequencies = [height_list.count(height) for height in distinct_height ]
            max_freq = max(frequencies)
            max_index = frequencies.index(max_freq)
            mode = distinct_height[max_index]
            #Get the mean
            mean_height = sum(height_list)/len(height_list)
            #get the median
            height_list_sorted = sorted(height_list)
            mid_index_median = int(len(height_list_sorted)/2)
            if len(height_list) %2 ==1:
                median = height_list_sorted[mid_index_median]
            else:
                median = (height_list_sorted[mid_index_median - 1] + height_list_sorted[mid_index_median])/2
            
            
            mode_skewness = (mean_height - (mode))/std_dev
            median_skewness = 3*(mean_height - median)/std_dev
            return mode_skewness, median_skewness
        except ValueError:
                print("Incorrect value type")
    
    #Correlation between height and weight
    def calc_correlation(height_list, weight_list):
        '''       
        Calculate the correlation between the height and weight

        Parameters
        ----------
        height_list : list [int]
            list of heights.
        weight_list : list[int]
            list of weights.

        Returns
        -------
        correlation : float
            the correlation between height and weight.

        '''
        try:
            x_mean = sum(weight_list)/len(weight_list)
            y_mean = sum(height_list)/len(height_list)
        
            x_deviations = [x - x_mean for x in weight_list]
            y_deviations = [y - y_mean for y in height_list]
        
            xy_deviations = [ x*y for (x,y) in  zip(x_deviations, y_deviations)]
        
            x_squared_deviations = [(x - x_mean)**2 for x in weight_list]
            y_squared_deviations = [(y - y_mean)**2 for y in height_list]
        
            correlation = sum(xy_deviations)/sqrt(sum(x_squared_deviations)*sum(y_squared_deviations))
            return correlation
        except ValueError:
                print("Incorrect value type")
        
    #Histogram
    def histogram(height_list):
        '''        
        Create a histogram of the heights

        Parameters
        ----------
        height_list : list[int]
            list of heights.

        Returns
        -------
        None.

        '''
        try:
            # Create the figure and axes
            fig, ax = plt.subplots()
            # Set the title for the figure
            fig.suptitle("Histogram of Player Height")
            # 1 histogram    
            # Set the title
            #ax.set_title("Histogram of patient data")
            # set the axis labels
            ax.set_xlabel("Height (cm)")
            ax.set_ylabel("Frequency")
            # create a list for the histogram boundaries
            bins_list = [i for i in range(170,max(height_list)+10,5)]
            # set the ticks on the x-axis
            ax.set_xticks(bins_list)
            # Display a histogram of the patient numbers
            ax.hist(height_list, bins=bins_list,ec="black")
            plt.show()
        except ValueError:
            print("Incorrect value type")

    #Box Plot
    def boxplot(height_list):
        '''      
        Generate a boxplot of the heights in the list

        Parameters
        ----------
        height_list : list[int]
            list of heights.

        Returns
        -------
        None.

        '''
        try:
            fig, ax = plt.subplots()
            ax.set_ylabel("Height(cm)")
    
            ax.set_title("Boxplot of NBA Players Height in NBA 2k20")
            ax.boxplot(height_list)
            plt.show()
        except ValueError:
            print("Incorrect value type")
    
    #Violin Plot
    def violinplot(height_list):
        '''      
        Generate a violin plot of the ist of heights in the list

        Parameters
        ----------
        height_list : list[int]
            list of heights.

        Returns
        -------
        None.

        '''
        try:
            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            ax.set_ylabel("Height(cm)")
            ax.set_title("Violin Plot of Height of Players in NBA 2k20")
            ax.violinplot(height_list, showmedians=True)
            plt.show()
        except ValueError:
            print("Incorrect value type")
    
    #Scatterplot
    def scatterplot(height_list, weight_list):
        '''      
        Generate a scatterplot of the heights in the list

        Parameters
        ----------
        height_list : list[int]
            list of heights.

        Returns
        -------
        None.

        '''
        try:
            fig, ax = plt.subplots()
            ax.set_xlabel("Weight(lbs)")
            ax.set_ylabel("Height(cm)")
            ax.set_title("Height(cm) v Weight(lbs)")
            ax.scatter(weight_list, height_list, marker=".")
            plt.show()
        except ValueError:
            print("Incorrect value type")
    
except (FileNotFoundError, PermissionError):
        print("Unable to open the file nba2k20_players.csv")
        
if __name__ == "__main__":
    print("Total number of values", number_of_values(height_list))
    print("Total Height", total_height(height_list))
    print(f"Mean height: {calc_mean(height_list):.1f} cm")
    print(f"Median height: {calc_median(height_list)} cm")
    print("Mode height:", calc_mode(height_list), "cm")
    print("Maximum:", calc_max(height_list))
    print("Minimum:", calc_min(height_list))
    print(f"Standard Deviation of height: {calc_std_dev(height_list):.2f} cm")
    print("IQR:", calc_iqr(height_list))
    print("Mode Skewness & Median Skewness:", calc_skewness(height_list))    
    print(f"The correlation between Height(cm) (y) and Weight(lbs) (x): {calc_correlation(height_list, weight_list):.1f}")
    histogram(height_list)
    boxplot(height_list)
    violinplot(height_list)
    scatterplot(height_list, weight_list)
    
    
    

    
    