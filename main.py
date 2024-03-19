import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')
# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    data = [row for row in csvreader]

def total_months(data):
    return len(data) 

def total_sum(data):
    return sum(int(row[1]) for row in data)

def total_average(data):
    total_change = 0
    total_months_count = len(data)
    for i in range(1, len(data)):
        change = int(data[i][1]) - int(data[i - 1][1])
        total_change += change
    return total_change / (total_months_count-1 )

def greatest_increase(data):
    max_increase = 0
    max_increase_month = ""
    for i in range(1, len(data)):
        change = int(data[i][1]) - int(data[i-1][1])
        month = data[i][0]
        if change > max_increase:
            max_increase = change
            max_increase_month = month
    return max_increase_month, max_increase

def greatest_decrease(data):
    max_decrease = float('inf')
    max_decrease_month = ""
    for i in range(1, len(data)):
        change = int(data[i][1]) - int(data[i-1][1])
        month = data[i][0]
        if change < max_decrease:
            max_decrease = change
            max_decrease_month = month
    return max_decrease_month, max_decrease

total_months_count = total_months(data)
total_sum_value = total_sum(data)
total_average_value = total_average(data)
greatest_increase_date, greatest_increase_value = greatest_increase(data)
greatest_decrease_date, greatest_decrease_value = greatest_decrease(data)

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months_count}")
print(f"Total: ${total_sum_value}")
print(f"Average Change: ${total_average_value:.2f}")

# Display the greatest increase in profits
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})")
# Display the greatest decrease in profits
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})")

output_file_path = "financial_analysis.txt"
with open(output_file_path, "w") as output_file:
    output_file.write(f"Financial Analysis\n")
    output_file.write(f"----------------------------\n")
    output_file.write(f"Total Months: {total_months_count}\n")
    output_file.write(f"Total: ${total_sum_value}\n")
    output_file.write(f"Average Change: ${total_average_value:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})\n")
