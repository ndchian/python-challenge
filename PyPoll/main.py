import os
import csv

pypoll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# create lists/dictionary and set initial variables
total_votes=[]
candidates=[]
candidate_names=[]
candidate_votes={}
vote_start = 0
vote_percent={}

with open(pypoll_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for row in csvreader:

        # add to vote tally and establish candidate name
        vote_start = vote_start + 1
        candidatename = (row[2])
        
        # generate list of unique candidate name values
        if candidatename not in candidates:
            candidates.append(candidatename)
            candidate_votes[candidatename] = 0
            candidate_votes[candidatename] = candidate_votes[candidatename] + 1

        # add vote to candidate total if they are not a unique value
        elif candidatename in candidates: 
            candidate_votes[candidatename] = candidate_votes[candidatename] + 1



print("Election Results")
print("-------------------------")
print("Total Votes:  " + str(vote_start))
print("-------------------------")
for name in range(len(candidates)):
    print((candidates[name]) + ": " + str(vote_percent) + "% (" + str(candidate_votes[name]) + ")")