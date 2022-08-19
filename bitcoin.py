# Expects the user to specify as a command-line argument the number of Bitcoins that they would like to buy.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object.

import sys                          # for capturing sysargv and exiting
import requests                     # imports module for querying BitCoin info
import json                         # helps us process JSON info

def main():

# evaluates whether command-line arguments have been included and determines whether they can be converted to a float.

    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument.")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments.")
    elif len(sys.argv) == 2:
        try:
            user_amount = float(sys.argv[1])                                # stores desired amount of bitcoin in user_amount
        except ValueError:
            sys.exit("Command-line argument is not a number.")

    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')        # visits this URL and gets the associated JSON data, part of "requests" package
        o = response.json()                                                                 # decodes result into JSON

    except requests.exceptions.JSONDecodeError:
        print("Cannot retrieve data.")


    price = o["bpi"]["USD"]["rate_float"]                                               # finds current price of bitcoin in JSON file
    total_price = price * user_amount                                                   # total_price is the current bitcoin price * the number in user_amount
    print(f"${total_price:,.4f}")



main()






