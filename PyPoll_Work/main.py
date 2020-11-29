import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

# Sets 'total' variable equal to 0 to start
total = 0

# Create blank list for candidates
candidates = []

# Create blank dictionary for candidates and their votes
candidate_votes = {}

# Sets 'election_winner_votes' variable as 0 to start
election_winner_votes = 0

# Beginning of code to determine HW outputs
with open(election_data_csv, newline="") as csvfile:
   
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
   
    # Code to calculate the total number of votes, set the unique list of 'candidates', 
    # and create a dictionary for each candidate and their corresponding number of votes
    for row in csvreader:
        total = total + 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate]=0
        candidate_votes[candidate] = candidate_votes[candidate] + 1

print(f"Election Results\n"
f"-------------------------\n"
f"Total Votes: {total}\n"
f"-------------------------")

# Using loop to calculate percent values for each candidate and determine the winning candidate
for candidate in candidates:
    votes = candidate_votes[candidate]
    percent = (votes/total) * 100
    if votes > election_winner_votes:
        election_winner_votes = votes
        winner = candidate
    print(f"{candidate}: {percent:.3f}% ({votes})")
print(f"-------------------------\nWinner: {winner}\n-------------------------")

# create an export to txt file for this output "with open (the path)" : 
# Text file output
# pypoll_text_file = os.path.join('Analysis', 'pypoll_output_text_file.txt')
# with open(pypoll_text_file, 'w') as textfile:
#     textwriter = textfile.write(f'-------------------------\n')
#     textwriter = textfile.write(f'Total votes {total}\n')
#     # for x in range(len(candidate_name)):
#     textwriter = textfile.write(f"{candidate_name}: {percent_candidate_won:.3f}% {votes_received}\n")
#     textwriter = textfile.write(f"-------------------------\nWinner: {election_winner}\n-------------------------\n")