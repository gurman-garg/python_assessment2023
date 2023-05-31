#Version 1: Basic Cafe Click & Collect

#set prices to menu items
item1 = 1.50
item2 = 3.50
item3 = 4.50
item4 = 2.50
item5 = 5.00

#empty list for user order and list of student names who already have accounts
order = []
students = ["someone", "person"]

#introduction to program for user and list of menu items for user to order as well as an exit option that stops ordering
print("Welcome to the BDSC Cafe Click & Collect!")
print("Menu: \n1: Hash Brown: ${} \n2: Cookie: ${} \n3: Nachos: ${} \n4: Garlic Bread: ${} \n5: Burger: ${} \n6: Exit - Stop Ordering".format(item1, item2, item3, item4, item5))

#declare price as global so it can be used outside of specific functions
global price
price = 0

#age function that asks user their age and calls the ordering function
def Age():
    age = int(input("What is your age (in years, as an integer)? "))
    if age in range(13,19):
        Ordering()
        for i in order:
            print(i)
        print("Your total is $", price)
    else:
        print("You must be between 13 and 18 to use this program.")


#ordering function where all the ordering takes place
def Ordering():
    global price
    #while user has not chosen the exit option, if number of item is chosen, ask quantity and add that quantity of that item to order list and add price of that quantity of that item to price, if exit chosen, break loop, if invalid number chosen, ask user to enter valid number
    while True:
        order_item = input("Enter the number of what you would like to order: ")
        if order_item == "1":
            quantity1 = int(input("Enter quantity (as an integer): "))
            print("{} of Hash Brown added to order.".format(quantity1))
            order.append("x{} Hash Brown".format(quantity1))
            price = price + (item1*quantity1)
        elif order_item == "2":
            quantity2 = int(input("Enter quantity (as an integer): "))
            print("{} of Cookie added to order.".format(quantity2))
            order.append("x{} Cookie".format(quantity2))
            price = price + (item2*quantity2) 
        elif order_item == "3":
            quantity3 = int(input("Enter quantity (as an integer): "))
            print("{} of Nachos added to order.".format(quantity3))
            order.append("x{} Nachos".format(quantity3))
            price = price + (item3*quantity3)
        elif order_item == "4":
            quantity4 = int(input("Enter quantity (as an integer): "))
            print("{} of Garlic Bread added to order.".format(quantity4))
            order.append("x{} Garlic Bread".format(quantity4))
            price = price + (item4*quantity4)
        elif order_item == "5":
            quantity5 = int(input("Enter quantity (as an integer): "))
            print("{} of Burger added to order.".format(quantity5))
            order.append("x{} Burger".format(quantity5))
            price = price + (item5*quantity5)
        elif order_item == "6":
            break           
        else:
            print("Please enter valid integer.")
            
#main code 
#asks user for name, if user name is in student list, call ordering function
student = input("What is your name? ")
if student in students:
    Ordering()
    for i in order:
        print(i)
    print("Your total is $", price)    

#else, (if name is not in student list), ask is user wants to add their name to the list, if yes, call age function, if no, end program
else:
    add_name = input("We can't find your name. (Note that you must add your name to continue ordering with this program.) Would you like to add it? (y/n): ")
    if add_name == "y" or "Y":
        students.append(student)
        Age()   
    else:
        print("Bye! Come back soon!")