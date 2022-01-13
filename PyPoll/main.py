import os
from csv import DictReader

# Get path to csv file
project_root = os.path.dirname(__file__)
csv_path = os.path.join(project_root, 'Resources', 'election_data.csv')

results = {}

# Read file and store vote counts in dictionary
with open(csv_path,'r') as file:
    reader = DictReader(file)
    for row in reader:
        candidate = row['Candidate']
        if candidate not in results:
            results[candidate] = {'votes': 0, 'percentage': 0.00}
        results[candidate]['votes'] += 1

# Calculate statistics
total_votes = sum([results[candidate]['votes'] for candidate in results])
most_votes = 0
winner = ''
for candidate in results:
    vote_count = results[candidate]['votes']
    if vote_count > most_votes:
        most_votes = vote_count
        winner = candidate
    results[candidate]['percentage'] = results[candidate]['votes'] / total_votes

# Format election results
results_formatted = 'Election Results\n'
results_formatted += '-------------------------\n'
results_formatted += f'Total Votes: {total_votes}\n'
results_formatted += '-------------------------\n'
for candidate in results:
    results_formatted += f'{candidate}: {results[candidate]["percentage"]:.2%} ({results[candidate]["votes"]})\n'
results_formatted += '-------------------------\n'
results_formatted += f'Winner: {winner}\n'
results_formatted += '-------------------------\n'

# Print results to console and write to file
print(results_formatted)

with open(f'{project_root}/election-results.txt', 'w') as f:
    f.write(results_formatted)

