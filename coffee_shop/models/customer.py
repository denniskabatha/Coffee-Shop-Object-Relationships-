class Customer:
    _all = []

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name
        Customer._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def orders(self):
        from models.order import Order
        return [order for order in Order._all if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        from models.order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}
        for order in coffee.orders():
            customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price
        return max(customer_spending, key=customer_spending.get) if customer_spending else None
