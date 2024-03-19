import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('..', 'Resources', 'election_data.csv')
# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    data = [row for row in csvreader]
#otal number of votes cast
def total_votes(data):
    return len(data)
#complete list of candidates who received votes
def candidates(data):
    return set(row[2] for row in data)
#votes each candidate earned
def votes_per_candidates(data):
    vote_counts = {}
    for row in data:
        candidate = row[2]
        if candidate in vote_counts:
            vote_counts[candidate] += 1
        else:
            vote_counts[candidate] = 1
    return vote_counts
#percentage of votes each candidate won
def percentage_votes(votes, total_votes):
    return {candidate: (votes[candidate] / total_votes_count) * 100 for candidate in votes}
#winner of the election based on popular vote
def winner(data):
    return max(votes,key=votes.get)

total_votes_count = total_votes(data)
candidate_set = candidates(data)
votes = votes_per_candidates(data)
percentages = percentage_votes(votes, total_votes)
winner_candidate = winner(votes)
#print result
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes_count}")
print(f"-------------------------")
for candidate in sorted(candidate_set):
    print(f"{candidate} : {percentages[candidate]: .3f}% ({votes[candidate]})")
print(f"-------------------------")
print(f"Winnder: {winner_candidate}")
print(f"-------------------------")
#create txt file
output_file_path = "election_results.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes_count}\n")
    output_file.write("-------------------------\n")
    for candidate in candidate_set:
        output_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes[candidate]})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner_candidate}\n")
    output_file.write("-------------------------\n")
