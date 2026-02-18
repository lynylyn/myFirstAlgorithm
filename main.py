import time
from time import sleep

menuitems = [
    {
        "numero": 1,
        "desc": 'Ham & Cheese Sandwich',
        "price": 4,
    },
    {
        "numero": 2,
        "desc": 'Chicken, Cheese & Tomato Sandwich',
        "price": 4.90,
    },
    {
        "numero": 3,
        "desc": 'Tuna Sushi',
        "price": 4
    },
    {
        "numero": 4,
        "desc": 'Salad Wrap',
        "price": 6.50
    },
    {
        "numero": 5,
        "desc": 'Falafel Wrap',
        "price": 6.90
    },
    {
        "numero": 6,
        "desc": 'Fruit Salad Bowl',
        'price': 6
    },
    {
        "numero": 7,
        "desc": 'Muffin',
        "price": 4.20
    },
    {
        "numero": 8,
        "desc": 'Bacon & Egg Roll',
        "price": 5.20
    },
    {
        'numero': 9,
        "desc": 'Hash Brown',
        "price": 1.50
    },
    {
        "numero": 10,
        "desc": 'Sour Snap Stix',
        "price": 1
    },
    {
        "numero": 11,
        "desc": 'Up N Go',
        "price": 3.50
    },
    {
        "numero": 12,
        "desc": 'Chicken Burger',
        "price": 5.50
    },
    {
        'numero': 13,
        "desc": 'Sausage Roll',
        'price': 4
    },
    {
        "numero": 14,
        'desc': 'Meat Pie',
        'price': 5.20
    }
]

def printmenu():
    for item in menuitems:
        print(f"({item['numero']}) {item['desc']} — ${item['price']:.2f}")

def finditem(selection):
    for item in menuitems:
        if str(item['numero']) == selection:
            return item
    return None

print("\nWelcome to the GHS lunch order system.")
time.sleep(0.5)
studentname = input("\nPlease input your name. ")
print(f"\nHere is the menu, {studentname}:\n")
time.sleep(0.5)
printmenu()

totalprice = 0
orderitems = []
while True:
    selection = input("Please input the number of the food you'd like to order, or press '0' to end: ")
    if selection == "0":
        break
    item = finditem(selection)
    if item == None:
        print("The selection was invalid.")
        continue
    totalprice = totalprice + item['price']
    orderitems.append(item)

if totalprice >= 20:
    finalprice = totalprice * 0.8
elif totalprice >= 10:
    finalprice = totalprice * 0.9
else:
    finalprice = totalprice

print("\nRECEIPT:\n")
for item in orderitems:
    print(f"{item['desc']:40} ${item['price']:.2f}")
print(f"{'TOTAL:':40} ${totalprice:.2f}")
print(f"{'PRICE AFTER DISCOUNT:':40} ${finalprice:.2f}")