def pretty_print_dict(d, indent=0):
    res = ""
    for k, v in d.items():
        res += "\t"*indent + str(k) + "\n"
        if isinstance(v, dict):
            res += pretty_print_dict(v, indent+1)
        else:
            res += "\t"*(indent+1) + str(v) + "\n"
    return res
test_dict = {
            'Ham & Cheese Sandwich': 4,
            'Chicken, Cheese & Tomato Sandwich': 4.90,
            'Tuna Sushi': 4,
            'Salad Wrap': 6.50,
            'Falafel Wrap': 6.90,
            'Fruit Salad Bowl': 6,
            'Muffin': 4.20,
            'Bacon & Egg Roll': 5.20,
            'Hash Brown': 1.50,
            'Sour Snap Stix': 1,
            'Up N Go': 3.50,
            'Chicken Burger': 5.50,
            'Sausage Roll': 4,
            'Meat Pie': 5.20
        }

print("The Pretty Print dictionary is : ")
print(pretty_print_dict(test_dict))