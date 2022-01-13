import os
from csv import DictReader

# Get path to csv file.
project_root = os.path.dirname(__file__)
csv_path = os.path.join(project_root, 'Resources', 'budget_data.csv')

# Initialize variables.
profit_total = 0
profit_greatest_increase = {'value': 0, 'month': ''}
profit_greatest_decrease = {'value': 0, 'month': ''}
profit_change_sum = 0

# Read file and calculate statistics.
with open(csv_path,'r') as file:
    reader = DictReader(file)

    for i, row in enumerate(reader):
        month = row['Date']
        profit = int(row['Profit/Losses'])
        profit_total += profit

# Calculate profit change stats.  
# The first month is excluded because a there is no previous month to compare it to.
        if i != 0:
            profit_change = profit - profit_previous
            profit_change_sum += profit_change
            
            if profit_change > profit_greatest_increase['value']:
                profit_greatest_increase['value'] = profit_change
                profit_greatest_increase['month'] = month
            
            if profit_change < profit_greatest_decrease['value']:
                profit_greatest_decrease['value'] = profit_change
                profit_greatest_decrease['month'] = month

        profit_previous = profit

        
profit_change_average = profit_change_sum/i

# Format results.
results_formatted = 'Financial Analysis\n' \
    f'----------------------------\n' \
    f'Total Months: {i + 1}\n' \
    f'Net Profit: ${profit_total}\n' \
    f'Average Change: {profit_change_average:.2f}\n' \
    f'Greatest Increase in Profits: {profit_greatest_increase["month"]} (${profit_greatest_increase["value"]})\n' \
    f'Greatest Decrease in Profits: {profit_greatest_decrease["month"]} (${profit_greatest_decrease["value"]})\n'

# Print results to console and write to file.
print(results_formatted)

with open(f'{project_root}/financial-analysis.txt', 'w') as f:
    f.write(results_formatted)
