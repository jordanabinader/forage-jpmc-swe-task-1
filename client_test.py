import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    _, _, _, price_1 = getDataPoint(quotes[0])
    _, _, _, price_2 = getDataPoint(quotes[1])

    self.assertAlmostEqual(price_1, 120.84, places=2, msg="Average price for stock 'ABC' is incorrect.")
    self.assertAlmostEqual(price_2, 119.775, places=2, msg="Average price for stock 'DEF' is incorrect.")

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    _, _, _, price_1 = getDataPoint(quotes[0])
    _, _, _, price_2 = getDataPoint(quotes[1])

    self.assertAlmostEqual(price_1, 119.84, places=2, msg="Average price for stock 'ABC' is incorrect.")
    self.assertAlmostEqual(price_2, 119.775, places=2, msg="Average price for stock 'DEF' is incorrect.")

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    # Positive ratio test
    result = getRatio(100, 50)
    assert result == 2.0, f"Result computed is {result}, but expected is 2.0"

    # Negative ratio test
    result = getRatio(-50, 100)
    assert result == -0.5, f"Result computed is {result}, but expected is -0.5"

    # Divide by zero test
    try:
      result = getRatio(100, 0)
      if result is None or result == '':
        print("getRatio 0 division test passed, edge case considered")
    except:
      print("getRatio 0 division test failed, edge case not considered")

if __name__ == '__main__':
    unittest.main()
