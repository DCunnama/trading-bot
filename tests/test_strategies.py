import pandas as pd

from tradingbot.strategies import SmaCrossStrategy


def test_sma_cross_buy():
    prices = pd.Series([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6], dtype=float)
    strat = SmaCrossStrategy(short_window=3, long_window=5)
    assert strat.should_buy(prices) is True
    assert strat.should_sell(prices) is False


def test_sma_cross_sell():
    prices = pd.Series([9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 7], dtype=float)
    strat = SmaCrossStrategy(short_window=3, long_window=5)
    assert strat.should_sell(prices) is True
    assert strat.should_buy(prices) is False
