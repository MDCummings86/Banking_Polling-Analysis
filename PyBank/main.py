# Modules
import os
import csv

#input the file
csv_path = "/Users/mdcummings/Desktop/Data Analysis/python-challenge/PyBank/Resources/budget_data.csv"

#read the file and make into a list
with open(csv_path) as interim_financials:
    csvreader = csv.reader(interim_financials)

    #establish indexes for month, income/loss and change variables
    profit_loss_change = []
    revenue = []
    
    #Count the number of total rows, skipping the header
    header = next(csvreader, None)
    # print(header)
    first_row = next(csvreader)
    previous_net = int(first_row[1])
    #iterate over rows in the list
    month_count = 1

    #new variables for max and min values by month
    inc_month = first_row[0]
    dec_month = first_row[0]
   
    #From tutoring session: variable for the difference from month to month
    for row in (csvreader):
        month_count += 1
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1]) 
        profit_loss_change += [net_change]
        max_increase = max(profit_loss_change)
        min_increase = min(profit_loss_change)
        Avg_rev_change = sum((profit_loss_change))/len(profit_loss_change)
        # casting str list as an integer to prepare for next if statements
        # https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/amp/
        for x in range(0, len(profit_loss_change)):

            # If statements to identify the max and min
            if net_change > previous_net:
                inc_month = row[0]
            if net_change < previous_net:
                dec_month = row[0]     
        
#using DictReader to append rows so the sum can be taken
#https://www.youtube.com/watch?v=q503SQPMTgg
with open("/Users/mdcummings/Desktop/Data Analysis/python-challenge/PyBank/Resources/budget_data.csv", "r", newline="") as interim_financials:   
    dictreader = csv.DictReader(interim_financials)
    for row in dictreader:
        revenue.append(float(row["Profit/Losses"]))
   
#Display the Finanacial Analysis, Total Months, and Total Revenue
#line skip from https://stackoverflow.com/questions/31489377/working-of-n-in-python
# currency/demical formatting: https://stackabuse.com/format-number-as-currency-string-in-python/
print("\n")
print(f"Financial Analysis")
print("---------------------------------")
print(f"Total Months:", month_count)
print(f"Total Revenue:","${:.0f}".format(sum(revenue)))
print(f"Average Revenue Change:","$%.2f"%Avg_rev_change )
print(f"Greatest Increase in Revenue:", inc_month, "${:.0f}".format(max_increase))
print(f"Greatest Decrease in Revenue:", dec_month, "${:.0f}".format(min_increase)) 
print("\n")

# Specify the file to write to
output_path = os.path.join("/Users/mdcummings/Desktop/Data Analysis/python-challenge/PyBank/Analysis/budget_data_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=' ')

# Write the header
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(['----------------------------------']) 
    csvwriter.writerow(['Total Months:',month_count])
    csvwriter.writerow(['Total Revenue:',"${:.2f}".format(sum(revenue))])
    csvwriter.writerow(['Average Revenue Change:',"${:.0f}".format(Avg_rev_change)])
    csvwriter.writerow(['Greatest Increase in Revenue:',inc_month, "${:.0f}".format(max_increase)])
    csvwriter.writerow(['Greatest Decrease in Revenue:',dec_month, "${:.0f}".format(min_increase)])
 

 




    




   
    