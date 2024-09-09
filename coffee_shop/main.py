# main.py

# main.py

from models.customer import Customer
from models.coffee import Coffee
from models.order import Order

# Rest of your code...

# Create some customers
dennis = Customer("Dennis")
mark = Customer("Mark")

# Create some coffees
domans = Coffee("Domans")
latte = Coffee("Latte")

# Place orders
order1 = dennis.create_order(domans, 5.50)
order2 = mark.create_order(latte, 4.75)

# Test methods
print(f"{dennis.name} ordered {len(dennis.orders())} times.")
print(f"{latte.name} has been ordered {latte.num_orders()} times.")
print(f"Average price for {latte.name}: ${latte.average_price():.2f}")

# Find the most loyal customer for a specific coffee
most_loyal = Customer.most_aficionado(latte)
if most_loyal:
    print(f"The most loyal customer for {latte.name} is {most_loyal.name}.")
else:
    print(f"No customers have ordered {latte.name} yet.")
