first = input("Enter first number :")
operator =input("enter your operator :(+,-,*,/,%)")
second = input("Enter the second number:")
first=int(first)
second =int(second)
if operator =="+":
    print(first + second)
elif operator =="-":
    print(first - second)
elif operator =="*":
    print(first * second)
elif operator =="/":
    print(first / second)
elif operator =="%":
    print(first % second)
else :
    print("Invalid operator !! hay bsdk !!")