# Lesson plan

Link to powerpoint: https://docs.google.com/presentation/d/1gwlXVUoaeeuATIVsEAscUS8dPOzZ0oTh/edit#slide=id.p1

#AND OR AND NOT

Uses literal words - and, or, not

boolean table showing and, or, not

examples:

two booleans being combined

two boolean expressions being combined (comparisons)

multiple ands, nots, ors.

Order of ands, nots, ors (order of operation)
(not, and then or)

Example:

'''
 Lesson 1.8 - Boolean Expressions
 Author: Mr. Kalisz
 Date Created: September 23, 2021
 Date Last Modified: February 17, 2022
'''

#Review

varA = True #all booleans must start with capital letters

#Comparisons

# < (open side is larger), >, <=, >=, ==(equals to), !=(not equals to)

#and, or, not

#These can be placed between booleans

varA = True
varB = False

# and - both sides must be true to resolve to true

#print(varA and varB)

print(5 < 7 and 3 > 2)
#print (True and True)

num = 5
num2 = 7
print(num < num2 and num2 > num)
#print(5 < 7 and 7 > 5)
#print(True and True)

# or - If either side is true, resolve to true

print(True or False) #True
print(5 < 1 or 3 > 2) #True

#not - goes in front of a boolean, and swaps its value

print(not True)
print(not False)

print(not 5 < 3)

#Combine these

result = False and False or True
#result = False or True
#result = True

result = True or False and False
#result = True or False
#result = True

result = not True and False or not True and False
#result = False and False or False and False
#result = False

result = True or not False and not True and False or not True and False or True
#result = True or True and False and False or False and False or True
#result = True or False and False or False and False or True
#result = True or False or False and False or True
#result = True or False or False or True
#result = True or False or True
#result = True or True
#result = True

result = (True or False) and False
#result = False

result = not(not(not(not(True))))
#result = True
print(result)

#Bad Example of combining booleans

num = 7

#THIS DOES NOT WORK, must have booleans on either side of and
#print(num > 5 and < 8)


print(num > 5 and num < 8) #You need booleans on either side of the AND/OR

word = "computer"

#Sometimes it doesn't crash but gives unpredictable behaviour
result = word == "wallet" or "computer"
#result = False or "computer"
print(result)

#Correct Way
result = word == "wallet" or word == "computer"