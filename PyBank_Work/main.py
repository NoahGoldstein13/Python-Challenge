import os
import csv

budget_data_csv = os.path.join('Resources','budget_data.csv')

# 
total_months = 0

net_ProfitLoss = 0

# Creates blank list for average changes in profits and losses
average_change_ProfitLoss = []

prior_month = 0

greatest_monthly_profit = {"profit": -100000}
lowest_monthly_profit = {"profit": 100000}
greatest_month = {"month": " "}
lowest_month = {"month": " "}

with open(budget_data_csv, newline="") as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #row represents a list
    for row in csvreader:
        current_month_ProfitLoss = int(row[1])
        if total_months > 0:
            #this will return false the first time because its the first item in the column, first item not greater than first item in row[1]
            total_month_change = current_month_ProfitLoss - prior_month
            average_change_ProfitLoss.append(total_month_change)
            if greatest_monthly_profit["profit"] < total_month_change:
                greatest_monthly_profit["profit"] = total_month_change
                greatest_month["month"] = row[0]
            if lowest_monthly_profit["profit"] > total_month_change:
                lowest_monthly_profit["profit"] = total_month_change
                lowest_month["month"] = row[0]

        #sets previous month from 0 to row 1
        prior_month = current_month_ProfitLoss
        total_months = total_months + 1
        #converting from str to int and redefine the amoutnt of net total amount
        #taking current value of net total amount and adding the row value to it which becomes the new net total amount
        net_ProfitLoss = net_ProfitLoss + current_month_ProfitLoss
    #this is the average formula for the average of the list called average change
    month_average = sum(average_change_ProfitLoss)/len(average_change_ProfitLoss)

#print statements
print(f'Financial Analysis')
print(f'-------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_ProfitLoss}')
print(f'Average Change: ${month_average:.2f}') #two decimal points
print(f'Greatest Increase in Profits: {greatest_month["month"]} (${greatest_monthly_profit["profit"]})')
print(f'Greatest Decrease in Profits: {lowest_month["month"]} (${lowest_monthly_profit["profit"]})')

#Text file output
pybank_analysis_text_file = os.path.join('Analysis', 'pybank_analysis.txt')
with open(pybank_analysis_text_file, 'w') as text_file:
    textwriter = text_file.write(f'Financial Analysis\n')
    textwriter = text_file.write(f'-------------------------------\n')
    textwriter = text_file.write(f'Total Months: {total_months}\n')
    textwriter = text_file.write(f'Total: ${net_ProfitLoss}\n')
    textwriter = text_file.write(f'Average Change: ${month_average:.2f}\n')
    textwriter = text_file.write(f'Greatest Increase in Profits: {greatest_month["month"]} (${greatest_monthly_profit["profit"]})\n')
    textwriter = text_file.write(f'Greatest Decrease in Profits: {lowest_month["month"]} (${lowest_monthly_profit["profit"]})\n')