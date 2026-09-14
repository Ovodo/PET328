"""
PYTHON PRACTICE ASSESSMENT 2
Topics: Lists, Accessing List Items, Looping Through Lists, Dictionaries

Context: You have just joined the TTOWG oilfield digitalization team as an
intern. Your training mentor, the Digital Services Lead (DSL), has given you
the following tasks to confirm your understanding of Python basics.

Total Questions: 10
"""

# ============================================================================
# LISTS AND ACCESSING ITEMS
# ============================================================================

# Question 1
# The DSL gives you a list of daily oil production rates (in STB) for
# well TTOWG_8 over five days:
#
#     oil_prod = [4520, 4680, 4495, 4710, 4602]
#
# Write Python statements to:
#   i.   display the production rate for the FIRST day
#   ii.  display the production rate for the LAST day (use a negative index)
#   iii. display how many days of records the list contains
#
# Answer:
#oil_prod = [4520, 4680, 4495, 4710, 4602]

# i. First day's production rate
print(oil_prod[0])      

# ii. Last day's production rate (negative index)
print(oil_prod[-1])     

# iii. Number of days of record
print(len(oil_prod))    



# Question 2
# During data entry, the Day 3 production rate of well TTOWG_8 was wrongly
# recorded as 4495 STB. The correct value is 4549 STB.
# Using the list in Question 1, write a Python statement that corrects the
# Day 3 value WITHOUT creating a new list, then write another statement to
# add a new record of 4660 STB for Day 6 to the list.
#
# Answer:
#oil_prod = [4520, 4680, 4495, 4710, 4602]

# Correct the Day 3 value (index 2) without creating a new list
oil_prod[2] = 4549
oil_prod.append(4660)
print(oil_prod)         
#
#

# Question 3
# The team stores the permeability (in mD) of four reservoir zones thus:
#
#     perm = [120, 85, 230, 64]
#
# A colleague wrote the statement below to display the permeability of
# Zone 4, but it failed:
#
#     print(perm[4])
#
# Explain WHY the statement failed, then write the correct statement.
#
print(perm[3])     
#or
print(perm[-1]) 
#
# ============================================================================
# LOOPING THROUGH LISTS
# =========
# Question 4
# Write a for loop that iterates through the list below and displays each
# well name on its own line:
#
#     wells = ["TTOWG_4", "TTOWG_8", "TTOWG_12", "TTOWG_14"]


for well in wells:
    print(well)
#

# Question 5
# Given the porosity values of core samples from a reservoir:
#
#     porosity = [0.21, 0.18, 0.25, 0.23, 0.19]
#
# Write a for loop that computes the TOTAL of all the porosity values
# (hint: initialize a variable total = 0 before the loop), then display
# the average porosity after the loop.
#
# Answer:
#porosity = [0.21, 0.18, 0.25, 0.23, 0.19]

total = 0
for p in porosity:
    total = total + p

average = total / len(porosity)
print("Average porosity:", average)


# Question 6
# The DSL wants only the active producers from a mixed list of daily
# production rates (STB). Write a for loop (with an if statement) that
# iterates through the list below and displays only the rates that are
# greater than 4000 STB:
#
#     rates = [5056, 2100, 4831, 1500, 5200, 900]
#
# Answer:
#rates = [5056, 2100, 4831, 1500, 5200, 900]

for rate in rates:
    if rate > 4000:
        print(rate)

# ============================================================================
# DICTIONARIES
# ============================================================================

# Question 7
# Create a dictionary named well_data to hold the following properties of
# a reservoir block:
#
#     Property                    Value
#     area                        50 (acres)
#     thickness                   27 (ft)
#     porosity                    0.23
#     water_saturation            0.28
#
# Then write a statement that displays the value of thickness.
#
# Answer:
well_data = {"area": 50,"thickness": 27,"porosity": 0.23,"water_saturation": 0.28}

print(well_data["thickness"])   


# Question 8
# After re-evaluation, some properties of the reservoir block in Question 7
# changed. Write Python statements that modify the EXISTING well_data
# dictionary (do NOT create another dictionary) such that:
#   i.   porosity becomes 0.25
#   ii.  water_saturation becomes 0.22
# Also write a statement that adds a NEW key, oil_fvf, with value 1.19.
#
# Answer: 
well_data["porosity"] = 0.25
well_data["water_saturation"] = 0.22
well_data["oil_fvf"] = 1.19

print(well_data)

# Question 9
# A function in the team's peteng module returns the STOIIP of discretized
# reservoir blocks as a dictionary:
#
#     stoiip_dict = {"Block1": 1.92e6, "Block2": 2.10e6, "Block3": 1.75e6}
#
# It was discovered that the value of Block2 was entered incorrectly; the
# correct value is 2.45e6 STB. Write Python statements to:
#   i.   retrieve and display the currently stored value of Block2
#   ii.  replace the incorrect value with the correct one
#   iii. compute and display the TOTAL STOIIP of all blocks using the
#        corrected dictionary (hint: loop through the dictionary values,
#        or use sum() with .values())
#
# Answer:
#stoiip_dict = {"Block1": 1.92e6, "Block2": 2.10e6, "Block3": 1.75e6}


print(stoiip_dict["Block2"])

stoiip_dict["Block2"] = 2.45e6

total_stoiip = sum(stoiip_dict.values())
print("Total STOIIP:", total_stoiip)


totalvalues = 0
for values in stoiip_dict.values():
   totalvalues=totalvalues+ values                    




# Question 10
# The team structures raw daily production data as a list of dictionaries:
#
#     field_data = [
#         {"well_name": "TTOWG_12", "well_type": "prod", "oil_prod": 5056},
#         {"well_name": "TTOWG_4",  "well_type": "inj",  "oil_prod": 0},
#         {"well_name": "TTOWG_14", "well_type": "prod", "oil_prod": 2532},
#     ]
#
# Write a for loop that iterates through field_data and displays the
# well name and oil production of ONLY the wells whose well_type is
# "prod".
#
# Answer:
field_data = [
    {"well_name": "TTOWG_12", "well_type": "prod", "oil_prod": 5056},
    {"well_name": "TTOWG_4",  "well_type": "inj",  "oil_prod": 0},
    {"well_name": "TTOWG_14", "well_type": "prod", "oil_prod": 2532},
]

for well in field_data:
    if well["well_type"] == "prod":
        print(well["well_name"], well["oil_prod"])

