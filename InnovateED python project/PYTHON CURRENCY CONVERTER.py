import requests

def currency_converter(amount, from_currency, to_currency):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your API key
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        response = requests.get(url)
        data = response.json()
        exchange_rate = data['rates'][to_currency]
        converted_amount = amount * exchange_rate
        return converted_amount
    except Exception as e:
        print("Error:", e)
        return None

def main():
    amount = float(input("Enter amount: "))
    from_currency = input("From currency: ").upper()
    to_currency = input("To currency: ").upper()

    converted_amount = currency_converter(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} equals {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()
