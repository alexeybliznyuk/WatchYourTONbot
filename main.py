import telebot
import requests
from config import tg_bot_api, crypto_ask_api




bot = telebot.TeleBot(tg_bot_api)

CoinAPI = crypto_ask_api

url = "https://rest.coinapi.io/v1/exchangerate/TON/USD"
headers = {
    "X-CoinAPI-Key": CoinAPI 
}





@bot.message_handler(commands=['start'])
def starting(message):
    bot.send_message(message.chat.id, f"Sup, {message.from_user.first_name} {message.from_user.last_name}! Dats WatchYourTONbot. It shows info bout TON n stuff.")
#    bot.send_message(message.chat.id, message.json)

@bot.message_handler(commands=['TON'])
def main(message):
    rateinjson = requests.get(url, headers=headers)
    rateinfo = rateinjson.json()
#    bot.send_message(message.chat.id, f"{rateinfo}")
    bot.send_message(message.chat.id, f"Now {rateinfo['asset_id_base']} is {rateinfo['rate']} {rateinfo['asset_id_quote']}")






bot.polling(none_stop=True)
