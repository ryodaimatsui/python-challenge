
# Import modules for csv file path
import os
import csv

# creating a csv path 
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# defining and initializing variables
    total_votes_cast = 0
    candidates = []
    candidate_votes = [0,0,0]
    vote_percentage = [0,0,0]
    
    # for loop to find values
    for row in csvreader:
    
    # counting the total number of votes
        total_votes_cast += 1
    
    # creating a list of all unique candidates
        if row[2] not in candidates:
            candidates.append(row[2])

    # conditional statement to count votes for each candidate
        if row[2] == candidates[0]:
            candidate_votes[0] += 1
        elif row[2] == candidates[1]:
            candidate_votes[1] += 1
        else:
            candidate_votes[2] += 1
                
    # calculating the percentage of votes for each candidate
    vote_percentage[0] = round((candidate_votes[0]/total_votes_cast) * 100, 3)
    vote_percentage[1] = round((candidate_votes[1]/total_votes_cast) * 100, 3)
    vote_percentage[2] = round((candidate_votes[2]/total_votes_cast) * 100, 3)

    # finding the winner and corresponding index numbers
    winner_votes = max(candidate_votes)
    winner_index = candidate_votes.index(winner_votes)    
    winner = candidates[winner_index]

    # printing results using a formatted string
    print(f""" 
Election Results:
---------------------------
Total Votes: {total_votes_cast}
---------------------------
{candidates[0]} {vote_percentage[0]}% ({candidate_votes[0]})
{candidates[1]} {vote_percentage[1]}% ({candidate_votes[1]})
{candidates[2]} {vote_percentage[2]}% ({candidate_votes[2]})
---------------------------
Winner: {winner}
---------------------------
""")

    # Exporting results to a text file
output_folder = os.path.join(os.getcwd(), "PyPoll", "Analysis")
output_path = os.path.join(output_folder, "election_data.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write(f""" 
Election Results:
---------------------------
Total Votes: {total_votes_cast}
---------------------------
{candidates[0]} {vote_percentage[0]}% ({candidate_votes[0]})
{candidates[1]} {vote_percentage[1]}% ({candidate_votes[1]})
{candidates[2]} {vote_percentage[2]}% ({candidate_votes[2]})
---------------------------
Winner: {winner}
---------------------------
""")

    
