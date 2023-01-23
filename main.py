import requests
import json
import telebot
from telebot import TeleBot

bot = telebot.TeleBot("5887260814:AAGRMeQwwq-HEoKYBmC0kgDSAfZijdl_tzw")

MyDictionary = {
    "/eur": "EUR",
    "/usd": "USD",
    "/ron": "RON",
}

class ConvertionException():
    pass

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "For new operation type : /conversion"
    bot.reply_to(message, text)

@bot.message_handler(commands=['conversion'])
def operation(message: telebot.types.Message):
    text = 'Actual currency: \n /pln_to_usd \n /pln_to_ron \n ' \
           '/pln_to_eur \n /usd_to_pln \n /ron_to_pln \n /eur_to_pln'

    r1 = requests.get(
        'https://api.nbp.pl/api/exchangerates/rates/a/eur')
    texts1 = json.loads(r1.content)
    Rates1 = texts1.get('rates')
    EUR1 = str(Rates1[0].get('mid'))

    r2 = requests.get(
        'https://api.nbp.pl/api/exchangerates/rates/a/usd')
    texts2 = json.loads(r2.content)
    Rates2 = texts2.get('rates')
    USD1 = str(Rates2[0].get('mid'))

    r3 = requests.get(
        'https://api.nbp.pl/api/exchangerates/rates/a/ron')
    texts3 = json.loads(r3.content)
    Rates3 = texts3.get('rates')
    RON1 = str(Rates3[0].get('mid'))

    MyDictionary = {
        "/eur": "",
        "/usd": "",
        "/ron": "",
    }
    MyDictionary["eur"] = EUR1
    MyDictionary["usd"] = USD1
    MyDictionary["ron"] = RON1
    for key in MyDictionary.keys():
        text = '\n'.join((text, key, "->", MyDictionary[key]))
    bot.reply_to(message, text)

@bot.message_handler(commands=['pln_to_usd'])
def pln_to_usd(message):
    bot.send_message(message.chat.id, "Type how many pln you want to convert to usd: ")
    @bot.message_handler(content_types=['text'])
    def pln_usd(message):
        r = requests.get(
            'https://api.nbp.pl/api/exchangerates/rates/a/usd')
        texts = json.loads(r.content)
        Rates = texts.get('rates')
        USD = Rates[0].get('mid')
        amount = int(message.text)
        total = round((amount / USD), 2)
        result = f'{amount} pln {total} usd'
        if type(amount) == str:
            raise ConvertionException(f'Did not manage to convert {amount}')
        bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['pln_to_ron'])
def pln_to_ron(message):
    bot.send_message(message.chat.id, "Type how many pln you want to convert to ron: ")
    @bot.message_handler(content_types=['text'])
    def pln_ron(message):
        r = requests.get(
            'https://api.nbp.pl/api/exchangerates/rates/a/ron')
        texts = json.loads(r.content)
        Rates = texts.get('rates')
        RON = Rates[0].get('mid')
        amount = int(message.text)
        total = round((amount / RON), 2)
        result = f'{amount} pln {total} ron'
        if type(amount) == str:
            raise ConvertionException(f'Did not manage to convert {amount}')
        bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['pln_to_eur'])
def pln_to_eur(message):
    bot.send_message(message.chat.id, "Type how many pln you want to convert to eur: ")
    @bot.message_handler(content_types=['text'])
    def pln_eur(message):
        r = requests.get(
            'https://api.nbp.pl/api/exchangerates/rates/a/eur')
        texts = json.loads(r.content)
        Rates = texts.get('rates')
        EUR = Rates[0].get('mid')
        amount = int(message.text)
        total = round((amount / EUR), 2)
        result = f'{amount} pln {total} eur'
        if type(amount) == str:
            raise ConvertionException(f'Did not manage to convert {amount}')
        bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['usd_to_pln'])
def usd_to_pln(message):
    bot.send_message(message.chat.id, "Type how many usd you want to convert to pln: ")
    @bot.message_handler(content_types=['text'])
    def usd_pln(message):
        r = requests.get(
            'https://api.nbp.pl/api/exchangerates/rates/a/usd')
        texts = json.loads(r.content)
        Rates = texts.get('rates')
        USD = Rates[0].get('mid')
        amount = int(message.text)
        total = round((amount * USD), 2)
        result = f'{amount} usd {total} pln'
        if type(amount) == str:
            raise ConvertionException(f'Did not manage to convert {amount}')
        bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['ron_to_pln'])
def ron_to_pln(message):
    bot.send_message(message.chat.id, "Type how many ron you want to convert to pln: ")
    @bot.message_handler(content_types=['text'])
    def ron_pln(message):
        r = requests.get(
            'https://api.nbp.pl/api/exchangerates/rates/a/ron')
        texts = json.loads(r.content)
        Rates = texts.get('rates')
        RON = Rates[0].get('mid')
        amount = int(message.text)
        total = round((amount * RON), 2)
        result = f'{amount} ron {total} pln'
        if type(amount) == str:
            raise ConvertionException(f'Did not manage to convert {amount}')
        bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['eur_to_pln'])
def eur_to_pln(message):
    bot.send_message(message.chat.id, "Type how many eur you want to convert to pln: ")
    @bot.message_handler(content_types=['text'])
    def eur_pln(message):
        r = requests.get(
            'https://api.nbp.pl/api/exchangerates/rates/a/eur')
        texts = json.loads(r.content)
        Rates = texts.get('rates')
        EUR = Rates[0].get('mid')
        amount = int(message.text)
        total = round((amount * EUR), 2)
        result = f'{amount} eur {total} pln'
        if type(amount) == str:
            raise ConvertionException(f'Did not manage to convert {amount}')
        bot.send_message(message.chat.id, result)

bot.polling(none_stop=True)