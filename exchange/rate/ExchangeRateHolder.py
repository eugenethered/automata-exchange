from core.exchange.ExchangeRate import ExchangeRate

from exchange.rate.InstantRate import InstantRate


class ExchangeRateHolder:

    def __init__(self, *args):
        self.exchange_rates = {}
        self.__parse_args(args)

    def __parse_args(self, args):
        if len(args) == 1 and type(args[0]) is list:
            interval_exchange_rates = args[0]
            self.add_multiple(interval_exchange_rates)

    def add_multiple(self, interval_exchange_rates):
        for exchange_rate, interval in interval_exchange_rates:
            self.add(exchange_rate, interval)

    def add(self, exchange_rate: ExchangeRate, instant):
        (instrument, to_instrument, rate) = exchange_rate
        instant_rate = InstantRate(instant, rate)
        self.__append(instrument, to_instrument, instant_rate)

    def __append(self, instrument, to_instrument, instant_rate):
        if instrument not in self.exchange_rates:
            self.exchange_rates[instrument] = {to_instrument: [instant_rate]}
        else:
            instant_rates = self.exchange_rates[instrument][to_instrument]
            instant_rates.append(instant_rate)

    def get(self, instrument=None):
        if instrument is None:
            return self.exchange_rates
        if instrument not in self.exchange_rates:
            return {}
        return dict([(k, v) for k, v in self.exchange_rates.items() if k == instrument])

    def get_rate(self, instrument, instrument_to, instant):
        if instrument not in self.exchange_rates or instrument_to not in self.exchange_rates[instrument]:
            return None
        return next(ir.rate for ir in self.exchange_rates[instrument][instrument_to] if ir.instant == instant)

    def get_rates(self, instrument, to_instrument):
        return self.exchange_rates[instrument][to_instrument]
