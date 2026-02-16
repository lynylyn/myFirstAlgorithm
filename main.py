import time
from time import sleep

def getmenu(d, indent=0):
    res = ""
    for k, v in d.items():
        res += "\t"*indent + str(k) + "\n"
        if isinstance(v, dict):
            res += getmenu(v, indent+1)
        else:
            res += "\t"*(indent+1) + str(v) + "\n"
    return res
menu = {
        '(1) Ham & Cheese Sandwich': 4,
        '(2) Chicken, Cheese & Tomato Sandwich': 4.90,
        '(3) Tuna Sushi': 4,
        '(4) Salad Wrap': 6.50,
        '(5) Falafel Wrap': 6.90,
        '(6) Fruit Salad Bowl': 6,
        '(7) Muffin': 4.20,
        '(8) Bacon & Egg Roll': 5.20,
        '(9) Hash Brown': 1.50,
        '(10) Sour Snap Stix': 1,
        '(11) Up N Go': 3.50,
        '(12) Chicken Burger': 5.50,
        '(13) Sausage Roll': 4,
        '(14) Meat Pie': 5.20
    }

print("\nWelcome to the GHS lunch order system.")
time.sleep(1)
studentname = input("\nPlease input your name. ")
print(f"\nHere is the menu, {studentname}:\n")
time.sleep(1)
print(getmenu(menu))

    while moreitems == 'true'
        item = input("Please input which food you'd like to order: ")
        
