import unittest

from exchange.InstrumentExchange import InstrumentExchange


class InstrumentExchangeTestCase(unittest.TestCase):

    def test_should_add_instrument_exchange(self):
        instrument_exchange = InstrumentExchange()
        instrument_exchange.add('BTC', 'USDT')
        exchanges = instrument_exchange.get('BTC')
        print(f'{exchanges}')
        self.assertEqual(len(exchanges), 1)
        self.assertEqual(exchanges, [('BTC', 'USDT')])

    def test_should_add_multiple_instrument_exchanges(self):
        instrument_exchange = InstrumentExchange()
        instrument_exchange.add('BTC', 'USDT')
        instrument_exchange.add('BTC', 'ETH')
        instrument_exchange.add('BTC', 'GBP')
        exchanges = instrument_exchange.get('BTC')
        self.assertEqual(len(exchanges), 3)
        self.assertEqual(exchanges, [('BTC', 'USDT'), ('BTC', 'ETH'), ('BTC', 'GBP')])

    def test_should_get_exchanges_for_instrument(self):
        instrument_exchange = InstrumentExchange()
        instrument_exchange.add('BTC', 'USDT')
        instrument_exchange.add('BTC', 'ETH')
        instrument_exchange.add('BTC', 'GBP')
        instrument_exchange.add('ETH', 'USDT')
        instrument_exchange.add('ETH', 'GBP')
        exchanges = instrument_exchange.get('BTC')
        self.assertEqual(len(exchanges), 3)
        self.assertEqual(exchanges, [('BTC', 'USDT'), ('BTC', 'ETH'), ('BTC', 'GBP')])

    def test_should_not_get_exchanges_for_non_existent_instrument(self):
        instrument_exchange = InstrumentExchange()
        exchanges = instrument_exchange.get('NON-EXISTENT')
        self.assertIsNone(exchanges)


if __name__ == '__main__':
    unittest.main()
