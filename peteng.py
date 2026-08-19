print("Hello this is a test code we are running")

def darcy_rate(perm,area,del_p,visc,thick,cf=0.001127):
    q=(cf*perm*area*del_p)/(visc*thick)
    return round(q,2) 



answer=darcy_rate(0.3,4000,0.9,2,2000)
print(hello)
