number1 = int(input ("enter the first number "))
number2 = int(input ("enter the second number "))
oper = input("enter a maths sign (+ addition, - subtracting * multiplication / division ** power ) ")
if oper == "+":
    print(number1 + number2)
elif oper == "-":
    print(number1 - number2)
elif oper == "*":
    print(number1 * number2)
elif oper == "/":
    print(number1 / number2)
elif oper == "**":
    print(number1 ** number2)
else:
    print("You put somthing rong pleas check or read the instruction that is below.")


