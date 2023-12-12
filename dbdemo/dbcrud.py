from dbfunctions import *
import os

again = True
while(again):
    print("------ Employee Management ------")
    print()
    print("[1] View Record")
    print("[2] Add Record")
    print("[3] Update Record")
    print("[4] Delete Record")
    print("[5] Clear Employees Table")
    print()
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

    if(choice==3):
        try:
            os.system('cls')
            getall()
            id = input('\n\nenter user id to update: ')
            print('--enter new values--')
            newfi = input('enter first name:')
            newla = input('enter last name:')
            newde = input('enter department:')
            newye = input('enter year hired:')
            updaterecord(id,newfi,newla,newde,newye)
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

    if(choice==4):
        try:
            os.system('cls')
            getall()
            print("\n\n===============================")
            print("--delete record option--")
            print("WARNING: DELETE OPERATION IS IRREVERSIBLE!")
            print("===============================")
            id = input("enter employee id to delete: ")
            deleterecord(id)
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

    if(choice==5):
        try:
            os.system('cls')
            print("\n\n===============================")
            print("--You are about to Clear Employees Table--")
            print("WARNING: CLEAR OPERATION IS IRREVERSIBLE!")
            print("===============================")
            confirm = input("Enter [IDO] to confirm: ")
            if(confirm=="IDO"):
                clearemployeestable()
                print("Employees Table Cleared")
            else:
                print("Muntik na")

            i = input('\npress y to try again: ')
            if(i=='y'):
                again=True
                os.system('cls')
            else:
                again=False
                print("bye")
                os.system('cls')
        except Exception as e:
            print(e)
