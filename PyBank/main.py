import os
import csv

pybank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")
# PyBank/Resources/budget_data.csv

# set initial variables and create lists to store data
profit = []
changes = []
date = []
total_profit = 0
total_profit_change = 0
profit_previous = None

#open csv 
with open(pybank_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)

    for row in csvreader: 
        profit_current = int(row[1])
        # read each row in the file and start to add up total profits
        profit.append(row[1])
        total_profit = total_profit + profit_current
        
        # kourt from tutoring helped me figure out this if statement
        if profit_previous is not None:

            # get the monthly profit change and store the month of change
            monthly_profit_change = profit_current - profit_previous
            date.append(row[0])

            #store the monthly profit change into the list we defined above
            changes.append(monthly_profit_change)
            total_profit_change = total_profit_change + monthly_profit_change
        
        # update the variable to calculate change
        profit_previous = profit_current

# find the maximum and minumum of the info in our changes list for the greatest increase/decrease
greatest_increase = max(changes)
greatest_decrease = min(changes)

# store the dates that go alongside those greatest increase/decrease amounts
increase_date = date[changes.index(greatest_increase)]
decrease_date = date[changes.index(greatest_decrease)]

#get the average change to plug into the table that prints out, + 1 since we didn't track the first month
month_number = len(date) + 1

# this was done in conjunction with kourt from tutoring
average_change = round(
    total_profit_change/(month_number - 1), 
    2)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month_number))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")")


file = open("analysis.txt", "w")
file.write("Financial Analysis" + "\n")
file.write("----------------------------" + "\n")
file.write("Total Months: " + str(month_number) + "\n")
file.write("Total: $" + str(total_profit) + "\n")
file.write("Average Change: $" + str(average_change) + "\n")
file.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")" + "\n")
file.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")" + "\n")
file.close