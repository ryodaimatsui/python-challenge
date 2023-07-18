# Importing modules to create the csvpath
import os 
import csv

# Path to CSV file within the 'Resources' file in the 'PyBank' directory
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

# Opening and reading the CSV file for analysis
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Defining and initializing variables 
    month_count = 0
    date = []
    nettotal_profit_loss = 0
    profit_loss_changes = []
    current_month_profit_loss = 0
    previous_month_profit_loss = 0
    
    # Creating a for loop to calculate values
    for row in csvreader:

        # counting the total number for months 
        month_count += 1

        # caluclating the net total profit loss for the given data
        nettotal_profit_loss += int(row[1])

        # initializing the current month's profit/loss value 
        current_month_profit_loss = int(row[1])

        # append each month and year to an empty list in order to finding the corresponding date for the greatest profit/loss
        date.append(row[0])

        # conditional statement to calculate and track changes profit/loss 
        # the first statement is to set a value for 'previous_month...' so that the we can calculate the change between row 1 and 2
        if previous_month_profit_loss == 0:
            previous_month_profit_loss = current_month_profit_loss
        else:
            monthly_change = (current_month_profit_loss) - (previous_month_profit_loss)
            profit_loss_changes.append(monthly_change)
            previous_month_profit_loss = current_month_profit_loss
    
    # Summing the total profit loss changes and divinding by the total number of months(i.e., 86)
    sum_profit_loss_change = sum(profit_loss_changes)
    avg_profit_loss_change = round(sum_profit_loss_change/(len(profit_loss_changes)), 2)
    
    # Greatest increase and decrease in profits and corresponding months
    greatest_increase_profit = max(profit_loss_changes)
    greatest_decrease_profit = min(profit_loss_changes)

    # Find the index number for the values associated with the greatest increase and decrease in profits
    greatest_increase_month = profit_loss_changes.index(greatest_increase_profit)
    greatest_decrease_month = profit_loss_changes.index(greatest_decrease_profit)

    # Using the index numbers, plug them to the date list and add 1.
    greatest_increase_date = date[greatest_increase_month + 1]
    greatest_decrease_date = date[greatest_decrease_month + 1]

    # Printing the results using a formatted string to the terminal
    print(f""" 
Financial Analysis
------------------------------
Total Months: {month_count}
Total: ${nettotal_profit_loss}
Average Change: ${avg_profit_loss_change}
Greatest Increase in Profits: {greatest_increase_date} $({greatest_increase_profit})
Greatest Decrease in Profits: {greatest_decrease_date} $({greatest_decrease_profit})
""")

# Exporting the results to a text file

output_folder = os.path.join(os.getcwd(), "PyBank", "Analysis")
output_path = os.path.join(output_folder, "budget_data.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write(f""" 
Financial Analysis
------------------------------
Total Months: {month_count}
Total: ${nettotal_profit_loss}
Average Change: ${avg_profit_loss_change}
Greatest Increase in Profits: {greatest_increase_date} $({greatest_increase_profit})
Greatest Decrease in Profits: {greatest_decrease_date} $({greatest_decrease_profit})
""")
