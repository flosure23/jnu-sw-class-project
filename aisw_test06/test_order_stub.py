# test_order_stub.py

import unittest
from order_service import OrderService

class StubNotifier:
    def send(self, message):
        return "sent"

class TestOrderServiceWithStub(unittest.TestCase):
    def setUp(self):
        self.notifier = StubNotifier()
        self.service = OrderService(self.notifier)

    def test_place_order_returns_ok(self):
        result = self.service.place_order("kim", "keyboard", 30000)
        self.assertEqual(result, "ORDER_OK")

if __name__ == "__main__":
    unittest.main(verbosity=2)