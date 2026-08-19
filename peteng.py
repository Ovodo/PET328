print("Hello this is a test code we are running")

def darcy_rate(perm,area,del_p,visc,thick,cf=0.001127):
    q=(cf*perm*area*del_p)/(visc*thick)
    return round(q,5) 



answer=darcy_rate(1,50000,0.9,2,1)
hello =500


print(f"The answer is {answer}")
