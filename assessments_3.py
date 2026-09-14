"""
PYTHON PRACTICE ASSESSMENT 3
Topics: Lists, Accessing List Items, Looping Through Lists, Dictionaries
Level: Tricky questions, basic syntax — read each question TWICE.

Context: The Digital Services Lead (DSL) wants to be sure you can REASON
about code, not just write it. Only concepts from Assessments 1 and 2 are
required — the trick is in the question itself.

Total Questions: 10
"""

# ============================================================================
# READING AND REASONING ABOUT LISTS
# ============================================================================

# Question 1
# The DSL hands you this list of daily oil rates (STB) for well TTOWG_8:
#
#     oil_prod = [4520, 4680, 4495, 4710, 4602]
#
# She asks: "Write ONE statement that displays the production of the
# third day."
# Two interns answered differently:
#     Intern A:  print(oil_prod[3])
#     Intern B:  print(oil_prod[2])
# Which intern is correct, and what would the OTHER intern's statement
# actually display?
#
# Answer:
#
#
#
#
#

# Question 2
# Without running the code, state EXACTLY what will be displayed:
#
#     perm = [120, 85, 230, 64]
#     perm[1] = perm[3]
#     print(perm)
#     print(len(perm))
#
# Answer:
#
#
#
#
#

# Question 3
# A colleague claims the two loops below will always display the same
# output for the given list. Is the colleague right? If yes, explain why;
# if no, give an example list for which the outputs differ.
#
#     rates = [5056, 4831, 5200]
#
#     # Loop 1
#     for i in range(len(rates)):
#         print(rates[i])
#
#     # Loop 2
#     for r in rates:
#         print(r)
#
# Answer:
#
#
#
#
#
#

# ============================================================================
# REASONING ABOUT LOOPS
# ============================================================================

# Question 4
# The DSL asks you to display the porosity of each core sample together
# with its sample number (1, 2, 3, ...). A colleague wrote:
#
#     poro = [0.21, 0.18, 0.25]
#     for i in range(len(poro)):
#         print(i, poro[i])
#
# The displayed sample numbers started from 0 instead of 1. The colleague
# insists the loop is correct and the list is to blame. Who is right?
# Fix the code WITHOUT changing the list or the loop structure.
#
# Answer:
#
#
#
#
#
#

# Question 5
# Study the code below carefully and state EXACTLY what it displays:
#
#     rates = [5056, 2100, 4831, 1500, 5200]
#     count = 0
#     for r in rates:
#         if r > 4000:
#             count = count + 1
#     print(r)
#     print(count)
#
# In particular: what value of r gets displayed, and why is it displayed
# at all, given that the print statement is outside the loop?
#
# Answer:
#
#
#
#
#
#

# Question 6
# Two interns were asked to compute the average of a list of thickness
# values. Both codes run without error, but ONE of them gives a wrong
# answer. Identify which one, and explain why it is wrong.
#
#     thickness = [27, 34, 22, 41]
#
#     # Intern A
#     total = 0
#     for h in thickness:
#         total = total + h
#     avg = total / len(thickness)
#     print(avg)
#
#     # Intern B
#     total = 0
#     for h in thickness:
#         total = total + h
#         avg = total / len(thickness)
#     print(avg)
#
# Answer:
#
#
#
#
#
#

# ============================================================================
# REASONING ABOUT DICTIONARIES
# ============================================================================

# Question 7
# The DSL asked an intern to create a dictionary of reservoir block
# properties. The intern produced the code below and swears it is
# a dictionary. Is it? If not, what is it, and how do you fix it?
#
#     block = "area": 50, "thickness": 27, "poro": 0.23
#
# Answer:
#
#
#
#
#

# Question 8
# Without running the code, state what is displayed and WHY:
#
#     well = {"name": "TTOWG_8", "oil_prod": 4520}
#     well["oil_prod"] = 4602
#     well["oil_prod"] = 4710
#     print(well)
#     print(len(well))
#
# In particular: how many items does the dictionary have, and why is it
# not 4?
#
# Answer:
#
#
#
#
#
#

# Question 9
# The team's STOIIP dictionary for a 3-block reservoir is:
#
#     stoiip_dict = {"Block1": 1.92e6, "Block2": 2.10e6, "Block3": 1.75e6}
#
# An intern was asked to add 500000 STB to the STOIIP of EVERY block
# (a reserve revision). The intern wrote:
#
#     for block in stoiip_dict:
#         block = stoiip_dict[block] + 500000
#
# The dictionary did not change. Explain why the loop failed to update
# any value, then re-write it correctly.
#
# Answer:
#
#
#
#
#
#
#

# Question 10
# The DSL gives you this production dataset:
#
#     field_data = [
#         {"well_name": "TTOWG_12", "well_type": "prod", "oil_prod": 5056},
#         {"well_name": "TTOWG_4",  "well_type": "inj",  "oil_prod": 0},
#         {"well_name": "TTOWG_14", "well_type": "prod", "oil_prod": 2532},
#     ]
#
# She asks you to count ONLY the injector wells. An intern wrote:
#
#     count = 0
#     for well in field_data:
#         if well["well_type"] == "prod":
#             count = count + 1
#     print(count)
#
#   i.  What number will the intern's code display, and what number
#       SHOULD be displayed?
#   ii. The intern then "fixed" the code by changing "prod" to "inj".
#       The code now displays the correct count, yet the DSL said the
#       code is still fragile. Suggest ONE thing about the dataset that
#       could silently break this fix (hint: what if a well record had
#       no "well_type" key at all?).
#
# Answer:
#
#
#
#
#
#
#
#

# End of Assessment — Good luck!
