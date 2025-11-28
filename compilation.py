from Variables_and_Printing_Output import *
from Operation import *
from Condition_Statement import *
from list import *
from for_loop import *
from while_loop import *


def countdown():
    import time
    for i in range(1,4):
        print(i)
        time.sleep(1)


        
def Variables_printing():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("_____________________________________________") 
        print("|             Prelims  Menu:                 |") 
        print("|                                            |") 
        print("|             1.Activity 1                   |") 
        print("|             2.Activity 2                   |") 
        print("|             3.Activity 3                   |") 
        print("|             4.Activity 15                  |")  
        print("|             0.Back to Main Menu            |") 
        print("|____________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            # display_zero()
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                act1()
                countdown()
            elif activity_number == 2:
                act2()
                countdown()
            elif activity_number == 3:
                act3()
                countdown()
            elif activity_number == 4:
                act15()
                countdown()

def operation():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("_____________________________________________") 
        print("|                Operation Menu              |") 
        print("|                                            |") 
        print("|             1.Assignment Operation         |") 
        print("|             2.Logical Operation            |") 
        print("|             3.Operator Precendence         |")  
        print("|             0.Back to Main Menu            |") 
        print("|____________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            # display_zero()
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                act8()
                countdown()
            elif activity_number == 2:
                act10()
                countdown()
            elif activity_number == 3:
                act11()
                countdown()


def Condition():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("_____________________________________________") 
        print("|            Condition Statement Menu        |") 
        print("|                                            |") 
        print("|             1.Activity 8                   |") 
        print("|             2.Activity 10                  |") 
        print("|             3.Activity 11                  |")  
        print("|             0.Back to Main Menu            |") 
        print("|____________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            # display_zero()
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                act8()
                countdown()
            elif activity_number == 2:
                act10()
                countdown()
            elif activity_number == 3:
                act11()
                countdown()

def forloop():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("__________________________________________") 
        print("|              For Loop Menu             |") 
        print("|                                        |") 
        print("|             1.Activity 12              |")
        print("|             2.Activity 13              |")
        print("|             3.Activity 16              |")
        print("|             4.Activity 17              |")
        print("|             5.Activity 18              |")  
        print("|             6.Activity 19              |")
        print("|             7.Activity 20              |")
        print("|             0.Back to Main Menu        |") 
        print("|________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            # display_zero()
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                act12()
                countdown()
            elif activity_number == 2:
                act13()
                countdown()
            elif activity_number == 3:
                act16()
                countdown()
            elif activity_number == 4:
                act17()
                countdown()
            elif activity_number == 5:
                act18()
                countdown()
            elif activity_number == 6:
                act19()
                countdown()
            elif activity_number == 7:
                act20()
                countdown()

def WhileLoop():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("__________________________________________") 
        print("|              For Loop Menu             |") 
        print("|                                        |") 
        print("|             1.Activity 21              |")
        print("|             2.Activity 22              |")
        print("|             0.Back to Main Menu        |") 
        print("|________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            # display_zero()
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                act21()
                countdown()
            elif activity_number == 2:
                act22()
                countdown()
            


def looping():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("__________________________________________") 
        print("|              Looping Menu              |") 
        print("|                                        |") 
        print("|             1.For Loop                 |")  
        print("|             2.While Loop               |") 
        print("|             0.Back to Main Menu        |") 
        print("|________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            # display_zero()
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                forloop()
            elif activity_number == 2:
                WhileLoop()





def List():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("__________________________________________") 
        print("|               List Menu                |") 
        print("|                                        |") 
        print("|             1.Activity 23              |")  
        print("|             0.Back to Main Menu        |") 
        print("|________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            # display_zero()
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                act23()
                countdown()




def main():
    while True:
        print(" ______________________________________________")         
        print("|                 Choose here                  |") 
        print("|______________________________________________|") 
        print("|                  Main Menu:                  |") 
        print("|                                              |") 
        print("|            1.Variables and Printing          |") 
        print("|            2.Data Types                      |") 
        print("|            3.Operation                       |") 
        print("|            4.Condition Statement             |")
        print("|            5.Looping                         |") 
        print("|            6.List                            |") 
        print("|            7.Dictionary                      |") 
        print("|            0.Exit                            |") 
        print("|______________________________________________|") 
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break
        elif choice == 1:
            Variables_printing()
        elif choice == 2:
            pass
        elif choice == 3:
            operation()
        elif choice == 4:
            Condition()
        elif choice == 5:
            looping()
        elif choice == 6:
            List()
        elif choice == 7:
            Condition()
            
        else:
            pass    

main()
