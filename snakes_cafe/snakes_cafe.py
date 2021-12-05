banner = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
"""

menu = """
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""

prompt = """
***********************************
** What would you like to order? **
***********************************
"""

items = [
    "Wings",
    "Cookies",
    "Spring Rolls",
    "Salmon",
    "Steak",
    "Meat Tornado",
    "A Literal Garden",
    "Ice Cream",
    "Cake",
    "Pie",
    "Coffee",
    "Tea",
    "Unicorn Tears",
]

cart = {}
if __name__ == "__main__":
    print(banner, menu, prompt)
    order_complete = False
    while not order_complete:
        order = input("> ").title()
        if order == "Quit":
            order_complete = True
        elif order in items:
            if order in cart:
                cart[order] = cart[order] + 1
            else:
                cart[order] = 1
            print(
                f"\n** {cart[order]} order of {order} have been added to your meal **\n"
            )
        else:
            print(f"\nSorry, {order} is not available, try other menu.\n")
    # print and format order summary
    summary = ""
    count = 14
    for item in cart:
        line = f"{item}    {cart[item]}\n"
        if len(line) > count:
            count = len(line)
        summary = summary + line
    summary = (
        "\n\nOrder Summary\n" + "*" * count + "\n" + summary[0:-1] + "\n" + "*" * count
    )
    print(summary)
