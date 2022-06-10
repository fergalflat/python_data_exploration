# -*- coding: utf-8 -*-
"""
Student ID: A00291231
Purpose: Menu for running calculations
"""
#import all necessary modules
from assignment_a import number_of_values, total_height, calc_mean, calc_median, calc_mode, calc_max, calc_min, calc_std_dev, calc_iqr, calc_skewness, calc_correlation,histogram, boxplot, violinplot, scatterplot, height_list, weight_list
from assignment_b import number_of_categories, highest_number_of_values, lowest_number_of_values, highest_total, lowest_total,boxplot2 , piechart, team_dict, team_dict2
from assignment_c import earliest_date, latest_date, delta_fn, date_high_value, date_low_value, average_value, date_plot, bar_chart, dates_data, dates_data2

try:
    choice = 0 # set a variable to 0
    while choice != 99: #while the input variable is not 99 do the following
        print("")
        print("Enter '1' for List analysis(part a)")
        print("Enter '2' for Dictionary analysis(part b")
        print("Enter '3' for Date analysis(part c)")
        print("Enter '99' to exit")
        
        choice = int(input("Input Menu Choice: ")) #user inputs a value corresponding to one of the above
    
        if choice == 1: # if user inputs 1, do the following
            option_a = 0
            while option_a != 99: #allow the user to leave this part of the menu by pressing 99 and go back to the main menu
                print("")
                print("Enter '1' for the number of values")
                print("Enter '2' for the total(sum) of the values")
                print("Enter '3' for the mean of the values")
                print("Enter '4' for the median of the values")
                print("Enter '5' for the mode of the values")
                print("Enter '6' for the max value")
                print("Enter '7' for the min value")
                print("Enter '8' for the standard deviation")
                print("Enter '9' for the Inter quartile range")
                print("Enter '10' for the Skewness")
                print("Enter '11' for the correlation")
                print("Enter '12' for the histogram")
                print("Enter '13' for the boxplot")
                print("Enter '14' for the violin plot")
                print("Enter '15' for the scatterplot")
                print("Enter '99' to return to main menu")
                option_a = int(input("Input an option from 1-15 from above: "))
                #depending on the users input, perform a function from part a
                if option_a == 1:
                    print("Total number of values:", number_of_values(height_list))
                elif option_a ==2:
                    print("Total(sum) of the values", total_height(height_list))
                elif option_a ==3:
                    print(f"Mean of the values: {calc_mean(height_list):.1f}")
                elif option_a ==4:
                    print(f"Median of the values: {calc_median(height_list):.1f}")
                elif option_a ==5:
                    print("Mode of the values:", calc_mode(height_list))
                elif option_a ==6:
                    print("The max value:", calc_max(height_list))
                elif option_a ==7:
                    print("The min value:", calc_min(height_list))
                elif option_a ==8:
                    print(f"The standard deviation of the values: {calc_std_dev(height_list):.2f}")
                elif option_a ==9:
                    print("The Interquartile range of the values:", calc_iqr(height_list))
                elif option_a ==10:
                    print("The skewness of the values:", calc_skewness(height_list))
                elif option_a ==11:
                    print(f"The correlation between the weight and height of the playeers: {calc_correlation(height_list, weight_list):.1f}")
                elif option_a ==12:
                    print(histogram(height_list))
                elif option_a ==13:
                    print(boxplot(height_list))
                elif option_a ==14:
                    print(violinplot(height_list))
                elif option_a ==15:
                    print(scatterplot(height_list, weight_list))
                elif option_a ==99:
                    break
                else:
                    print("Invalid input - Try again")
                
        elif choice == 2:#if the user chooses the category section (b)
            option_b = 0
            while option_b != 99:
            #give the user a menu to choose from for part b
                print("")
                print("Enter '1' for the number of teams/categories")
                print("Enter '2' for the team with the most salaries associated with it")
                print("Enter '3' for the team with the lowest number of salaries associated with it")
                print("Enter '4' for the team that has the highest spend on salaries (highest salary total)")
                print("Enter '5' for the team that has the lowest spend on salaries (lowest salary total)")
                print("Enter '6' for a pie chart of the percentage number of values (salaries) in each category")
                print("Enter '7' for a boxplot of each team and their salary")
                print("Enter '99' to return to main menu")
                option_b = int(input("Input an option from 1-7 from above: "))
                #depending on the users input, perform a function from part b
                if option_b == 1:
                    print("The number of teams/categories:", number_of_categories(team_dict))
                elif option_b ==2:
                    print("The team with the most salaries associated with it:", highest_number_of_values(team_dict2))
                elif option_b ==3:
                    print("The team with the lowest number of salaries associated with it:", lowest_number_of_values(team_dict2))
                elif option_b ==4:
                    print("The team that has the highest spend on salaries (highest salary total):", highest_total(team_dict))
                elif option_b ==5:
                    print("The team that has the lowest spend on salaries (lowest salary total):", lowest_total(team_dict))
                elif option_b ==6:
                    print(piechart(team_dict))
                elif option_b ==7:
                    print(boxplot2(team_dict2))
                elif option_b ==99:
                    break
                else:
                    print("Invalid input - Try again")
        
        elif choice == 3:
            option_c = 0
            while option_c != 99:
            #give the user a menu to choose from for part c
                print("")
                print("Enter '1' for the earliest date in the dictionary")
                print("Enter '2' for the latest date in the dictionary")
                print("Enter '3' for the difference, in days, between the earliest and latest dates")
                print("Enter '4' for the date with the highest value associated with it")
                print("Enter '5' for the date with the lowest value associated with it")
                print("Enter '6' for the average value per date")
                print("Enter '7' for a date plot of all heights in the dictionary")
                print("Enter '8' for a bar chart of all months and their cumulative height")
                print("Enter '99' to return to main menu")
                option_c = int(input("Input an option from 1-8 from above: "))
                #depending on the users input, perform a function from part c
                if option_c == 1:
                    print("The earliest date in the dictionary:", earliest_date(dates_data))
                elif option_c ==2:
                    print("The latest date in the dictionary:", latest_date(dates_data))
                elif option_c ==3:
                    print("The difference, in days, between the earliest and latest dates:", delta_fn(dates_data))
                elif option_c ==4:
                    print("The date with the highest value associated with it:", date_high_value(dates_data))
                elif option_c ==5:
                    print("The date with the lowest value associated with it:", date_low_value(dates_data))
                elif option_c ==6:
                    print(f"The average value per date: {average_value(dates_data):.1f}")
                elif option_c ==7:
                    print(date_plot(dates_data))
                elif option_c ==8:
                    print(bar_chart(dates_data2))
                elif option_c ==99:
                    break
                else:
                    print("Invalid input - Try again")
       #exis the program if the user enters 99        
        elif choice == 99:
            break
        
        else:
            print("Invalid input - Try again")
except ValueError:
    print("Your input is not in correct format - Exiting")