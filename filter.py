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


# i
filter_paper=[]

for item in field_data:    
    if item["well_type"] == "prod":
        filter_paper.append(item)
    

# filter_data = [item for item in field_data if item["well_type"] == "prod"]  
filter_data = [ item for item in field_data if item["well_type"] == "prod"]




# ii
well_names =[]
weekly_totals= []
weekly_summary = {"well_names":well_names, "weekly_totals":weekly_totals}

for well in filter_data:
    well_names.append(well["well_name"])
    total_prod = 0
    for index,item in enumerate(well['oil_prod']):
        qo = item
        qw = well['water_prod'][index]
    # if water cut is below 0.5, then add to weekly total
        total_prod = total_prod + item
    weekly_totals.append(total_prod)    

# print(weekly_summary)




list_of_names = ["Peter", "John", "James","Mary", "Alice", "Bob"]

filter_list = [x for x in list_of_names if x.startswith("J")]



itemz = [1,2,3,4,5]


total = 0
for item,index in enumerate(itemz):
    total = total + item
    # total += item

print(itemz[4])