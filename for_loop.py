#Print a word as many as you want
def act12():
    for i in range(1,100+1,1):
        print(i, "I Love You")

#ask the user to input a number using loop
#contatenate all the input numbers
def act13():
    con = []

    for i in range (1, 16):
        x = int(input("Enter Whole Number: "))
        con.append (x) #append para pumunta sa []
        print(con)

def act16():
    for i in range(1,11,1):
        print(i, end=" ") 

# using loop print 1 to 10 horizontal 
# print 1 to 10 per each row
def act17():
    for sun in range(1,11,1): #This will serve as a outer loop 
        for earth in range(1,11,1): #This will serve as a inner loop 
            # Each time the outer loop runs, the inner loop runs from 1 to 10 
            print(earth, end=" ")  # print earth, followed by end=" " to prevent new line
        print()# print new line every inner loop
        
def act18():
    num = 10 
    for outer in range(1,5,1): 
        for inner in range(outer + 1, 6):
            print(num, end=" ")
            num -= 1 
        print()

    #right triangle
    for outer in range(1,11,1):  #This outer loop responsible for creating 1 to 10 in row
        for inner in range(1, outer): #This inner loop responsible for print number on each row or create horizontal 
            print(inner, end=" ")
        print() #Move to the next line

    #reverse triangle
    for outer in range(1,11,1): 
        for inner in range(outer, 10):
            print(inner, end=" ")
        print()
    


    num = 1 # starting number
    for outer in range(1,5,1): #This will create 4 row
        for inner in range(1, outer + 1): # this will create horizontal
            print(num, end=" ")
            num += 1 # every time that it will print, it will add 1
        print()

# create a right triangle using (*)
def act19():
    for outer in range(1,11,1): 
        for inner in range(1, outer,1): # print triangle using (*)
            print("*", end=" ") 
        print() # to make new line after each row

#combined two loop in one loop
def act20():
    for outer in range(1,11,1):
        for star in range(1,outer,1): # print triangle using (*)
            print("*", end=" ") 
        for diamond in range(outer,10,1): # print reverse triangle in the same loop
            print("♦", end=" ") 

        print() # to make new line after each row
