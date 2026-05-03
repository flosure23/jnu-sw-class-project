# test_order_mock.py

import unittest
from unittest.mock import Mock
from order_service import OrderService

class TestOrderServiceWithMock(unittest.TestCase):
    def setUp(self):
        self.mock_notifier = Mock()
        self.service = OrderService(self.mock_notifier)

    def test_place_order_calls_notifier(self):
        result = self.service.place_order("lee", "mouse", 15000)

        self.assertEqual(result, "ORDER_OK")
        self.mock_notifier.send.assert_called_with("lee ordered mouse (15000)")

if __name__ == "__main__":
    unittest.main(verbosity=2)