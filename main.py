import os
import csv

election_data = os.path.join('Resources/election_data.csv')
# print("hello")
# Open the CSV file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  # The total number of votes cast (skip header), assign to list
    next(csvreader)
    rows = list(csvreader)
    total_votes = len(rows)
    total_votes = total_votes

  # Create new list from Candidate colum to count votes for each candidate iterating through all the rows
  # used python range function 'LoopDeLoop.py'
    candidate_names = list()
    amount = list()
    for active_rows in range (0,total_votes):
        if active_rows == "Charles Casper Stockham":
            print(active_rows)
        candidate = rows[active_rows][2]
        amount.append(candidate)
        # if statement to determine how many candidates (assistance from TA)
        if candidate not in candidate_names:
            candidate_names.append(candidate)
    number_of_candidates = len(candidate_names)
    # print(number_of_candidates)
    # print(candidate_names)

  # Append the lists to count and calculate total votes and percentage
    votes = list()
    percentage = list()
    for columns in range (0,number_of_candidates):
        name = candidate_names[columns]
        votes.append(amount.count(name))
        decimal = votes[columns]/total_votes
        percentage.append(decimal)
        # print(decimal)
        # print(columns)

  # variable for the winner '1'
    winner = votes.index(max(votes))
    # print(winner)

  # Print the results to terminal with percentage formatting 3 decimal places
    print("\n")
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
    for z in range (0,number_of_candidates):
        print(f"{candidate_names[z]}: {percentage[z]:} ({votes[z]:,})")
    print("----------------------------")
    print(f"Winner: {candidate_names[winner]}")
    print("----------------------------")
    print("\n")

# Write the results to "election_data_output.txt" file
# Specify the file to write to
output_path = os.path.join("Analysis/election_data_output.txt")

# Open the file using "write" mode. 
with open(output_path, 'w') as txtfile:

    # involve the csv.writer
    csvwriter = csv.writer(txtfile, delimiter=' ')

# Write the header
    csvwriter.writerow(['Election Results'])

    # Header Separator
    csvwriter.writerow(['----------------------------------'])
    
    # Total Votes row
    csvwriter.writerow(['Total Votes:',total_votes])

    # Separator
    csvwriter.writerow(['----------------------------------'])

    #Votes for Candidate
    for z in range (0,number_of_candidates):
        csvwriter.writerow(f"{candidate_names[z]}: {percentage[z]:.3%} ({votes[z]:,})")
    
    # Separator
    csvwriter.writerow(['----------------------------------']) 

     # Winner
    csvwriter.writerow([f"Winner: {candidate_names[winner]}"])

    # Separator
    csvwriter.writerow(['----------------------------------'])
    


    