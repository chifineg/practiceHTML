#!/usr/bin/python3
"""
    program to calculate compound interest
    over 10 years
"""
# get initial amount from user
amount = eval(input("enter starting amount "))
# store starting amount
startingAmount = amount
# get rate from user
rate = eval(input("enter rate "))
# convert rate to percentage
rate = rate / 100
# calculate compound interest
for i in range(1, 11):
    amount = amount + (amount * rate)
    if (i == 1):
        print("amount in {} year = {:.2f}".format(i, amount))
    else:
        print("amount in {} years = {:.2f}".format(i, amount))
#compound interest after 10 years
print("Total money compounded in 10 years = ${:.2f}".format(amount))
# return on investment
profit = amount - startingAmount
print("Profit after 10 years = ${:.2f}".format(profit))
