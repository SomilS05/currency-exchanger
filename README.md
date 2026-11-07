# Currency Exchanger

A Python command-line tool that converts between currencies using rates quoted against USD. It fetches the provider's latest daily rates once per session, so you can run multiple conversions without another request.

## Run

Use Python 3. Both versions use the standard library.

```sh
python3 Currency_exchanger.py
```

This version requires an internet connection to load exchange rates. To use the version that falls back to a small set of illustrative rates when the provider is unavailable, run the following command.

```sh
python3 USD_Ex.py
```

Choose a source and target currency, then enter the amount. Currency codes are case-insensitive. Enter `exit` at the source prompt to quit. The program labels the offline sample rates when it uses them.

[Rates by ExchangeRate-API](https://www.exchangerate-api.com/)
