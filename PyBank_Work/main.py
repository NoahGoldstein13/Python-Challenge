import os
import csv

budget_data_csv = os.path.join('Resources','budget_data.csv')

# 
total_months = 0

net_ProfitLoss = 0

# Creates blank list for average changes in profits and losses
average_change_ProfitLoss = []

prior_month = 0

months = []

with open(budget_data_csv, newline="") as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #row represents a list
    for row in csvreader:
        months.append(row[0])
        current_month_ProfitLoss = int(row[1])
        if total_months > 0:
            #this will return false the first time because its the first item in the column, first item not greater than first item in row[1]
            total_month_change = current_month_ProfitLoss - prior_month
            average_change_ProfitLoss.append(total_month_change)
          

        #sets previous month from 0 to row 1
        prior_month = current_month_ProfitLoss
        total_months = total_months + 1
        #converting from str to int and redefine the amoutnt of net total amount
        #taking current value of net total amount and adding the row value to it which becomes the new net total amount
        net_ProfitLoss = net_ProfitLoss + current_month_ProfitLoss
    #this is the average formula for the average of the list called average change
    month_average = sum(average_change_ProfitLoss)/len(average_change_ProfitLoss)
    
    max_profit = max(average_change_ProfitLoss)
    max_profit_month = months[average_change_ProfitLoss.index(max_profit)+1]

    max_loss = min(average_change_ProfitLoss)
    max_loss_month = months[average_change_ProfitLoss.index(max_loss)+1]

#print statements
print(f'Financial Analysis')
print(f'-------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_ProfitLoss}')
print(f'Average Change: ${month_average:.2f}') #two decimal points
print(f'Greatest Increase in Profits: {max_profit_month} (${max_profit})')
print(f'Greatest Decrease in Profits: {max_loss_month} (${max_loss})')

#Text file output
pybank_analysis = os.path.join('Analysis', 'pybank_analysis.txt')
with open(pybank_analysis, 'w') as text_file:
    textwriter = text_file.write(f'Financial Analysis\n')
    textwriter = text_file.write(f'-------------------------------\n')
    textwriter = text_file.write(f'Total Months: {total_months}\n')
    textwriter = text_file.write(f'Total: ${net_ProfitLoss}\n')
    textwriter = text_file.write(f'Average Change: ${month_average:.2f}\n')
    textwriter = text_file.write(f'Greatest Increase in Profits: {max_profit_month} (${max_profit})\n')
    textwriter = text_file.write(f'Greatest Decrease in Profits: {max_loss_month} (${max_loss})\n')