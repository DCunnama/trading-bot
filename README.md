# Trading Bot (Codex-assisted)

A skeletal Python bot that will evolve with the help of OpenAI Codex.

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file or set the following environment variables:

- `TRADING_API_KEY` – your API key for the trading service.
- `TRADING_OAUTH_TOKEN` – OAuth token if using OAuth.

The `TradingAPI` class will read these variables automatically.
