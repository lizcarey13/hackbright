"""
Lists Lecture Exercise.
This project is a shopping list app.
We have a global list that will be our shopping list.
Make sure your code deals with upper and lower case.
"""
shopping_list = []


def add_shopping_list():
    item = raw_input("What would you like to add? ")
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "Here's your updated list", sorted_shopping_list()
    else:
        print "This item %s already exists!" % (item)


def sorted_shopping_list():
    shopping_list.sort()
    return shopping_list


def remove_item():
    item = raw_input("What would you like to remove? ")
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s has been removed. Here's your updated list" % (item), sorted_shopping_list()
    else:
        print "%s was not on the list." % (item)

def print_menu():
    while(True):
        print "0 - Main Menu"
        print "1 - Show current list"
        print "2 - Add an item to your shopping list"
        print "3 - Remove item from your shopping list"
        x = raw_input("What would you like to do? ")
        if x == "0":
            print_menu()
        elif x == "1":
            print shopping_list
        elif x == "2":
            add_shopping_list()
        elif x == "3":
            remove_item()
        elif x == "exit":
            break
        else: 
            print "Please enter a real number"

if __name__ == "__main__":
    print_menu()
