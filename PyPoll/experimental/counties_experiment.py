import os
import json
from csv import DictReader


project_root = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(project_root, "Resources", "election_data.csv")

results = {}
results_by_county = {}

with open(csv_path,'r') as file:
    reader = DictReader(file)
    for row in reader:
        candidate = row['Candidate']
        if candidate not in results:
            results[candidate] = {'votes': 0, 'percentage': 0.00}
        results[candidate]['votes'] += 1

        county = row['County']
        if county not in results_by_county:
            results_by_county[county] = {}
        if candidate not in results_by_county[county]:
            results_by_county[county][candidate] = {'votes': 0, 'percentage': 0.00}
        results_by_county[county][candidate]['votes'] += 1


total_votes = sum([results[candidate]['votes'] for candidate in results])
for candidate in results:
    results[candidate]['percentage'] = results[candidate]['votes'] / total_votes * 100
print(json.dumps(results, sort_keys=True, indent=4))

for county in results_by_county:
    county_total = sum([results_by_county[county][candidate]['votes'] for candidate in results_by_county[county]])
    for candidate in results_by_county[county]:
        results_by_county[county][candidate]['percentage'] = results_by_county[county][candidate]['votes'] / county_total * 100

print(json.dumps(results_by_county, sort_keys=True, indent=4))



        
    


