from core.exchange.ExchangeRate import ExchangeRate

from exchange.rate.InstantRate import InstantRate


class ExchangeRateHolder:

    def __init__(self):
        self.exchange_rates = {}

    def add(self, exchange_rate: ExchangeRate, instant):
        (instrument, to_instrument, rate) = exchange_rate
        instant_rate = InstantRate(instant, rate)
        if instrument not in self.exchange_rates:
            self.exchange_rates[instrument] = {to_instrument: [instant_rate]}
        else:
            instant_rates = self.exchange_rates[instrument][to_instrument]
            instant_rates.append(instant_rate)

    def get_rate(self, instrument, instrument_to, instant):
        rates = [ir.rate for ir in self.exchange_rates[instrument][instrument_to] if ir.instant == instant]
        return rates[0]
