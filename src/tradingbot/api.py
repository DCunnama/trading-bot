import os


class TradingAPI:
    """Simple trading API wrapper handling authentication."""

    def __init__(self, api_key: str | None = None, oauth_token: str | None = None) -> None:
        self.api_key = api_key or os.getenv("TRADING_API_KEY")
        self.oauth_token = oauth_token or os.getenv("TRADING_OAUTH_TOKEN")
        if not self.api_key and not self.oauth_token:
            raise ValueError("An API key or OAuth token must be provided")

    def _get_headers(self) -> dict:
        """Return HTTP headers for authenticated requests."""
        if self.oauth_token:
            return {"Authorization": f"Bearer {self.oauth_token}"}
        return {"X-API-KEY": self.api_key}

    def get_price(self, symbol: str):
        """Return the latest price for a trading pair."""
        # TODO: Call the real price endpoint
        raise NotImplementedError

    def place_order(self, symbol: str, quantity: int, side: str):
        """Place an order.

        Parameters
        ----------
        symbol:
            Market symbol such as ``BTCUSD``.
        quantity:
            The amount to buy or sell.
        side:
            Either ``buy`` or ``sell``.
        """
        # TODO: Call the real order endpoint
        raise NotImplementedError

