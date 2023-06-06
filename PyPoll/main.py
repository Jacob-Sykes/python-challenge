import os

import csv

# Path to collect data from Resources folder
election_data = os.path.join('Resources','election_data.csv')

with open(election_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        csv_header = next(csvreader)
        
        candidate_list = [candidate[2] for candidate in csvreader]

votes = len(candidate_list)   
cand_name = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]
cand_name = sorted(cand_name, key=lambda x: x[1], reverse=True)

# Print out results for total votes
print("Election Results")

print("------------------")

print("Total Votes: ", str(votes))

print("------------------")

# Run loop to determine percent of votes
for candidate in cand_name:
    percent_votes = (candidate[1] / votes) * 100
    
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')
    
print("------------------")

print(f"Winner: {cand_name[0][0]}")

print("------------------")

# Write prints into a output text file

output_file = open('election_results.txt', 'w')

output_file.write("Election Results\n")

output_file.write("------------------\n")

output_file.write("Total Votes: {}\n".format(str(votes)))

output_file.write("------------------\n")

output_file.write("{}: {:6.3f}% ({})\n".format(candidate[0], percent_votes, candidate[1]))

output_file.write("------------------\n")

output_file.write("Winner: {}\n".format(cand_name[0][0]))

output_file.write("------------------\n")

# Close the output file
output_file.close()
