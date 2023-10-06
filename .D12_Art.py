################### Scope ####################

enemies = "Zombie"

def increase_enemies():
    global enemies
    enemies = "Skeleton"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
