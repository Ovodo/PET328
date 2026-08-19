def volumetrics(area, thickness, porosity):
    BV = area * thickness
    PV = BV * porosity
    return (BV, PV)


def addition(a,b):
    print("This is the addition function of a and b")
    tuple =("this is 1",45,b)
    return a +b



answer = addition(4,4)

print("The answer is ", answer)