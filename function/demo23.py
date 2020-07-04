from demo22 import *

basic = float(input("enter the basic salary amount: "))
gross = basic+da(basic)+hra(basic)
print("your gross salary is: ", gross)

net = gross-pf(basic)-itax(gross)
print('your net salary is: ', net)
