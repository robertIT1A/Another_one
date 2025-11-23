def act6():
    x = eval(input("Enter the value of x : "))
    y = eval(input("Enter the value of y : "))
    s = x + y
    d = x - y
    p = x * y
    q = x / y
    print("\nThe sum of", x, "and", y, "is" ,s)
    print("The difference of", x, "and", y, "is", d) 
    print("The product of", x, "and",y, "is",p) 
    print("The quotient of",x, "and",y, "is",q)
    print(x, "exponent by", y, "is",x**y)
    print ("The remainder of", x, "and",y, "is", x % y) 
    print ("The floor division of",x, "and", y, "is", x//y)

def act7():   
    x = 10
    print("The original value of x is", x)
    x += 5
    x -= 10
    x *= 3
    x /= 10
    print("The value of x is", x)

def act9():
    # Comparison Operators + Conditional Logic (Basics)
    username = "Junior"
    password = "Good_B0y"

    name = input("Type your username:")
    print(username == name)
    password1 = input("\nType your password:")
    print(password == password1)