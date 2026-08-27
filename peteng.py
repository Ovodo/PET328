print("Hello this is a test code we are running")

def darcy_rate(perm,area,del_p,visc,thick,cf=0.001127):
    q=(cf*perm*area*del_p)/(visc*thick)
    return round(q,5) 



answer=darcy_rate(0.3,4000,0.9,2,2000)

def reservior(flowrate,pressure,area):
    res=flowrate*pressure*area
    return round(res,2)

result=reservior(100,200,300)
print (result) 


