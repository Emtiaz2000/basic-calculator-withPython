#basic calculator
number_input1=float(input("Please Enter First Number: "))#first Input
operation=input("What operation do you want: ")#operation Input
number_input2=float(input("Please Enter Second Number: "))#second Input

if operation == "+":
    print(number_input1+number_input2)#operation for plus
elif operation == "-":
    print(number_input1-number_input2)#operation for minus
elif operation=="*":
    print(number_input1*number_input2)#operation for multiplication
elif operation =="/":
    print(number_input1/number_input2)#operation for divition
else:
    print("Invalid Operation!")#if invalid operation key entered
