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


class Authorized(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class AuthorizedSMS(Authorized):

    def __init__(self):
        self.authorizer = False

    def auth_sms(self, code):
        print(f"Верификация SMS кода {code}.")
        self.authorizer = True

    def is_authorized(self) -> bool:
        return self.authorizer


class AuthorizedRobot(Authorized):

    def __init__(self):
        self.authorizer = False

    def is_not_robot(self):
        self.authorizer = True

    def is_authorized(self) -> bool:
        return self.authorizer


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorized):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Не авторизован!")
        print("Обработка дебетового типа платежа.")
        print(f"Проверка кода безопасности: {self.security_code}.")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Обработка кредитного типа платежа.")
        print(f"Проверка кода безопасности: {self.security_code}.")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: Authorized):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Не авторизован!")
        print("Обработка paypal платежа.")
        print(f"Использование адреса электронной почты: {self.email_address}.")
        order.status = "paid"


order = Order()
order.add_item("Клавиатура", 1, 2500)
order.add_item("SSD", 1, 7500)
order.add_item("USB-кабель", 2, 250)

print(order.total_price())

print("\n# debit_processor")
authorized = AuthorizedSMS()
authorized.auth_sms("0372846")
debit_processor = DebitPaymentProcessor("0372846", authorized)
debit_processor.pay(order)

print("\n# credit_processor")
credit_processor = CreditPaymentProcessor("7383903")
credit_processor.pay(order)

print("\n# paypal_processor+authorizer")
authorized = AuthorizedRobot()
authorized.is_not_robot()
paypal_processor = PaypalPaymentProcessor("hi@company.com", authorized)
paypal_processor.pay(order)
