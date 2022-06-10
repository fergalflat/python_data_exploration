# -*- coding: utf-8 -*-
"""
Student ID: A00291231
Purpose: Perform analysis on a category that has had its values added to a dictionary
"""
from matplotlib import pyplot as plt

team_dict = {}
team_dict2 = {}

try:       
    #Open the data set and initialise it to "csv_file"
    with open ("nba2k20_players.csv") as data_file:
        _ = data_file.readline()
    #for each line in the csv, split each variable by a comma. The add the value from the height row(row 6) to the list
        for line in data_file:
            try:
                fullName, rating, jersey, team, bDay, height, weight, salary, country = line.split(",")
                                 
                if team not in team_dict:            
                    team_dict[team] = int(salary)
                else:
                    team_dict[team] += int(salary)
                
                #If a  team is not in the dictionary add the team and the salary, else, append the salary to the dictionary line
                if not team in team_dict2:
                    team_dict2[team] = [int(salary)]
                else:
                    team_dict2[team].append(int(salary))
            except ValueError:
                print("Your input is not in correct format")
        
    def number_of_categories(team_dict):
        '''       
        Get the number of distinct categories from the dictionary

        Parameters
        ----------
        team_dict : dictionary{int}
            dictionary of NBA teamas along with the salary.

        Returns
        -------
        number : int
            the amount of distinct NBA teamas in the dictionary.

        '''
        try:
            number = len(team_dict)
            return number
        except ValueError:
            print("Incorrect value type")
    
    def highest_number_of_values(team_dict2):
        '''       
        Return the dictionary key(team) that has the most salarys associated with it

        Parameters
        ----------
        team_dict2 : dictionatry{list}
            dictionary of NBA teams along with a list of NBA salarys associated with them.

        Returns
        -------
        highest_no : string
            the team that has the most salarys associated with it.

        '''
        try:
            highest_no = max(team_dict2, key=lambda k: len(team_dict2[k]))
            return highest_no
        except ValueError:
            print("Incorrect value type")
    
    def lowest_number_of_values(team_dict2):
        '''       
        The team with the lowest number of salarys associated with it

        Parameters
        ----------
        team_dict2 : dictionary{list}
            dictionary of NBA teams along with a list of NBA salarys associated with them..

        Returns
        -------
        lowest_no : string
            the team with the least amount of salarys associated with it
        '''
        try:
            lowest_no = min(team_dict2, key=lambda k: len(team_dict2[k]))
            return lowest_no
        except ValueError:
            print("Incorrect value type")
            
    def highest_total(team_dict):
        '''        
        Get the team that has the highest spend on salaries

        Parameters
        ----------
        team_dict : dictionary{int}
            dictionary of NBA teamas along with the salary.

        Returns
        -------
        highest_tot : string
            the nba team with the highest total salary associated with it.

        '''
        try:
            highest_tot =  max(team_dict, key=team_dict.get)
            return highest_tot
        except ValueError:
            print("Incorrect value type")
    
    def lowest_total(team_dict):
        '''       
        Get the team that has the lowest spend on salaries

        Parameters
        ----------
        team_dict : dictionary{int}
            dictionary of NBA teamas along with the salary.

        Returns
        -------
        lowest_tot : string
            the nba team with the lowest total salary associated with it.

        '''
        try:
            lowest_tot = min(team_dict, key=team_dict.get)
            return lowest_tot
        except ValueError:
            print("Incorrect value type")

    def piechart(team_dict):
        '''      
        create a pie chart of the percentage number of values in each category

        Parameters
        ----------
        team_dict : dictionary{int}
            dictionary of NBA teamas along with the salary.

        Returns
        -------
        None.

        '''
        try:
            fig, ax = plt.subplots()
            ax.set_title("Pie Chart of % number of values in each category")
            ax.pie(team_dict.values(), labels = team_dict.keys(), autopct="%.0f%%", textprops={'fontsize': 6})
            plt.show()
        except ValueError:
            print("Incorrect value type")

    def boxplot2(team_dict2):
        '''       
        boxplot of each team and their salary

        Parameters
        ----------
        team_dict2 : dictionary{list}
            dictionary of NBA teams along with a list of NBA salarys associated with them.

        Returns
        -------
        None.

        '''
        try:
            fig, ax = plt.subplots()
            ax.set_title("Box Plots for each team's salary")
            ax.set_xlabel("Salary in 10s of Millions (1.0 = 10 Million)", fontsize=8)
            ax.set_ylabel("Teams", fontsize=8)
            for label in (ax.get_xticklabels() + ax.get_yticklabels()):label.set_fontsize(7)
            ax.boxplot(team_dict2.values(), showfliers=True, vert=False, labels=team_dict2.keys())
            plt.show()
        except ValueError:
            print("Incorrect value type")
            
except (FileNotFoundError, PermissionError):
    print("Unable to open the file nba2k20_players.csv")
    
if __name__ == "__main__":
    print("Number of distinct teams/categories:", number_of_categories(team_dict))
    print("Category with the highest number of values:", highest_number_of_values(team_dict2))
    print("Category with the lowest number of values:", lowest_number_of_values(team_dict2))
    print("Category with the highest salary/total:",  highest_total(team_dict))
    print("Category with the lowest salary/total:",  lowest_total(team_dict))
    piechart(team_dict)
    boxplot2(team_dict2)