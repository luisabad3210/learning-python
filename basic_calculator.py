# BASIC CALCULATOR

# num1 = input('enter a number: ')
# num2 = input('enter another number: ')
# result = float(num1) + float(num2)
# print(result)


# BASIC CALCULATOR 2

num1 = float(input("enter 1st num"))
op = input("action")
num2 = float(input("enter 2nd num"))

def calculate(num1, op, num2):
    if (op == '+'):
        return num1 + num2
    elif (op == '-'):
        return num1 - num2
    elif (op == '/'):
        return num1 / num2
    else:
        return num1 * num2

print(calculate(num1, op, num2))