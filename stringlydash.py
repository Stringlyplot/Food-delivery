
resturants = ["Chipotle", "Q39"]
#list in a dictinoary for the prices of each item
resturant_menu_items = [{"1": 7.95, "2": 9.30, "3": 8.50}, {"1": 13.25, "2": 16.50, "3": 12.99}]

def Chipotle_menu():
    #chipotle menu
    print("\nChipotle menu: \n1 - Chicken burrito $7.95 \n2 - Steak burrito bowl $ 9.30 \n3- Chicken Quesadilla $8.50\n\nEnter 1/2/3 to add items to your order")
    input(">>> ")

def Q39_menu():
    #Q39 menu
    while True:
        print("\nQ39 menu: \n1 - Wings $13.25\n2 - Burnt End Burger $ 16.50\n3 - Brisket $12.99\n\nEnter 1/2/3 to add items to your order")
        choice = int(input(">>>"))
        final_decision = input("Anything else (Y/N): ")
        order = resturant_menu_items[choice - 1][choice - 1]
        if final_decision.lower in ["yes", "y", "ye", "ys", "es", "yess", "yesss"]:
            pass
        elif final_decision.lower in ["no", "n", "o", "noo", "nooo"]:
            break

    return

#Begining
def introduction():
    #Prints the intial greetings and selection of resturants
    print ("\nWelcome to 101 delivery")
    print("We devliver from the following 2 resturants\n")
    print("1 - Chipotle, 2 - Q39\n\nEnter your choice:\n1. Chipotle\n2. Q39\n3. Both")
    #
    user_resturant_choice = int(input(">>> "))
    return user_resturant_choice

def overall_order():
    
    
    pass

user_resturant_choice = introduction()
overall_order()
#Picks the resturant that the user picks
print(resturants[user_resturant_choice - 1])








"""
1- Chicken burrito $7.95
2- Steak burrito bowl $ 9.30
3- Chicken Quesadilla $8.50
Enter 1/2/3 to add items to your order
"""