import sys
import requests

def main():
    no_of_bitcoins = convert_to_float()
    url_for_bitcoin = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = get_json_object(url_for_bitcoin)
    rate_float = get_price_from_json_response(response)
    total_cost = no_of_bitcoins * rate_float
    print(f"${total_cost:,.4f}")

def convert_to_float():
    try:
        if len(sys.argv) == 1:
            sys.exit("Missing command-line argument")
        num = float(sys.argv[1])
        return num
    except ValueError:
        sys.exit("Command-line argument is not a number")

def get_json_object(url_for_bitcoin):
    try:
        response = requests.get(url_for_bitcoin)
        response.raise_for_status()
        return response
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

def get_price_from_json_response(response):
    try:
        data = response.json()
        rate_float = data["bpi"]["USD"]["rate_float"]
        return rate_float
    except (KeyError, ValueError, TypeError):
        sys.exit("Error parsing Bitcoin price")

if __name__ == "__main__":
    main()
