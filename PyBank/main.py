# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period


# As an example, your analysis should look similar to the one below:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


#tutor notes 
# 'pybank.csv'
# os.path.join('folder', 'subfolder', 'py_bank')
# 'folder/subfolder/py_bank.csv'
# ','.join('folder', 'subfolder', 'py_bank')
# 'folder,subfolder,py_bank.csv'

# Define the function and have it accept the 'budget_data' as its sole parameter

# to read a csv file (text)
# location the file from within the directory
# use a input/output file reader to read the characters in this text
# use a text parser to searate each value (by comma?)

# str, int, float, bool, lists, dictionary
# create custom data types on top of these elements

import os
import csv

csvpath = os.path.join('budget_data.csv')

# Defining list & itializing start points
profit = []
monthly_delta = []
date = []

total_profit = 0
total_change_profits = 0
initial_profit = 0


#open file 
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)    

    
    for row in csvreader:    
        profit.append(row[1]) 
        
        # The net total amount of "Profit/Losses" over the entire period
        total_profit = total_profit + int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        final_profit = int(row[1])
        delta_profit = final_profit - initial_profit

        monthly_delta.append(delta_profit)

        total_change_profits = total_change_profits + delta_profit
        initial_profit = final_profit

        average_change = (total_change_profits/(len(profit)))
      
        #Find the max and min change in profits and the corresponding dates these changes were obeserved
        greatest_increase_profits = max(monthly_delta)
        greatest_decrease_profits = min(monthly_delta)
        #print(greatest_increase_profits)
        
        date.append(row[0])
        increase_date = date[monthly_delta.index(greatest_increase_profits)]
        decrease_date = date[monthly_delta.index(greatest_decrease_profits)]
        #print(increase_date)
        
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print(f"Total Months: {len(profit)}")
    print(f"Total Profits: ${total_profit}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase_profits}")
    print(f"Greatest Decrease in Profits: {decrease_date} ${greatest_decrease_profits}")
    print("----------------------------------------------------------")
 

#print(total_profit)
#print(delta_profit)
#print(profit_list)