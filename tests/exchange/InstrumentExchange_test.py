import unittest

from exchange.InstrumentExchange import InstrumentExchange


class InstrumentExchangeTestCase(unittest.TestCase):

    def test_create_instrument_exchange(self):
        instrument_exchange = InstrumentExchange(instrument='BTC', to_instrument='USDT')
        self.assertEqual('BTC', instrument_exchange.instrument)
        self.assertEqual('USDT', instrument_exchange.to_instrument)

    def test_unpack_instrument_exchange(self):
        (instrument, to_instrument) = InstrumentExchange('BTC', 'USDT')
        self.assertEqual('BTC', instrument)
        self.assertEqual('USDT', to_instrument)


if __name__ == '__main__':
    unittest.main()
