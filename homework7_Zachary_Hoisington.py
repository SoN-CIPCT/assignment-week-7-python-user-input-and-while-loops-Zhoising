# Week 7: User Input and While Loops

# List
pizza_orders = ["Pepperoni", "Cheese", "Big New Yorker", "Stuffed Crust", "Three Meat Treat"]

# Empty List
finished_pizzas = []

current_number = 0
while pizza_orders:
    current_pizza = pizza_orders[current_number]
    print("Your " + current_pizza + " pizza pie is finished!")
    finished_pizzas = finished_pizzas + [current_pizza]
    pizza_orders = pizza_orders[1:]

current_number = 0
while finished_pizzas:
    print("The pizza " + finished_pizzas[current_number] + " was made.")
    finished_pizzas = finished_pizzas[1:]
