import unittest

from core.exchange.ExchangeRate import ExchangeRate
from core.number.BigFloat import BigFloat

from exchange.rate.ExchangeRateHolder import ExchangeRateHolder
from exchange.rate.InstantRate import InstantRate


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

    def test_should_obtain_rates_for_instruments(self):
        exchange_rate_holder = ExchangeRateHolder()
        exchange_rate_holder.add(ExchangeRate('BTC', 'USDT', BigFloat('38835.34')), 1)
        exchange_rate_holder.add(ExchangeRate('BTC', 'USDT', BigFloat('38719.72')), 2)
        rates = exchange_rate_holder.get_rates('BTC', 'USDT')
        self.assertEqual(len(rates), 2)
        self.assertEqual(rates[0], InstantRate(1, BigFloat('38835.34')))
        self.assertEqual(rates[1], InstantRate(2, BigFloat('38719.72')))

    def test_should_not_get_rates_for_non_existent_instruments(self):
        exchange_rate_holder = ExchangeRateHolder()
        rate = exchange_rate_holder.get_rate('BTC', 'USDT', 1)
        self.assertIsNone(rate)
        exchange_rate_holder = ExchangeRateHolder()
        exchange_rate_holder.add(ExchangeRate('BTC', 'USDT', BigFloat('38835.34')), 1)
        rate = exchange_rate_holder.get_rate('BTC', 'ETH', 1)
        self.assertIsNone(rate)

    def test_should_get_exchange_rates_graph_filtered_by_instrument(self):
        exchange_rate_holder = ExchangeRateHolder()
        exchange_rate_holder.add(ExchangeRate('BTC', 'USDT', BigFloat('38835.34')), 1)
        exchange_rate_holder.add(ExchangeRate('BTC', 'USDT', BigFloat('38719.72')), 2)
        exchange_rate_holder.add(ExchangeRate('ETH', 'USDT', BigFloat('2861.62')), 1)
        exchange_rates = exchange_rate_holder.get('BTC')
        self.assertEqual(len(exchange_rates), 1)
        self.assertEqual(len(exchange_rates['BTC']['USDT']), 2)

    def test_should_get_exchange_rates_graph_filtered_by_instrument_exchange(self):
        exchange_rate_holder = ExchangeRateHolder()
        exchange_rate_holder.add(ExchangeRate('BTC', 'USDT', BigFloat('38835.34')), 1)
        exchange_rate_holder.add(ExchangeRate('BTC', 'USDT', BigFloat('38719.72')), 2)
        exchange_rate_holder.add(ExchangeRate('ETH', 'USDT', BigFloat('2861.62')), 1)
        exchange_rates = exchange_rate_holder.get()
        self.assertEqual(len(exchange_rates), 2)
        self.assertEqual(len(exchange_rates['BTC']), 1)
        self.assertEqual(len(exchange_rates['BTC']['USDT']), 2)
        self.assertEqual(len(exchange_rates['ETH']), 1)
        self.assertEqual(len(exchange_rates['ETH']['USDT']), 1)

    def test_should_not_get_exchange_rates(self):
        exchange_rate_holder = ExchangeRateHolder()
        exchange_rates = exchange_rate_holder.get('NON-EXISTENT')
        self.assertEqual(exchange_rates, {}, 'should be empty dict')

    def test_should_initialize_exchange_rates(self):
        exchange_rate_holder = ExchangeRateHolder([
            (ExchangeRate('BTC', 'USDT', BigFloat('38835.34')), 1),
            (ExchangeRate('BTC', 'USDT', BigFloat('38719.72')), 2),
            (ExchangeRate('ETH', 'USDT', BigFloat('2861.62')), 1)
        ])
        self.assertEqual(exchange_rate_holder.get_rate('BTC', 'USDT', 1), BigFloat('38835.34'))
        self.assertEqual(exchange_rate_holder.get_rate('BTC', 'USDT', 2), BigFloat('38719.72'))
        self.assertEqual(exchange_rate_holder.get_rate('ETH', 'USDT', 1), BigFloat('2861.62'))

    def test_should_initialize_multiple_exchange_rates(self):
        exchange_rate_holder = ExchangeRateHolder([
            (ExchangeRate('OTC', 'USDT', BigFloat('150.00')), 2),
            (ExchangeRate('OTC', 'USDT', BigFloat('100.00')), 1),
            (ExchangeRate('OTC', 'BUSD', BigFloat('100.00')), 2),
            (ExchangeRate('OTC', 'BUSD', BigFloat('150.00')), 1)
        ])
        print(f'result? -> {exchange_rate_holder.get()}')
        self.assertEqual(exchange_rate_holder.get_rate('OTC', 'USDT', 2), BigFloat('150.00'))
        self.assertEqual(exchange_rate_holder.get_rate('OTC', 'USDT', 1), BigFloat('100.00'))
        self.assertEqual(exchange_rate_holder.get_rate('OTC', 'BUSD', 2), BigFloat('100.00'))
        self.assertEqual(exchange_rate_holder.get_rate('OTC', 'BUSD', 1), BigFloat('150.00'))


if __name__ == '__main__':
    unittest.main()
