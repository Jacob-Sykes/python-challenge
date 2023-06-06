
import os

import csv

# Path to collect data from Resources folder
budget_data = os.path.join('Resources','budget_data.csv')

with open(budget_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        csv_header = next(csvreader)
        profit = []        
        month = []
        profit_change = []
        
        for row in csvreader:
            profit.append(float(row[1]))
            month.append(row[0])

# Print out beginning portion of repot

        print("Financial Analysis")

        print("------------------")

        print("Total Months:", len(month))

        print("Total: $", sum(profit))

# Loop through profit to determine change, increase, and decrease of profits
        for i in range(1, len(profit)):
            profit_change.append(profit[i] - profit[i-1])
            avg_profit_change = sum(profit_change)/len(profit_change)
            max_profit_change = max(profit_change)
            min_profit_change = min(profit_change)

            max_profit_change_date = str(month[profit_change.index(max(profit_change))])
            min_profit_change_date = str(month[profit_change.index(min(profit_change))])

# Print the rest of report
        print("Average Change: $", round(avg_profit_change))

        print("Greatest Increase in Profits:", max_profit_change_date,"($", max_profit_change,")")

        print("Greatest Decrease in Profits:", min_profit_change_date,"($", min_profit_change,")")

# Write prints to output text file
output_file = open('output.txt', 'w')

output_file.write("Financial Analysis\n")

output_file.write("------------------\n")

output_file.write("Total Months: {}\n".format(len(month)))

output_file.write("Total: $ {}\n".format(sum(profit)))

output_file.write("Average Change: $ {}\n".format(round(avg_profit_change)))

output_file.write("Greatest Increase in Profits: {} ($ {})\n".format(max_profit_change_date, max_profit_change))

output_file.write("Greatest Decrease in Profits: {} ($ {})\n".format(min_profit_change_date, min_profit_change))


# Close file
output_file.close()



















