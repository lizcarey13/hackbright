"""
Lists Lecture Exercise.
This project is a shopping list app.
We have a global list that will be our shopping list.
Make sure your code deals with upper and lower case.
"""
shopping_list = []


def add_shopping_list(item):
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "Here's your updated list", sorted_shopping_list()
    else:
        print "This item %s already exists!" % (item)


def sorted_shopping_list():
    shopping_list.sort()
    return shopping_list


def remove_item(item):
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s has been removed. Here's your updated list" % (item), sorted_shopping_list()
    else:
        print "%s was not on the list." % (item)

def print_menu():
        print "0 - Main Menu"
        print "1 - Show current list"
        print "2 - Add an item to your shopping list"
        print "3 - Remove item from your shopping list"
        x = int(raw_input("What would you like to do? "))
        return x

def main():
    x = print_menu()
    
    while True:
        if x == 0:
            x = print_menu()
        elif x == 1:
            print "This is your current list,", shopping_list
            x = 0
        elif x == 2:
            y = raw_input("What would you like to add? ")
            add_shopping_list(y)
            x = 0
        elif x == 3:
            y = raw_input("What would you like to remove? ")
            remove_item(y)
            x = 0
        else:
            print "Please enter a valid item "
            x = 0

if __name__ == "__main__":
    main()
