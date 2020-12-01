import os
import csv

budget_data_csv = os.path.join('Resources','budget_data.csv')

# Counter variable for the total number of months
total_months = 0

# Blank variable for the net profit / loss and prior month
net_ProfitLoss = 0
prior_month = 0

# Creates a blank list for changes in profits and losses and months
change_ProfitLoss = []
months = []

with open(budget_data_csv, newline="") as csvfile:
    
    # Splits the csv by commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Code to fill the months list, find the total number of months, and calculate net profit / loss
    for row in csvreader:
        months.append(row[0])
        current_month_ProfitLoss = int(row[1])
        if total_months > 0:
            
            #this will return false the first iteration because it is the first item in the column
            total_month_change = current_month_ProfitLoss - prior_month
            change_ProfitLoss.append(total_month_change)

        # Updates prior month value for the next loop to current month value
        prior_month = current_month_ProfitLoss
        total_months = total_months + 1

        # Adds the current month profit / loss to the net total each iteration
        net_ProfitLoss = net_ProfitLoss + current_month_ProfitLoss
    
    # This calulates the average profit / loss across all months
    month_average = sum(change_ProfitLoss)/len(change_ProfitLoss)
    
    # The following calculates the greatest profit and loss and the corresponding months
    max_profit = max(change_ProfitLoss)
    max_profit_month = months[change_ProfitLoss.index(max_profit)+1]

    max_loss = min(change_ProfitLoss)
    max_loss_month = months[change_ProfitLoss.index(max_loss)+1]

#print statements
print(f'Financial Analysis')
print(f'-------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_ProfitLoss}')
print(f'Average Change: ${month_average:.2f}')
print(f'Greatest Increase in Profits: {max_profit_month} (${max_profit})')
print(f'Greatest Decrease in Profits: {max_loss_month} (${max_loss})')

#Print to a new text file
pybank_analysis = os.path.join('Analysis', 'pybank_analysis.txt')
with open(pybank_analysis, 'w') as text_file:
    text_file.write(f'Financial Analysis\n')
    text_file.write(f'-------------------------------\n')
    text_file.write(f'Total Months: {total_months}\n')
    text_file.write(f'Total: ${net_ProfitLoss}\n')
    text_file.write(f'Average Change: ${month_average:.2f}\n')
    text_file.write(f'Greatest Increase in Profits: {max_profit_month} (${max_profit})\n')
    text_file.write(f'Greatest Decrease in Profits: {max_loss_month} (${max_loss})\n')