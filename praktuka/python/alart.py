import requests


def is_alert_active():
    url = "https://api.ukrainealarm.com/api/v3/alerts/31"
    headers = {
        "accept": "application/json",
        "Authorization": "12d1b934:b367a6686be9b284f9371e9dcc682640"
    }
    response = requests.get(url=url, headers=headers)

    if response.status_code != 200:
        print(f"Помилка запиту: {response.status_code}")
        exit()
    return response

response = is_alert_active()

data = response.json()

# Очікуємо список з одним елементом
if not data or not isinstance(data, list):
    print("Невірний формат даних")
    exit()

kyiv_data = data[0]
region = kyiv_data.get("regionName", "Невідомо")
last_update = kyiv_data.get("lastUpdate", "Невідомо")
active_alerts = kyiv_data.get("activeAlerts", [])


if active_alerts:
    print(f"🚨 Повітряна тривога у регіоні: {region}! ")
else:
    print(f"✅ У регіоні {region} спокійно.")

