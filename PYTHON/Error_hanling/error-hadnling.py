# print("Intializing")
# a=int(input("Enter First number\n"))
# b=int(input("Enter Second number\n"))
# try:
#     print("The value of after Divide",a/b)
# except Exception as e: #to print what error occur use exception and code without exception will run also 
    
#     print("Some error occur",e)
# print("Thank You")
try:
    x=int(input("Enter a Number"))
    y=10/x
except ValueError:
    print("Enter valid Number")
except ZeroDivisionError:
    print("Cannot divide by zero")    
finally:
    print("I Will Always Run")