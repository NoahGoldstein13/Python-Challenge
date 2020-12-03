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
   
    # Split the csv on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
   
    # Calculate total number of votes 
    # Set unique list of 'candidates'
    # Create dictionary for each candidate and their corresponding number of votes
    for row in csvreader:
        total = total + 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate]=0
        candidate_votes[candidate] = candidate_votes[candidate] + 1

# Text file output
pypoll_analysis = os.path.join('Analysis', 'pypoll_analysis.txt')
with open(pypoll_analysis, 'w') as textfile:
    textfile.write(f"Election Results\n")
    textfile.write(f'-------------------------\n')
    textfile.write(f'Total Votes: {total}\n')
    textfile.write(f'-------------------------\n')

    print(f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total}\n"
    f"-------------------------")

# Using loop to calculate percent values for each candidate and determine the winning candidate
    for candidate in candidates:
        votes_received = candidate_votes[candidate]
        percent_candidate_won = (votes_received/total) * 100
        if votes_received > election_winner_votes:
            election_winner_votes = votes_received
            election_winner = candidate
        print(f"{candidate}: {percent_candidate_won:.3f}% ({votes_received})")
        textfile.write(f"{candidate}: {percent_candidate_won:.3f}% ({votes_received})\n")
    print(f"-------------------------\nWinner: {election_winner}\n-------------------------")
    textfile.write(f"-------------------------\nWinner: {election_winner}\n-------------------------\n")