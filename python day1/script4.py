# functions
# required parameters, default parameters
# overriding values

print("=====Registration======")
print()
fn = input("Enter first name: ")
ln = input("Enter last name: ")
age = input("Enter age now: ")

# expected output:
# Good day Juan Santos (48)!
def showgreet(firstname="Andrea",lastname="Brillante",myage=20):
    print(f'Good day {firstname} {lastname} ({myage})!')

showgreet(fn,ln,age)
showgreet('daniel','padilla') # missing myage parameter, uses default value
showgreet(lastname='Padilla')

