# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the path file
# csvpath = Path("/Users/areshbwint/Desktop/CU-NYC-FIN-PT-08-2019-U-C/02-Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv")
Path.cwd()
csvpath = Path("/Users/areshbwint/Desktop/CU-NYC-FIN-PT-08-2019-U-C/02-Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv")

# Initialize variable to hold profit/losses and dates
date = []
total_profit_losses = []


# Average of changes in Profit/Losses over entire period
# Total months included in a data set
with open(csvpath, mode= 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Total months included in a data set
    next(csvreader)
    month_count = 0
   
    total_profit_loss =[]
    dates = []
    for line in csvreader:
        month_count+=1
    
#The average of the changes in Profit/Losses over the entire period.

revenue_change = []

for x in range(1, len(total_profit_loss)):
        revenue_change.append(total_profit_loss[x] - total_profit_loss[x-1])

revenue_average = round((sum(revenue_change) / len(revenue_change)),2)
#The greatest increase in profits (date and amount) over the entire period.
max_revenue_change = max(revenue_change)

#The greatest decrease in losses (date and amount) over the entire period.
    
    min_revenue_change = min(revenue_change)
    
    print('Financial Analysis')
    print()
    print("----------------------------------------")
    print()
    print(f'Total: $ {total}')
    print(f'Total Months:{mounth_count}')
    print(f'Average Change: $ {revenue_average}')
    print(f'Greatest Increase in Profits:{dates[revenue_change.index(max(revenue_change))+1]} (${max_revenue_change})')
    print(f'Greatest Decrease in Profits:{dates[revenue_change.index(min(revenue_change))+1]} (${min_revenue_change})')
    
with open('final_results.txt','w') as file:
    file.write('Financial Analysis' '\n')
    file.write('\n')
    file.write('----------------------------------------''\n')
    file.write('\n')
    file.write(f'Total Months:{mounth_count}''\n')
    file.write(f'Total: ${total}''\n')
    file.write(f'Average Change: ${revenue_average}''\n')
    file.write(f'Greatest Increase in Profits:{dates[revenue_change.index(max(revenue_change))+1]} (${max_revenue_change})''\n')
    file.write(f'Greatest Decrease in Profits:{dates[revenue_change.index(min(revenue_change))+1]} (${min_revenue_change})''\n')







