import os
import pandas as pd

project_root = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(project_root, "Resources", "election_data.csv")
ballots_df = pd.read_csv(csv_path)

vote_count = ballots_df['Candidate'].value_counts()
results_df = vote_count.to_frame(name = "votes")
results_df['percentage'] = results_df['votes'] / sum(results_df['votes']) * 100
winner = results_df['votes'].idxmax()

results_formatted = '=========================\n' \
    'Election Results\n' \
    '=========================\n' \
    'Total\n' \
    f'{results_df}\n\n' \
    f'Winner: {winner}\n' \
    '=========================\n' \

print(results_formatted)
with open(f'{project_root}/experimental/election-results.txt', 'w') as f:
    f.write(results_formatted)