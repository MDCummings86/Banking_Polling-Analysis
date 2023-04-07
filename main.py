# Modules
import os
import csv

#input the file
csv_path = "Resources/budget_data.csv"

#read the file and make into a list
with open(csv_path) as interim_financials:
    reader = csv.reader(interim_financials)

    #establish indexes for month, income/loss and change
    profit_loss = []
    profit_loss_change = []
    months = []

    #Count the number of total rows, skipping the header
    rows = len(list(csv_path))
    next(reader, None)
    # print(rows) 

    #subtract the header from the total rows
    rows_minus_header = (rows-1)

    #Calculate the sum and average of the profit/loss 
    csvreader = csv.reader(interim_financials, delimiter= ',')
    for row in csvreader:

        profit_loss.append(float(row[1]))
        months.append(row[0])

        total_months = len(months)
        total_revenue = sum(profit_loss)

    #For loop to iterate through rows while iterating from one row to the next to calculate average
    for row in range(1,len(profit_loss)):
        profit_loss_change.append(profit_loss[row] - profit_loss[row-1])   
        avg_revenue_change = sum(profit_loss_change)/len(profit_loss_change)
        max_revenue_change = max(profit_loss_change)
        min_revenue_change = min(profit_loss_change)
        max_revenue_change_date = str(months[profit_loss_change.index(max(profit_loss_change))])
        min_revenue_change_date = str(months[profit_loss_change.index(min(profit_loss_change))])
        
    #Display the Finanacial Analysis, Total Months, and Total Revenue
    #line skip from https://stackoverflow.com/questions/31489377/working-of-n-in-python
    print("\n")
    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months:", total_months)
    print("Total Revenue: $", total_revenue)
    print("Average Revenue Change: $", round(avg_revenue_change))
    print("Greatest Increase in Revenue:", max_revenue_change_date,"($", max_revenue_change,")")
    print("Greatest Decrease in Revenue:", min_revenue_change_date,"($", min_revenue_change,")") 
    print("\n")

# Specify the file to write to
output_path = os.path.join("budget_data_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=' ')

# Write the header
    csvwriter.writerow(["Financial Analysis"])

    # Header Separator
    csvwriter.writerow(['----------------------------------'])
    
    # Total Months row
    csvwriter.writerow(['Total Months:',total_months])

    # Total Revenue row
    csvwriter.writerow(['Total Revenue:',total_revenue])

    #Average Revenue Change row 
    csvwriter.writerow(['Average Revenue Change:',avg_revenue_change])

    #Greatest Increase in Revenue row
    csvwriter.writerow(['Greatest Increase in Revenue:',max_revenue_change_date,max_revenue_change])

    #Greatest Decrease in Revenue row
    csvwriter.writerow(['Greatest Decrease in Revenue:', min_revenue_change_date,min_revenue_change])
 

 




    




   
    