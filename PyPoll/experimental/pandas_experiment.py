import os
import pandas as pd

project_root = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(project_root, "Resources", "election_data.csv")
ballots_df = pd.read_csv(csv_path)

vote_count = ballots_df['Candidate'].value_counts()
results_df = vote_count.to_frame(name = "votes")

results_df['percentage'] = results_df['votes'] / sum(results_df['votes']) * 100
print(results_df)