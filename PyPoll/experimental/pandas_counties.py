import os
import pandas as pd

project_root = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(project_root, 'Resources', 'election_data.csv')
ballots_df = pd.read_csv(csv_path)

vote_count = ballots_df['Candidate'].value_counts()
results_df = vote_count.to_frame(name = 'votes')
results_df['percentage'] = results_df['votes'] / sum(results_df['votes']) * 100
winner = results_df['votes'].idxmax()

results_by_county = {}
for county in ballots_df['County'].unique():
    ballots_county_df = ballots_df[ballots_df['County'] == county]
    vote_count_county = ballots_county_df['Candidate'].value_counts()
    results_county_df = vote_count_county.to_frame(name = 'votes')
    results_county_df['percentage'] = results_county_df['votes'] / sum(results_county_df['votes']) * 100
    results_by_county[county] = results_county_df


formatted_results_county = ''
for county in results_by_county:
    formatted_results_county += f'{county} County\n' \
        f'{results_by_county[county]}\n\n' \
        f'Winner: {results_df["votes"].idxmax()}\n' \
        '-------------------------\n' \

results_formatted = '=========================\n' \
    'Election Results\n' \
    '=========================\n' \
    'Total\n' \
    f'{results_df}\n\n' \
    f'Winner: {winner}\n' \
    '=========================\n' \
    'Results by County\n' \
    '-------------------------\n' \
    f'{formatted_results_county}' 

print(results_formatted)
with open(f'{project_root}/experimental/election-results-by-county.txt', 'w') as f:
    f.write(results_formatted)