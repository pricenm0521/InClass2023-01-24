# main.py

# generate a random integer, print it
# decide if its even or odd
# print even or odd

import random
from Tools.scripts.summarize_stats import TOTAL
'''
alpha = random.randint(100, 200) # random integer between 100 and 200 inclusive
print("alpha=", alpha) # printing this makes it more friendly
if alpha % 2 == 0: # if integer remainder of alpha divided by 2 is 0 then it is even
    print("Even")
else:
    print("Odd")

# write the instructions that might be given based on code below
# data = input("Enter your favorite integer ")
# num = int(data)
# if (num % 2 == 0):
#    print("Your number is even")
# else:
#    print("Your number is odd")
    
# create variable data to be input "Enter your favorite number"
# convert input to an integer
# decide if it is even or odd
# print "Your number is even/odd" based on results
# prof's answer:
# Read an integer from the keyboard
# Print a friendly message telling if it is even or odd


# while loop
# divide by 2 until we get to 0

tmp = 100. # if 100. here and no int in line 36 before math it will be in float point divisions
while(True): # infinite loop, will run forever, condition will never become false
    tmp = tmp / 2
    print(tmp)
    if (tmp == 0): # if this fail safe line 39 & 40 are taken out it will run forever 
        break # takes us out of the loop immediately

# Rule: Use integers unless you have a good reason not to
# 2 reasons: faster computations, floating point numbers have a precision problem
'''

'''
# to remove all previous code do three single quotes at top and bottom

# for loop
# default start is 0

for i in range (10, 25, 2): # ints from 10 to 25 but only even numbers
    print(i)
'''

# Start an infinite loop
# Read an int from the keyboard
# if it's negative exit the loop
# else add it to the running total
# after the loop print the running total
'''
total = 0
while(True):
    alpha = int(input("Enter a number, positive or negative: "))
    if alpha < 0:
        break
    else:
        total += alpha # total = total + alpha
print("Total is ", total)
'''
'''
# count down from 100 to 1 in even integers

for i in range (100, 1, -2):
    print(i)
'''
