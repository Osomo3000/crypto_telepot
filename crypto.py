import time
import telepot
import requests
import json

# Get data from Coingecko
r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cardano,safemoon,coti&vs_currencies=eur&include_market_cap=true")
wert = r.json()

# Get String-Value
cardano_string=(wert['cardano']['eur'])
safemoon_string=(wert['safemoon']['eur'])
coti_string=(wert['coti']['eur'])

# Parse from String to Float
cardano_komma = float(cardano_string)
safemoon_komma = float(safemoon_string)
coti_komma = float(coti_string)

# Set upper limit an lower limit
cardano_up = 2.03
cardano_down = 0.70

safemoon_up = 0.00001
safemoon_down = 0.000001

coti_up = 0.43
coti_down = 0.10

# Set API and ID credentials
chat_id = 'XX'
bot = telepot.Bot('XX')



def coins():
  bot.sendMessage(chat_id, "-----*Cardano*-----",parse_mode= 'Markdown')
  bot.sendMessage(chat_id, "Preis: " + "{0:.2f}".format(cardano_komma) + " EUR")
  time.sleep(1)
  bot.sendMessage(chat_id, "------*Safemoon*-----",parse_mode= 'Markdown')
  bot.sendMessage(chat_id, "Preis: " + "{0:.10f}".format(safemoon_komma) + " EUR")
  time.sleep(1)
  bot.sendMessage(chat_id, "------*Coti*-----",parse_mode= 'Markdown')
  bot.sendMessage(chat_id, "Preis: " + "{0:.2f}".format(coti_komma) + " EUR")



if ((cardano_komma >= cardano_up) or (safemoon_komma >= safemoon_up) or (coti_komma >= coti_up) ):
  bot.sendMessage(chat_id, "*Neues ATH!*",parse_mode= 'Markdown')
  bot.sendPhoto(chat_id, photo=open('rocket.png', 'rb'))
  coins()

elif ((cardano_komma <= cardano_down) or (safemoon_komma <= safemoon_down) or (coti_komma <= coti_down)):
  bot.sendMessage(chat_id, "*ACHTUNG!*",parse_mode= 'Markdown')
  bot.sendPhoto(chat_id, photo=open('achtung.png', 'rb'))
  coins()


