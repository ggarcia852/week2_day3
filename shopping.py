
def shopping():
    shopping_cart = []
    while True:
        name = input("What is your name? \n Enter 'quit' at any point to stop shopping ")
        if name.lower() == "quit":
            break
            
        item = input(f"Hello, {name.title()}! What would you like to purchase today? ")
        if item.lower() == "quit":
            break
        else:
            shopping_cart.append(item)
            
        add = input("What would you like to do next? \n Enter 'Add' to add more items \n Enter 'Remove' to remove an item \n Enter 'Finish' to finish and pay \n Enter 'View' to view your cart ") 
        if add.lower() == "quit":
            break
        elif add.lower() == "add":
            next_item = input("What else would you like to purchase? ")
            if next_item.lower() == "quit":
                break
            else:
                shopping_cart.append(next_item)
        elif add.lower() == "remove":
            print(shopping_cart)
            remov = input("Which item would you like to remove? ")
            if remov.lower() == "quit":
                break
            else:
                shopping_cart.remove(remov)
        elif add.lower() == "finish":
            finish = input("Are you sure you dont want to purchase more items? ")
            if finish.lower() == "yes":
                print("Ok your items are free today! Here is what you purchased: " + str(shopping_cart))
                break
            elif finish.lower() == "no":
                another_item = input("What else would you like to purchase? ")
                if another_item.lower() == "quit":
                    break
                else:
                    shopping_cart.append(another_item)
        elif add.lower() == "view":
            print(shopping_cart)
        
shopping()
