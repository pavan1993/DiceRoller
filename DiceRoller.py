from random import *
var="A"
while "No" not in var:
    var = input("Do you want to roll the dice?:\n ")
    if "Yes" in var or "yes" in var:
        print(randint(1,6))
    if "no" in var or "No" in var:
        exit()