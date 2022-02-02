def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

print ("Select an Option: 1. Add \n" \
        "                  2. Substact \n" \
        "                  3. Multiply \n"
        "                  4. Divide")

select = float(input("            \n"\
    "What would u like to do?? : "))

number1 = float(input('First Number: '))
number2 = float(input('Second Number: '))

if select == 1:
    print(number1, '+', number2, '=', add(number1,number2))
elif select == 2:
    print(number1, '-', number2, '=', sub(number1,number2))
elif select == 3:
    print(number1, '*', number2, '=', mul(number1,number2))
elif select == 4:
    print(number1, '/', number2, '=', div(number1,number2))

else:
    print("Poshel Nahui")



