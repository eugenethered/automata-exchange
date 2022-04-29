import unittest

from core.number.BigFloat import BigFloat

from exchange.rate.InstantRate import InstantRate


class InstantRateTestCase(unittest.TestCase):

    def test_instant_rate_should_have_instant_and_rate(self):
        instant_rate = InstantRate(1, BigFloat('38835.34'))
        self.assertEqual(instant_rate.instant, 1)
        self.assertEqual(instant_rate.rate, BigFloat('38835.34'))


if __name__ == '__main__':
    unittest.main()
