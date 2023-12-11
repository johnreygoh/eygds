from dbfunctions import *
import os

again = True
while(again):
    print("------ Employee Management ------")
    print()
    print("[1] View Record")
    print("[2] Add Record")
    choice = int(input("enter your choice: "))

    if(choice==1):
        try:
            os.system('cls')
            getall()
            i = input('press y to try again: ')
            if(i=='y'):
                again=True
                os.system('cls')
            else:
                again=False
                print("bye")

        except Exception as e:
            print(e)

    if(choice==2):
        try:
            os.system('cls')
            f = input("enter first name: ")
            l = input("enter last name: ")
            d = input("enter department: ")
            y = input("enter year hired: ")
            addrecord(f,l,d,y)
            i = input('press y to try again: ')
            if(i=='y'):
                again=True
                os.system('cls')
            else:
                again=False
                print("bye")
                os.system('cls')

        except Exception as e:
            print(e)



