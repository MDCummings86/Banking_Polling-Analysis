import os
import csv

election_data = os.path.join('/Users/mdcummings/Desktop/Data Analysis/python-challenge/PyPoll/Resources/election_data.csv')
# print("hello")
# Open the CSV file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #count the number of rows skipping the header
    next(csvreader)
    row_list = list(csvreader)
    row_count = len(row_list)
    total_votes = row_count

    #Create a new list from column C to make a new list of all candidates who got votes
    cand_list = list()  
    count = list()
    for votes in range (0,row_count):
        candidate = row_list[votes][2]
        count.append(candidate)
        if candidate not in cand_list:
            cand_list.append(candidate)
    can_votes = len(cand_list)
          
    #Calculate the total votes for each candidate and compare that to total votes for percentage
    votes = list()
    percent = list()  
    for vote_count in range (0,can_votes):
        person = cand_list[vote_count]
        votes.append(count.count(person))
        vote_percent = votes[vote_count]/row_count
        percent.append(vote_percent)
        winner_index = votes.index(max(votes))
        winner_name = cand_list[winner_index]
        
            
# Print the results to terminal with percentage formatting 3 decimal places
# fomatting used https://stackabuse.com/format-number-as-currency-string-in-python/
print("\n")
print("Election Results")
print("----------------------------")
print(f"Total Votes:",total_votes)
print("----------------------------")
#Another for loop to iterate through the list of candidate votes and show their name, percent, and votes
for name in range (0,can_votes):
  name_perc_vote = (f"{cand_list[name]}: {percent[name]:.3%} ({votes[name]:,})")
  print(name_perc_vote)
print("----------------------------")
print("Winner:", winner_name)
      
# path for output results
output_path = os.path.join("Analysis/election_data_output.txt")

# Open the file in write mode. 
with open(output_path, 'w') as txtfile:

    # involve the csv.writer
    csvwriter = csv.writer(txtfile, delimiter=' ')

# Write the header
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['----------------------------------'])
    csvwriter.writerow(['Total Votes:',total_votes])
    csvwriter.writerow(['----------------------------------'])
    for name in range (0,can_votes):
      name_perc_vote = (f"{cand_list[name]}: {percent[name]:.3%} ({votes[name]:,})")
      csvwriter.writerow(name_perc_vote) 
    csvwriter.writerow(['----------------------------------']) 
    csvwriter.writerow([f'Winner:', winner_name])
    csvwriter.writerow(['----------------------------------'])
    


    