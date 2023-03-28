import requests, sys, json


try:
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    user = float(sys.argv[1])
    r = data["bpi"]["EUR"]["rate_float"]*(user)
    print(f"{r:,.4f}")
except requests.RequestException:
    sys.exit("Incorrect sys argument")

