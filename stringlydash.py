
resturants = ["Welcome to Chipotle", "Welcome to Q39", "Chiptole & Q39"]
#list in a dictinoary for the prices of each item
resturant_menu_items = [{"1": 7.95, "2": 9.30, "3": 8.50}, {"1": 13.25, "2": 16.50, "3": 12.99}]
def chipotle_menu():
    #chipotle menu
    chipotle = ("\nChipotle menu: \n1 - Chicken burrito $7.95 \n2 - Steak burrito bowl $ 9.30 \n3- Chicken Quesadilla $8.50\n\nEnter 1/2/3 to add items to your order")
    return chipotle
def q39_menu():
    #Q39 menu
    q39 = ("\nQ39 menu: \n1 - Wings $13.25\n2 - Burnt End Burger $ 16.50\n3 - Brisket $12.99\n\nEnter 1/2/3 to add items to your order")
    return q39
#Will pick the correct resturant

menus = {1: chipotle_menu, 2: q39_menu}


#Begining
def introduction():
    #Prints the intial greetings and selection of resturants
    print ("\nWelcome to 101 delivery")
    print("We devliver from the following 2 resturants\n")
    print("1 - Chipotle, 2 - Q39\n\nEnter your choice:\n1. Chipotle\n2. Q39\n3. Both")
    #Where the user will pick the resturant
    user_resturant_choice = int(input(">>> "))
    #This will return the users choice of resturant either chipotle or Q39 or both
    return user_resturant_choice
#This is where the order is going to mainly be and will call the other functions
def overall_order(menus_choice):
     #This checks the menu list for th functions and calls it with the parenthesis at the end
    print (menus[menus_choice]())
    #Asks user for there choice of menu
    order = input(">>> ")
    #picks the correct menu and menu order
    resturant_menu_items[menus_choice][order]

    


    
    
    pass

user_resturant_choice = introduction()
overall_order(user_resturant_choice)
#Picks the resturant that the user picks

