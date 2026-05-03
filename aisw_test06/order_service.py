# order_service.py

class OrderService:
    def __init__(self, notifier):
        self.notifier = notifier

    def place_order(self, user, item, price):
        message = f"{user} ordered {item} ({price})"
        self.notifier.send(message)
        return "ORDER_OK"