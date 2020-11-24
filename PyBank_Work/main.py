# PyBank Code
import os
import csv

budget_data_csv = os.path.join("Resources","budget_data.csv")

# Define the function
def budget_calc(budget_data):
    date = str(budget_data[0])
    profit_losses = int(budget_data[1])




















with open(budget_data_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader: