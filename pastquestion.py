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
     'water_prod': [6, 9, 8, 11, 6, 3723, 3906]}
]

# question i

filtered_data = []
for item in field_data:
    if item.get('well_type') == 'prod':
        filtered_data.append(item)

# iinline method

filtered_data_2=[item for item in field_data if item['well_type'] == 'prod'] 
 
 # question ii

wellnames=[]
weeklytotals=[]
weekly_summary= {'wellnames': wellnames ,'weeklytotals' : weeklytotals}

for item in filtered_data:
    wellnames.append(item['well_name'])
    weekly_total= 0
    for oil_rate in item['oil_prod']:
        weekly_total += oil_rate
        

    weeklytotals.append(weekly_total)

print(weekly_summary)

# question iii

wellnames=[]
weeklytotals=[]
weekly_summary= {'wellnames': wellnames ,'weeklytotals' : weeklytotals}

for item in filtered_data:
    wellnames.append(item['well_name'])
    weekly_total= 0
    for index,oil_rate in enumerate(item['oil_prod']):
        qo = oil_rate
        qw = item['water_prod'][index]
        fw = qw/(qo+qw)
        if fw < 0.5 :
            weekly_total += oil_rate
            
    weeklytotals.append(weekly_total)


print(weekly_summary)