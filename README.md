# Coffee Shop Object Relationships
- Welcome to the Coffee Shop Object Relationships project! ☕️

- In this project, we’ve created a simple domain model for a coffee shop. We have three main classes: Customer, Coffee, and Order. These classes are interconnected, allowing us to track orders, customer preferences, and coffee statistics.

## Project Structure
-  models
- - customer.py: Contains the Customer class.
- - coffee.py: Contains the Coffee class.
- - order.py: Contains the Order class.
- main.py: The main script where we create instances and test functionality.
## Class Descriptions
### Customer
- Represents a coffee shop customer.
- Properties:
- -name: The customer’s name.
- Methods:
- -orders(): Returns a list of orders placed by this customer.
- -coffees(): Returns a unique list of coffees ordered by this customer.
- -create_order(coffee, price): Creates a new order associated with this customer.
- -most_aficionado(coffee): Finds the most loyal customer for a specific coffee.
### Coffee
- Represents a type of coffee.
- Properties:
- - name: The coffee’s name.
- Methods:
- -orders(): Returns a list of orders for this coffee.
- -customers(): Returns a unique list of customers who have ordered this coffee.
- - num_orders(): Calculates the total number of times this coffee has been ordered.
- -average_price(): Computes the average price for this coffee.
### Order
- Represents an order placed by a customer.
- Properties:
- -customer: The customer who placed the order.
- -coffee: The coffee ordered.
- -price: The price of the order.
### Usage
- Clone this repository.
- Navigate to the coffee_shop directory.
- Run python main.py to create instances and test functionality.
Feel free to explore and expand upon this project! Add more features, enhance the classes, or even build a user interface.

Enjoy your virtual coffee! ☕️
