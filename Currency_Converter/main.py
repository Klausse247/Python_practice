import requests

def get_exchange_rates(base_currency):
    api_key = 'e442ebee578cb4713c79b140'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)
    
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data['conversion_rates'] # Return only the conversion rates dictionary
        else:
            print('error: ' , response.status_code)
            return None
    
    except requests.exceptions.RequestException as e:
    
        # Handle any network-related errors or exceptions
        print('Error: ', e)
        return None

def main():
    base_currency = input("Enter the base currency (e.g., USD, EUR): ").upper()
    rates = get_exchange_rates(base_currency)
    if rates is None:
        print("failed to retrieve excahnge rates!!!")
        return
    

    # Display available currencies as a comma-separated list
    print("These are the currencies you can exchange to:")
    print(", ".join(rates.keys()))
    print("\n")
    

    try:

        amount = float(input("Input the amount you want to convert EX(100): "))
        #currency_1 = (input("What is the base currency associated with the amount you put in (e.g., USD): ")).upper()
        currency_2 = (input("What is the currency you want to exchange to (e.g., EUR): ")).upper()

        #if base_currency != 'USD':
           # print("Currently, only USD is supported as the base currency.")
           # return

        # Perform the conversion
        if currency_2 in rates:
            converted_amount = amount * rates[currency_2]
            print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {currency_2}")
        else:
            print(f"Currency {currency_2} is not available.")
    
    except ValueError:
        print("Invalid amount entered.")

if __name__ == "__main__":
    main()