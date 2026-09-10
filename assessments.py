"""
PYTHON BASICS ASSESSMENT

Topics: Dictionaries, Lists, For Loops, While Loops, Filtering
Total Questions: 20 (15 short-answer + 5 multiple choice)
"""

# ============================================================================
# SECTION A: SHORT-ANSWER QUESTIONS (15)
# ============================================================================

# ----------------------------- DICTIONARIES --------------------------------

# 1. What is a dictionary in Python, and how is it different from a list?
#
# Answer:
#
#
#

# 2. Write a dictionary called `student` with the keys `name`, `age`, and
#    `department`, and give each key a value.
#
# Answer:
#
#
#

# 3. Given the dictionary below, write the line of code that prints the
#    value of `grade`:
#
#    result = {"name": "Ada", "grade": "A", "score": 89}
#
# Answer:
#
#
#

# 4. How do you add a new key-value pair to an existing dictionary?
#    Give an example.
#
# Answer:
#
#
#

# -------------------------------- LISTS ------------------------------------

# 5. What is a list in Python? Give one example of a list containing
#    4 numbers.
#
# Answer:
#
#
#

# 6. Given fruits = ["mango", "banana", "orange", "apple"], what is the
#    output of fruits[2]?
#
# Answer:
#
#
#

# 7. Write the line of code that adds "grape" to the end of the `fruits`
#    list above.
#
# Answer:
#
#
#

# 8. What does the len() function do when used on a list? Give an example.
#
# Answer:
#
#
#

# ------------------------------- FOR LOOPS ---------------------------------

# 9. What is a `for` loop used for in Python?
#
# Answer:
#
#
#

# 10. Write a `for` loop that prints each name in the list
#     names = ["John", "Mary", "Peter"].
#
# Answer:
#
#
#

# 11. What will be the output of the code below?
#
#     for i in range(3):
#         print(i)
#
# Answer:
#
#
#

# ------------------------------ WHILE LOOPS --------------------------------

# 12. What is the difference between a `for` loop and a `while` loop?
#
# Answer:
#
#
#

# 13. Write a `while` loop that prints the numbers 1 to 5.
#
# Answer:
#
#
#

# 14. What is an infinite loop, and how can you avoid one when using a
#     `while` loop?
#
# Answer:
#
#
#

# ------------------------------ FILTERING ----------------------------------

# 15. Given the list scores = [45, 78, 62, 30, 90], write a `for` loop
#     (with an `if` statement) that prints only the scores greater than 50.
#
# Answer:
#
#
#

# ============================================================================
# SECTION B: MULTIPLE CHOICE QUESTIONS (5)
# Circle or tick the correct option.
# ============================================================================

# 16. Which of these symbols is used to create a dictionary?
#
#     (a) [ ]
#     (b) ( )
#     (c) { }
#     (d) < >
#
# Answer:

# 17. What is the index of the FIRST element in a Python list?
#
#     (a) 1
#     (b) 0
#     (c) -1
#     (d) It depends on the list
#
# Answer:

# 18. What will range(5) generate?
#
#     (a) 1, 2, 3, 4, 5
#     (b) 0, 1, 2, 3, 4, 5
#     (c) 0, 1, 2, 3, 4
#     (d) 5, 4, 3, 2, 1
#
# Answer:

# 19. Which keyword is used to immediately stop a loop?
#
#     (a) stop
#     (b) exit
#     (c) end
#     (d) break
#
# Answer:

# 20. Given nums = [10, 25, 30, 47, 50], which of the following is the
#     correct way to collect only the even numbers into a new list?
#
#     (a) [n for n in nums if n % 2 == 0]
#     (b) [n in nums if n / 2 == 0]
#     (c) [nums for n if n % 2 = 0]
#     (d) [n for nums if n % 2 == 0]
#
# Answer:

# Good luck!





# A dictionary is a collection of key-value pairs enclosed in curly braces {}.
# Each key is unique and is used to access its corresponding value.
# A list is an ordered collection of items accessed by their index (position),
# while a dictionary is accessed by its keys (not by index).
# Lists use square brackets [] and store single values;
# dictionaries use curly braces {} and store key:value pairs.

 


student = {"name": "Alice","age": 20,"department": "Computer Science"}

#3
result = {"name": "Ada", "grade": "A", "score": 89}
print(result["grade"])

# 4
# You add a new key-value pair by assigning a value to a new key using [] square brackets and the eqauls too sign =

student["year"] = 200  
print(student)

# 5.
# A list is an ordered, mutable collection of items enclosed in square
# brackets [],then the Items are separated by commas and can be accessed by index.
# Example
numbers = [10, 20, 30, 40]

# 6
# The output is "orange" because indexing starts from 0


#7
fruits = ["mango", "banana", "orange", "apple"]
fruits.append("grape")


# 8.
# The len() function returns the number of items in a list.
# Example
fruits = ["mango", "banana", "orange", "apple"]
print(len(fruits))


# 9
# A for loop is used to iterate over a sequence (such as a list, tuple,string, or range) and execute a block of code once for each item in that sequence.

# 10.
names = ["John", "Mary", "Peter"]
for i in names:
    print(i)

# 11.
# The output will be: 0 1 2 

# 12. What is the difference between a `for` loop and a `while` loop?
#
# Answer:
# A for loop is used when you know in advance how many times you want to
# iterate (e.g., over a sequence or a range).
# A while loop is used when you want to repeat a block of code as long as a certain condition remains True; the number of iterations may not be known beforehand.

# 13
num = 1
while num <= 5:
    print(num)
    num += 1

# 14.
# An infinite loop is a loop that never stops because its condition always remains True. To avoid it, make sure the condition will 
# eventually become False — for example, by updating a counter variable
# inside the loop so that the condition is eventually met.


# 15.
scores = [45, 78, 62, 30, 90]
for score in scores:
    if score > 50:
        print(score)


# 16. 
# Answer: c { }

# 17
# Answer: b 0

# 18. What will range(5) generate?

# Answer: c 0, 1, 2, 3, 4

# 19.
# Answer: d break

# 20.
# Answer: a [n for n in nums if n % 2 == 0]
