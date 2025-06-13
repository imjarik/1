import requests
import telebot
from telebot import types
import time

# ====== Налаштування ======
BOT_TOKEN = "7699057429:AAFRiJevrsiiymWwlW_4OW_qcFVsAz_Eedc"
ALERT_API_URL = "https://api.ukrainealarm.com/api/v3/alerts/31"
ALERT_API_KEY = "12d1b934:b367a6686be9b284f9371e9dcc682640"

bot = telebot.TeleBot(BOT_TOKEN)

def get_alert_message():
    headers = {
        "accept": "application/json",
        "Authorization": ALERT_API_KEY
    }

    try:
        response = requests.get(url=ALERT_API_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"[ERROR] API запит: {e}")
        return " Не вдалося отримати дані з сервера тривог."

    if not data or not isinstance(data, list):
        return " Невірний формат даних з API."

    region_data = data[0]
    region = region_data.get("regionName", "Невідомо")
    active_alerts = region_data.get("activeAlerts", [])

    if active_alerts:
        return f" Повітряна тривога у регіоні: {region}!"
    else:
        return f" У регіоні {region} спокійно."

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Повітряна тривога")
    keyboard.add(button)
    bot.send_message(
        message.chat.id,
        "Привіт! Натисни кнопку нижче, щоб дізнатись про тривогу.",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: message.text == "Повітряна тривога")
def handle_alert(message):
    try:
        result = get_alert_message()
        bot.send_message(message.chat.id, result)
    except Exception as e:
        bot.send_message(message.chat.id, " Сталася помилка.")
        print(f"[handle_alert error] {e}")

if __name__ == "__main__":
    while True:
        try:
            print(" Бот запущено.")
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print(f"[ERROR] Бот впав: {e}")
            time.sleep(5)  # Затримка перед перезапуском