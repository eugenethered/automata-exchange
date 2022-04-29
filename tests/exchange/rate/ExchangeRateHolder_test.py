import unittest

from core.exchange.ExchangeRate import ExchangeRate
from core.number.BigFloat import BigFloat

from exchange.rate.ExchangeRateHolder import ExchangeRateHolder


class ExchangeRateTestCase(unittest.TestCase):

    def test_should_add_exchange_rate(self):
        exchange_rate = ExchangeRate('BTC', 'USDT', BigFloat('38835.34'))
        exchange_rate_holder = ExchangeRateHolder()
        exchange_rate_holder.add(exchange_rate, 1)
        rate = exchange_rate_holder.get_rate('BTC', 'USDT', 1)
        self.assertEqual(rate, BigFloat('38835.34'))

    def test_should_add_multiple_exchange_rates(self):
        exchange_rate_1 = ExchangeRate('BTC', 'USDT', BigFloat('38835.34'))
        exchange_rate_2 = ExchangeRate('BTC', 'USDT', BigFloat('38719.72'))
        exchange_rate_holder = ExchangeRateHolder()
        exchange_rate_holder.add(exchange_rate_1, 1)
        exchange_rate_holder.add(exchange_rate_2, 2)
        rate_1 = exchange_rate_holder.get_rate('BTC', 'USDT', 1)
        rate_2 = exchange_rate_holder.get_rate('BTC', 'USDT', 2)
        self.assertEqual(rate_1, BigFloat('38835.34'))
        self.assertEqual(rate_2, BigFloat('38719.72'))


if __name__ == '__main__':
    unittest.main()
