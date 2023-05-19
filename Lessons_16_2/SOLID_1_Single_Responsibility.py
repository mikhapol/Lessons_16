class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        return sum(quantities * prices for quantities, prices in zip(self.quantities, self.prices))


class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Обработка дебетового типа платежа")
        print(f"Проверка кода безопасности: {security_code}")
        order.status = "paid"

    def pay_credit(self, order, security_code):
        print("Обработка кредитного типа платежа")
        print(f"Проверка кода безопасности: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Клавиатура", 1, 2500)
order.add_item("SSD", 1, 7500)
order.add_item("USB-кабель", 2, 250)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order, "0372846")