"""Convert currencies using the latest USD-based rates from ExchangeRate-API."""

import json
import math
from urllib.request import urlopen

API_URL = "https://open.er-api.com/v6/latest/USD"


def get_rates():
    """Fetch and validate the provider's latest daily exchange rates."""
    try:
        with urlopen(API_URL, timeout=5) as response:
            data = json.load(response)

        if data["result"] != "success" or data["base_code"] != "USD":
            raise ValueError("Unexpected exchange-rate response")

        rates = data["rates"]
        if rates["USD"] != 1 or not all(
            type(rate) in (int, float) and math.isfinite(rate) and rate > 0
            for rate in rates.values()
        ):
            raise ValueError("Invalid exchange rates")

        return rates
    except (OSError, ValueError, TypeError, KeyError, OverflowError):
        return {}


def convert(amount, from_rate, to_rate):
    """Convert through USD using two rates quoted per US dollar."""
    return (amount / from_rate) * to_rate


def main(fallback_rates=None):
    print("Loading exchange rates from ExchangeRate-API...")
    rates = get_rates()
    if rates:
        print("Using the provider's latest daily rates.")
    elif fallback_rates:
        rates = fallback_rates
        print("Rates unavailable. Using illustrative offline rates.")
    else:
        print("Could not load exchange rates. Please try again later.")
        return

    print("Available codes:", ", ".join(sorted(rates)))
    try:
        while True:
            base = input("\nFrom currency (or 'exit'): ").strip().upper()
            if base == "EXIT":
                break
            if base not in rates:
                print("Invalid source currency code.")
                continue

            target = input("To currency: ").strip().upper()
            if target not in rates:
                print("Invalid target currency code.")
                continue

            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            result = convert(amount, rates[base], rates[target])
            if not math.isfinite(result):
                print("Please enter an amount within the supported numeric range.")
                continue

            print(f"{amount:,} {base} = {result:,.2f} {target}")
    except (EOFError, KeyboardInterrupt):
        print()

    print("Goodbye!")


if __name__ == "__main__":
    main()
