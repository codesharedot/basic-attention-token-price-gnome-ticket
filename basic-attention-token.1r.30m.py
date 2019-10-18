#!/usr/bin/env python
# How to use:
#  - Make sure the Argos shell extension (https://github.com/p-e-w/argos) is installed.
#  - Copy the `basic-attention-token.1r.30m.py` file to ~/.config/argos/
#  - Make the file executable
#  - Aaand that's it!

import requests
from datetime import datetime

def get_price():
    data = requests.get("https://api.coinmarketcap.com/v1/ticker/basic-attention-token/")
    price_str = data.json()[0]["price_usd"]
    price_trimmed = "{0:.2f}".format(float(price_str))
    price = float(price_trimmed)
    return price

print("BAT ${usb} | iconName=invest-applet".format(usb=get_price()))
print("---")
print("Last checked: " + datetime.now().strftime("%H:%M:%S"))
