# Define three different payment methods
class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")


class BankTransferPayment:
    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount}")


# Polymorphic function
def make_payment(payment_method, amount):
    payment_method.process_payment(amount)


if __name__ == "__main__":
    # Create one object of each payment method
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    bank_transfer = BankTransferPayment()

    # Store in a list for iteration
    payments = [credit_card, paypal, bank_transfer]
    amounts = [100, 250, 500]

    # Demonstrate polymorphism: same function works with different objects
    print("=== Payment Processing ===")
    for method, amt in zip(payments, amounts):
        make_payment(method, amt)
