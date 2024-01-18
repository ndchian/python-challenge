import os
import csv

pypoll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# create lists/dictionary and set initial variables
total_votes=[]
candidates=[]
candidate_names=[]
candidate_total=[]
candidate_votes=[]
vote_start = 0
vote_percent=[]
winner = ""
winner_votes = 0

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
            candidate_votes = 0
            candidate_votes = candidate_votes + 1

        # add vote to candidate total if they are not a unique value
        elif candidatename in candidates: 
            candidate_votes = candidate_votes + 1
            candidate_total.append(candidate_votes)

            #create a percentage of votes per candidate
            candidate_percent = round((((int(candidate_votes))/vote_start)*100), 3)
            vote_percent.append(candidate_percent)

        
    if candidate_votes > winner_votes:
        winner_votes = candidate_votes
        winner = candidatename
    

print("Election Results")
print("-------------------------")
print("Total Votes:  " + str(vote_start))
print("-------------------------")
for name in range(len(candidates)):
    print((candidates[name]) + ": " + str(vote_percent[name]) + "% (" + str(candidate_total[name]) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")


file = open("pollanalysis.txt", "w")
file.write("Election Results"  + "\n")
file.write("-------------------------" + "\n")
file.write("Total Votes:  " + str(vote_start) + "\n")
file.write("-------------------------" + "\n")
for name in range(len(candidates)):
    file.write((candidates[name]) + ": " + str(vote_percent[name]) + "% (" + str(candidate_total[name]) + ")" + "\n")
file.write("-------------------------" + "\n")
file.write("Winner: " + winner + "\n")
file.write("-------------------------" + "\n")
file.close