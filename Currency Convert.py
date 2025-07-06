import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    data = response.json()

    if to_currency.upper() in data["rates"]:
        rate = data["rates"][to_currency.upper()]
        converted = amount * rate
        print(f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
    else:
        print("❌ Currency not supported.")

# Main
print("💱 Currency Converter")
from_curr = input("From currency (e.g. USD): ")
to_curr = input("To currency (e.g. PKR): ")
amt = float(input("Amount: "))
convert_currency(from_curr, to_curr, amt)
