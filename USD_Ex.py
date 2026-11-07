"""Run the currency converter with illustrative rates as an offline fallback."""

from Currency_exchanger import main

# Fixed examples for practicing currency conversion without a connection.
BACKUP_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.77,
    "INR": 84.0,
    "CAD": 1.38,
    "AUD": 1.50,
    "JPY": 150.0,
}

if __name__ == "__main__":
    main(fallback_rates=BACKUP_RATES)
