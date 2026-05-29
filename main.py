# Calculator created by Sagar Agarwal


# First Program to get name as input and print
#name_input = input("Please enter your name :")

#print(name_input)

first_input = int(input("Please enter your first number :"))
second_input = int(input("Please enter your second number :"))
operator = input("Enter operation (+, -, *, /): ")

if operator == '+':
    sum = (first_input + second_input)
    print("Your enter values sum is:" +str(sum))
elif operator == '-':
    Substration = (first_input - second_input)
    print("Your enter values Substration is:" +str(Substration))
elif operator == '*':
    multiplication = (first_input * second_input)
    print("Your enter values multiplication is:" +str(multiplication))
elif operator == '/':
    if second_input > first_input:
       print("Please enter small value from first value")
    else: 
        devition = (first_input / second_input)
        print("Your enter values devition is:" + str(devition))
else:
    print("Enter correct opration command")
