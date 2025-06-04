from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class TradingStrategy(ABC):
    """Abstract base class for trading strategies."""

    @abstractmethod
    def should_buy(self, prices: pd.Series) -> bool:
        """Return True if a buy signal is generated given price history."""
        raise NotImplementedError

    @abstractmethod
    def should_sell(self, prices: pd.Series) -> bool:
        """Return True if a sell signal is generated given price history."""
        raise NotImplementedError


class SmaCrossStrategy(TradingStrategy):
    """Simple moving average cross over strategy."""

    def __init__(self, short_window: int, long_window: int) -> None:
        if short_window >= long_window:
            raise ValueError("short_window must be less than long_window")
        self.short_window = short_window
        self.long_window = long_window

    def _has_enough_data(self, prices: pd.Series) -> bool:
        return len(prices) >= self.long_window + 1

    def _sma(self, prices: pd.Series, window: int) -> pd.Series:
        return prices.rolling(window).mean()

    def should_buy(self, prices: pd.Series) -> bool:
        if not self._has_enough_data(prices):
            return False
        short_sma = self._sma(prices, self.short_window)
        long_sma = self._sma(prices, self.long_window)
        prev_short, prev_long = short_sma.iloc[-2], long_sma.iloc[-2]
        last_short, last_long = short_sma.iloc[-1], long_sma.iloc[-1]
        return prev_short <= prev_long and last_short > last_long

    def should_sell(self, prices: pd.Series) -> bool:
        if not self._has_enough_data(prices):
            return False
        short_sma = self._sma(prices, self.short_window)
        long_sma = self._sma(prices, self.long_window)
        prev_short, prev_long = short_sma.iloc[-2], long_sma.iloc[-2]
        last_short, last_long = short_sma.iloc[-1], long_sma.iloc[-1]
        return prev_short >= prev_long and last_short < last_long


__all__ = ["TradingStrategy", "SmaCrossStrategy"]
