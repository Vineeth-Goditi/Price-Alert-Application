API

import smtplib, ssl
from flask import Flask
app = Flask(Alert Creation)


@app.route('alerts/create/')
def main(Alert Creration(receiver_email=mail id)):

if __name__ == '__main__':
    app.run()

Crypto Currency


import requests
import time

# global variables
api_key = 'your_coinmarketcap_api_key'
bot_token = 'your_telegram_bot_token'
chat_id = 'your_telegram_account_chat_id_here'
threshold = 30000
time_interval = 5 * 60 # in seconds


def get_btc_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }
   
    # make a request to the coinmarketcap api
    response = requests.get(url, headers=headers)
    response_json = response.json()

    # extract the bitcoin price from the json data
    btc_price = response_json['data'][0]
    return btc_price['quote']['USD']['price']

# main fn
def Alert Creation:

    price_list = []

    # infinite loop
    while True:
        price = get_btc_price()
        price_list.append(price)

        # if the price falls below threshold, send an immediate msg
        if price < threshold:
            send_message(receiver_email=mail id)

        
            # empty the price_list
            price_list = []

# fancy way to activate the main() function
if __name__ == '__main__':
    main()

Mail

def Send_message(receiver_mail):
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = input("Type your password and press enter:")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message
