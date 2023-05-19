from abc import ABC, abstractmethod


class Order:  # Класс Order не менялся.

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


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Обработка дебетового типа платежа.")
        print(f"Проверка кода безопасности: {security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Обработка кредитного типа платежа.")
        print(f"Проверка кода безопасности: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Клавиатура", 1, 2500)
order.add_item("SSD", 1, 7500)
order.add_item("USB-кабель", 2, 250)

print(order.total_price())
debit_processor = DebitPaymentProcessor()
debit_processor.pay(order, "0372846")

credit_processor = CreditPaymentProcessor()
credit_processor.pay(order, "7383903")
