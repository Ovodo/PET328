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

#4d
def pwf_updator(gwi,visc,b,pi_list,pwfc,qsp):
#i
    j=1
    pwf=pwfc+1
    pwf_tuple=()
#ii
    while pwf>pwfc:
        qsc=qsp
        pi=pi_list[j]
        j=j+1
        pwf=pi+((qsc*visc*b)/gwi)
        pwf_tuple=(pwf)
    print('end of constant regime')
    return pwf_tuple

#last exam questions
# 2bi
def fzi(p,K,rqi=None):
    pZ=p/(1-p)
    if rqi is None:
        rqi=0.34*((k/p)**0.5)
    value=rqi/pZ
    return round(value,3)


total=[]
cash=['cat',2,3]
food=['cat','can','dog']
places=['cat','church','office']
for  i in range(len(cash)):
    if cash[i] == food[i] == places[i]:
        total.append(food[i])
        

manipulated_target_depths=[]
manipulated_gr=[]
manipulated_rt=[]

# Target depths within the Reservoir Zone of Interest (RZI)
target_depths = [3189.122, 3189.275, 3189.732]

# Wireline Run 1: gamma ray depths and corresponding values
gr_depths = [3189.122, 3189.275, 3189.581, 3189.732]
gr_values = [45.2, 48.1, 50.3, 42.9]

# Wireline Run 2: true resistivity depths and corresponding values
rt_depths = [3189.122, 3189.275, 3189.428, 3189.885]
rt_values = [12.5, 14.2, 8.9, 25.1]
for i in range(len(target_depths)):
    if target_depths[i] == gr_depths[i]== rt_depths[i]:
        manipulated_target_depths.append(target_depths[i])
        manipulated_gr.append(gr_values[i])
        manipulated_rt.append(rt_values[i])








target_depths = [3189.122, 3189.275, 3189.732]
gr_depths = [3189.122, 3189.275, 3189.581, 3189.732]
gr_values = [45.2, 48.1, 50.3, 42.9]
rt_depths = [3189.122, 3189.275, 3189.428, 3189.885]
rt_values = [12.5, 14.2, 8.9, 25.1]

manipulated_target_depths = []
manipulated_gr = []
manipulated_rt = []


for depth in target_depths:
    if depth in gr_depths and depth in rt_depths:
        gr_index = gr_depths.index(depth)
        rt_index = rt_depths.index(depth)
        
        
        manipulated_target_depths.append(depth)
        manipulated_gr.append(gr_values[gr_index])
        manipulated_rt.append(rt_values[rt_index])


#
block_data=dict(area='50 acres',thickness='27 ft',porosity='0.27',watersaturation='0.28',oilformationvolumefactor='1.19rb/stb')

block_data['porosity']='0.20'
block_data['watersaturation']='0.3'
block_data['oilformationvolumefactor']='1.16'


x=[4,5,6,7,8]

    


components = ["Methane", "Ethane", "Propane", "n-Butane"] 
x=[0.35,0.20,0.20,0.20]
y=[0.70,0.18,0.08,0.04]
k=[]
for i in range(len(components)):
    k.append(x[i]/y[i])

    print(k[i],components[i])
print('complete list of k value',k)