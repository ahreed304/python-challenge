import os
from csv import DictReader

project_root = os.path.dirname(__file__)
csv_path = os.path.join(project_root, "Resources", "election_data.csv")

results = {}

with open(csv_path,'r') as file:
    reader = DictReader(file)
    for row in reader:
        candidate = row['Candidate']
        if candidate not in results:
            results[candidate] = {'votes': 0, 'percentage': 0.00, 'by_county': {}}
        results[candidate]['votes'] += 1

        county = row['County']
        if county not in results[candidate]['by_county']:
            results[candidate]['by_county'][county] = {'votes': 0, 'percentage': 0.00}
        results[candidate]['by_county'][county]['votes'] += 1

total_votes = sum([results[candidate]['votes'] for candidate in results])
for candidate in results:
    results[candidate]['percentage'] = results[candidate]['votes'] / total_votes * 100

print(results)




        
    


