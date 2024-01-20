import os
import csv

pypoll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# create lists/dictionary and set initial variables
total_votes=[]
candidates=[]
candidate_votes=[]
candidate_percentage=[]
total_votes = 0
vote_percent=[]
winner_votes = 0

with open(pypoll_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for row in csvreader:

        # add to vote tally and establish candidate name
        total_votes += 1
        candidatename = (row[2])
        
        # generate list of unique candidate name values
        if candidatename not in candidates:
            candidates.append(candidatename)
            candidate_votes.append(1)

        # add vote to candidate total if they are not a unique value
        else:
            name = candidates.index(candidatename)
            candidate_votes[name] += 1

# determine percentage of votes per candidate
for x in range(len(candidate_votes)):
    candidate_percentage.append(candidate_votes[x] / total_votes)
    # converting help from stackoverflow https://stackoverflow.com/questions/61611110/how-do-i-convert-a-list-of-floats-into-a-list-of-percentages
    converted = [f'{x*100:.3f}%' for x in candidate_percentage]
    
    if candidate_votes[x] > winner_votes:
        winner_votes = candidate_votes[x]
        winner = candidates[x]

print("Election Results")
print("-------------------------")
print("Total Votes:  " + str(total_votes))
print("-------------------------")
for name in range(len(candidates)):
    print((candidates[name]) + ": " + str.format(converted[name]) + " (" + str(candidate_votes[name]) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")


file = open("pollanalysis.txt", "w")
file.write("Election Results"  + "\n")
file.write("-------------------------" + "\n")
file.write("Total Votes:  " + str(total_votes) + "\n")
file.write("-------------------------" + "\n")
for name in range(len(candidates)):
    file.write((candidates[name]) + ": " + str.format(converted[name]) + " (" + str(candidate_votes[name]) + ")" + "\n")
file.write("-------------------------" + "\n")
file.write("Winner: " + winner + "\n")
file.write("-------------------------" + "\n")
file.close