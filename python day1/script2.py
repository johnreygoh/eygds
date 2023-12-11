# functions
# operations / tasks
import functions1

# net pay
rateperhour = int(input('enter rate per hour: '))
hours = int(input('enter number of hours: '))
deductions = int(input('enter total deductions: '))

# str(), int(), float()

# create a function for netpay
# netpay = (rateperhour * hours) - deductions
# print(netpay) 

# use our functions
functions1.greetme()
ans = functions1.getnetpay(rateperhour,hours,deductions)
print(f'netpay is {ans}')

overall = functions1.overalltotal()
print(f'overall: {overall}')
# sample usages
# getnetpay(2000,2,100)
# getnetpay(4000,3,200)
# getnetpay(5000,4,100)






















