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
    def pay(self, order):
        pass


class PaymentProcessorSMS(PaymentProcessor):

    @abstractmethod
    def pay(self, order):
        pass

    @abstractmethod
    def auth_sms(self):
        pass


class DebitPaymentProcessor(PaymentProcessorSMS):

    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self):
        print(f"Верификация SMS кода: {self.security_code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Не авторизован!")
        print("Обработка дебетового типа платежа.")
        print(f"Проверка кода безопасности: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Обработка кредитного типа платежа.")
        print(f"Проверка кода безопасности: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessorSMS):

    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False

    def auth_sms(self):
        print(f"Верификация SMS кода: {self.email_address}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Не авторизован!")
        print("Обработка paypal платежа.")
        print(f"Использование адреса электронной почты: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Клавиатура", 1, 2500)
order.add_item("SSD", 1, 7500)
order.add_item("USB-кабель", 2, 250)

print(order.total_price())

print("# debit_processor")
debit_processor = DebitPaymentProcessor("0372846")
debit_processor.auth_sms()
debit_processor.pay(order)

print("# credit_processor")
credit_processor = CreditPaymentProcessor("7383903")
credit_processor.pay(order)

print("# paypal_processor")
paypal_processor = PaypalPaymentProcessor("hi@company.com")
paypal_processor.auth_sms()
paypal_processor.pay(order)
