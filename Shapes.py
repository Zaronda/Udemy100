from prettytable import PrettyTable
# Pascal font
table = PrettyTable()
# table.add_column("ch",["1","2", "7"])
table.add_column("Ingredients",["Onion","Tomato", "Peppers", "Herbs"])
table.add_column("Location", ["Trolly", "Fridge", "Fridge", "Spice rack"])
table.add_column("Amount", ["One", "One Tin", "Three", "Pinch"])
table.align = "l"
print(table)
