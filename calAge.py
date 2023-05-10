age = eval(input("enter your age: "))
if age < 5:
    print("You are too young for school")
elif age == 5:
    print("Go to kindergarten")
elif age > 5 and age <= 17:
    grade = age - 5
    print("Go to {}th grade".format(grade))
elif age >= 18 and age <= 40:
    print("you should be in college")
else:
    print("You are probable too old for this!")
