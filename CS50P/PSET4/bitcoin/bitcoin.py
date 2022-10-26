import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Example: bitcoin.py 1.5")

try:
    n = float(sys.argv[1])

except ValueError:
    sys.exit("Not a number")

try:

    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

except requests.RequestException:

    sys.exit("failed request")

#if you skip this step the response is just a string, must convert using json()

text = r.json()
prices = text["bpi"]
USD = prices["USD"]
rate = USD["rate_float"]

print(f"${(rate * n):,.4f}")