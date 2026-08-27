field_data = [
    {'well_name': 'ttowG_12', 
     'well_type': 'prod',
     'oil_prod': [5056, 5082, 4831, 5106, 4971, 5200, 4853],
     'water_prod': [42, 19, 35, 34, 65, 51, 48]},
    {'well_name': 'ttowG_4', 
     'well_type': 'inj',
     'water_inj': [1245, 6797, 6649, 7141, 6786, 5750, 6905],
     'water_prod': []},
    {'well_name': 'ttowG_14', 
     'well_type': 'prod',
     'oil_prod': [2532, 3031, 3288, 2780, 2774, 2574, 3723],
     'water_prod': [6, 9, 8, 11, 6, 3723, 3906]}]


filter_paper=[]


for item in field_data:    
    if item["well_type"] == "prod":
        filter_paper.append(item)

    
filter_data = [item for item in field_data if item["well_type"] == "prod"]  



filter_papers=[]

for item in field_data:
    if item["well_type"] == "inj":
        filter_papers.append(item)

print(filter_papers)