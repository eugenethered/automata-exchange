class InstrumentExchange:

    def __init__(self):
        self.exchanges = {}

    def add(self, instrument, to_instrument):
        if instrument not in self.exchanges:
            self.exchanges[instrument] = [to_instrument]
        else:
            instrument_exchanges = self.exchanges[instrument]
            instrument_exchanges.append(to_instrument)

    def get(self, instrument):
        if instrument not in self.exchanges:
            return None
        return list([(k, vi) for k, v in self.exchanges.items() if k == instrument for vi in v])
