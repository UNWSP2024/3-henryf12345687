# There are two types of hot dogs  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
# Code123
def hotdogs_sales():
    # Get hot dog type
    hotdog = input("What hot dog would you like? ")
    if hotdog == "hot dog" :
        cost = 3.50 
    elif hotdog == "chili dog" :
        cost = 4.50 
# Ask about toppings
    cheese = input("Would you like cheese on your order? ")
    if cheese == "yes":
        cost += .50
    peppers = input("Would you like peppers on your order? ")
    if peppers == "yes":
        cost += .75
    grilled_onions = input("Would you like grilled onions on your order? ")
    if grilled_onions == "yes":
        cost += 1
# Calcultate tax and total
    tax = cost * .07
    total = cost + tax 
    print(f"Your hot dog costs: ${cost:.2f}")
    print(f"The tax is: ${tax:.2f}")
    print(f"Your total comes out to: ${total:.2f}")


hotdogs_sales()
