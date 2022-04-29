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
        if instrument not in self.exchange_rates or instrument_to not in self.exchange_rates[instrument]:
            return None
        return next(ir.rate for ir in self.exchange_rates[instrument][instrument_to] if ir.instant == instant)

    def get_rates(self, instrument, to_instrument):
        return self.exchange_rates[instrument][to_instrument]
