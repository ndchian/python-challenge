import os
import csv

pybank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")
# PyBank/Resources/budget_data.csv

# set initial variables and create lists to store data
profit = []
changes = []
date = []
month_number = 0
total_profit = 0
total_profit_change = 0
profit_start = 0

#open csv 
with open(pybank_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)

    for row in csvreader: 

        #to total up the number of months in this data set and store date for greatest increase/decrease
        month_number = month_number + 1
        date.append(row[0])

        # calculate the total profit
        profit.append(row[0])
        total_profit = total_profit + int(row[1])

        # get the monthly profit change
        profit_end = int(row[1])
        monthly_profit_change = profit_end - profit_start

        #store the monthly profit change into the list we defined above
        changes.append(monthly_profit_change)
        total_profit_change = total_profit_change + monthly_profit_change
        profit_start = profit_end

        #get the average change to plug into the table that prints out
        average_change = (total_profit_change/month_number)

        # find the maximum and minumum of the info in our changes list for the greatest increase/decrease
        greatest_increase = max(changes)
        greatest_decrease = min(changes)

        # store the dates that go alongside those greatest increase/decrease amounts
        increase_date = date[changes.index(greatest_increase)]
        decrease_date = date[changes.index(greatest_decrease)]


print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month_number))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(int(average_change)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")")
