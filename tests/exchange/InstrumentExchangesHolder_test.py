import unittest

from exchange.InstrumentExchange import InstrumentExchange
from exchange.InstrumentExchangesHolder import InstrumentExchangesHolder


class InstrumentExchangesHolderTestCase(unittest.TestCase):

    def test_should_add_instrument_exchange(self):
        holder = InstrumentExchangesHolder()
        holder.add(InstrumentExchange('BTC', 'USDT'))
        exchanges = holder.get('BTC')
        self.assertEqual(len(exchanges), 1)
        self.assertEqual(exchanges, [InstrumentExchange('BTC', 'USDT')])

    def test_should_add_multiple_instrument_exchanges(self):
        holder = InstrumentExchangesHolder()
        holder.add(InstrumentExchange('BTC', 'USDT'))
        holder.add(InstrumentExchange('BTC', 'ETH'))
        holder.add(InstrumentExchange('BTC', 'GBP'))
        exchanges = holder.get('BTC')
        self.assertEqual(len(exchanges), 3)
        self.assertEqual(exchanges, [InstrumentExchange('BTC', 'USDT'), InstrumentExchange('BTC', 'ETH'), InstrumentExchange('BTC', 'GBP')])

    def test_should_get_exchanges_for_instrument(self):
        holder = InstrumentExchangesHolder()
        holder.add(InstrumentExchange('BTC', 'USDT'))
        holder.add(InstrumentExchange('BTC', 'ETH'))
        holder.add(InstrumentExchange('BTC', 'GBP'))
        holder.add(InstrumentExchange('ETH', 'USDT'))
        holder.add(InstrumentExchange('ETH', 'GBP'))
        exchanges = holder.get('BTC')
        self.assertEqual(len(exchanges), 3)
        self.assertEqual(exchanges, [InstrumentExchange('BTC', 'USDT'), InstrumentExchange('BTC', 'ETH'), InstrumentExchange('BTC', 'GBP')])

    def test_should_not_get_exchanges_for_non_existent_instrument(self):
        holder = InstrumentExchangesHolder()
        exchanges = holder.get('NON-EXISTENT')
        self.assertIsNone(exchanges)


if __name__ == '__main__':
    unittest.main()
