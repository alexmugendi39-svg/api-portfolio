import requests

def get_rates():
    """Fetch live exchange rates with KES as base currency."""
    url = "https://open.er-api.com/v6/latest/KES"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["rates"], data["time_last_update_utc"]

def convert(amount_kes, rates):
    """Convert KES amount to major currencies."""
    return {
        "USD": amount_kes * rates["USD"],
        "EUR": amount_kes * rates["EUR"],
        "GBP": amount_kes * rates["GBP"],
        "UGX": amount_kes * rates["UGX"],
        "TZS": amount_kes * rates["TZS"],
    }

def main():
    print("=== KENYAN BUSINESS CURRENCY TRACKER ===")
    print("Live rates for businesses quoting international clients\n")

    try:
        rates, last_updated = get_rates()
        print(f"Rates last updated: {last_updated}\n")
    except Exception as e:
        print(f"Error: Could not fetch live rates. Check internet. ({e})")
        return

    try:
        amount_kes = float(input("Enter amount in KES: "))
    except ValueError:
        print("Please enter a valid number. Example: 50000")
        return

    converted = convert(amount_kes, rates)

    print(f"\nKES {amount_kes:,.2f} equals:")
    print(f"USD: ${converted['USD']:,.2f}")
    print(f"EUR: €{converted['EUR']:,.2f}")
    print(f"GBP: £{converted['GBP']:,.2f}")
    print(f"UGX: UGX {converted['UGX']:,.0f}")
    print(f"TZS: TZS {converted['TZS']:,.0f}")
    print("\nUse this quote for your international client.")

if __name__ == "__main__":
    main()