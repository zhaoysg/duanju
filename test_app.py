import unittest

from app import order_total_cents


class OrderTotalTests(unittest.TestCase):
    def test_total_uses_cents(self):
        self.assertEqual(order_total_cents([199, 299]), 498)

    def test_empty_order(self):
        self.assertEqual(order_total_cents([]), 0)

    def test_single_item_keeps_its_amount(self):
        self.assertEqual(order_total_cents([101]), 101)


if __name__ == "__main__":
    unittest.main()
