def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def even_odd(n):
    if n%2==0:
        return str(n)+" is Even"
    else:
        return str(n)+" is Odd"
def percentage(a,b):
    return (a/b)*100
while True:
    # Input from user keeps asking until user chooses to exit
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even or Odd")
    print("6. Calculate Percentage") 
    print("7. Exit")
    c=input("Enter your choice (1-7):")
    if c=='7':
        print("Exit")
        break
    # Executes the corresponding function based on user's choice 
    if c=='1':
        print("Sum:",addition(a,b))
    elif c=='2':
        print("Difference:",subtraction(a,b))
    elif c=='3':
        print("Product:",multiplication(a,b))
    elif c=='4':
        print("Quotient:",division(a,b))
    elif c=='5':
        print(even_odd(int(a)))
        print(even_odd(int(b)))
    elif c=='6':
        print("Percentage:",percentage(a,b),"%")
    else:
        print("Invalid Entry")
