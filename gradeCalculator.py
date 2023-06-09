#!/usr/bin/python3
"""
    program to calculate grade a user should be in
    based on the age entered
"""

# get age input from user
age = input("Enter student age ")
# convert input to integer
age = int(age)
# check conditions for age less than 5
if (age < 5):
    print("Too young for school")
# check conditions for age 5
elif (age == 5):
    print("Go to kindergarten")
# check conditions for age 6 through 17
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to grade {}".format(grade))
# check for conditions greater than 17
elif (age > 17) and (age <= 45):
    print("You should be in collage")
# handle invalid options
else:
    print("Too old for school")
