import os
import csv

pybank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")
# PyBank/Resources/budget_data.csv
profit = []
changes = []
date = []
month_number = 0
total_profit = 0
total_profit_change = 0
profit_start = 0

with open(pybank_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)

    for row in csvreader: 
        month_number = month_number + 1
        date.append(row[0])
        profit.append(row[0])
        total_profit = total_profit + int(row[1])
        profit_end = int(row[1])
        monthly_profit_change = profit_end - profit_start
        changes.append(monthly_profit_change)
        total_profit_change = total_profit_change + monthly_profit_change
        profit_start = profit_end
        average_change = (total_profit_change/month_number)


        greatest_increase = max(changes)
        greatest_decrease = min(changes)

        increase_date = date[changes.index(greatest_increase)]
        decrease_date = date[changes.index(greatest_decrease)]


print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month_number))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(int(average_change)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")")
