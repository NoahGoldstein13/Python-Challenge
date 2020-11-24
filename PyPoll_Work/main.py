import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

total = 0

# create blank list for candidates
candidates = []

# create blank dictionary for candidates and their votes
candidate_votes = {}

# Using function to calculate percentage votes
# def percent_votes(votes):
#     percent = round((votes/total) * 100,2)
#     return percent

election_winner = 0

with open(election_data_csv, newline="") as csvfile:
   
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
   
    for row in csvreader:
        total = total + 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate]=0
        candidate_votes[candidate] = candidate_votes[candidate] + 1

# create an export to txt file for this output "with open (the path)" : https://www.geeksforgeeks.org/writing-csv-files-in-python/


print(f"Election Results\n"
f"-------------------------\n"
f"Total Votes: {total}\n"
f"-------------------------")

# Using loop to calculate values
for candidate in candidates:
    votes = candidate_votes[candidate]
    percent = (votes/total) * 100
    if votes > election_winner:
        election_winner = votes
        winner = candidate
    print(f"{candidate}: {percent:.3f}% ({votes})")
print(f"-------------------------\nWinner: {winner}\n-------------------------")


# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

    # print(percent_votes(votes)) ...referring to function defined above

# print(candidates, candidate_votes)
# print(percent_votes(candidate_votes["Khan"]))
# print (f'Total votes cast were {total}')