import telebot
import requests
import telebot
from telebot import types
import alart

bot = telebot.TeleBot("7699057429:AAFRiJevrsiiymWwlW_4OW_qcFVsAz_Eedc")

@bot.message_handler(commands=['start'])
def start(message):
    murksup = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton("Повітряна тривога")
    murksup.add(btn)
    bot.send_message(message.chat.id, "Привіт!", reply_markup=murksup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Повітряна тривога":
        response = alart.is_alert_active()
        data = response.json()
        
    if response.status_code != 200:
        print(f"Помилка запиту: {response.status_code}")
        exit()
    
    else:
        if not data or not isinstance(data, list):
            bot.send_message(message.chat.id, "Невірний формат даних")
            return

        kyiv_data = data[0]
        region = kyiv_data.get("regionName", "Невідомо")
        last_update = kyiv_data.get("lastUpdate", "Невідомо")
        active_alerts = kyiv_data.get("activeAlerts", [])

        if active_alerts:
            bot.send_message(message.chat.id, f"🚨 Повітряна тривога y регіоні: {region}! ")
        else:
            bot.send_message(message.chat.id, f"✅ У регіоні {region} спокійно.")
        return on_click
        
        
    
    
    
    
    
    
    
bot.polling(none_stop=True)