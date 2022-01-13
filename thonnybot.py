print("Hello, i am Thonny, your personal bot")
# ask the user to enter their name
user_name = input("enter your name ")
print("welcome "+ user_name)
def do_calculation():
    print("lets " + command + " some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    if command == "add":
        result = number1 + number2
        operator = "+"
    elif command == "subtract":
        result = number1 - number2
        operator = "-"
    elif command == "divide":
        result = number1 / number2
        result = round(result, 2)
        operator = "/"
    output = str(result)
    print(input1 + operator + input2 + " = " + output)
def do_totalaverage():
    how_many = input("how many numbers?> ")
    how_many = int(how_many)
    total=0
    for number_count in range(how_many):
        number = input("Number" + str(number_count) + "> ")
        total = total + int(number)
    if command == "total":
        result = total
    elif command == "average":
        result = total/how_many
        result =round(result,2)
    print("The " + command + " of these numbers are: ", str(result))   
finished = False 
while finished == False:
    command = input("How can i help you? ")
    if command == "add":
        do_calculation()
    elif command == "subtract":
        do_calculation()
    elif command == "divide":
        do_calculation()
    elif command == "total":
        do_totalaverage()
    elif command == "average":
        do_totalaverage()
    elif command == "shopping":
        print("there are ten item in our shop, choose from a, b, c, d, e, f, g, h, i, j:")
        shopping = []
        how_many = input("how many item you wanna purchase> ")
        how_many = int(how_many)
        total = 0
        for item_count in range(how_many):
            item = input("your item " + str(item_count) + "> " )
            if item == "a":
                item_value = 10
            elif item == "b":
                item_value = 30
            elif item == "c":
                item_value = 50
            elif item == "d":
                item_value = 25
            elif item == "e":
                item_value= 45
            elif item == "f":
                item_value = 77
            elif item == "g":
                item_value = 56
            elif item == "h":
                item_value = 92
            elif item == "i":
                item_value = 34
            elif item == "j":
                item_value = 199
            else:
                print("this item is not there in our shop")
            item_unit = input("how many unit of this item> ")
            item_unit = int(item_unit)
            total = total + int(item_value*item_unit)
        print("Dear customer your total bill is Rs. " + str(total))
        print(" Thank You for visiting us, Have a nice day.")
    elif command == "bye":
        finished = True
    else:
        print("i don't understand")