import requests

# Дані для запитів
HEADERS = {
    "accept": "application/json",
    "Authorization": "12d1b934:b367a6686be9b284f9371e9dcc682640"
}

# Регіони: Київ (31) і Київська область (10)
REGIONS = {
    "Київ": 31,
    "Київська область": 10
}

def check_alarm(region_name, region_id):
    url = f"https://api.ukrainealarm.com/api/v3/alerts/{region_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"❌ Помилка запиту для {region_name}: {response.status_code}")
        return

    data = response.json()
    if not data or not isinstance(data, list):
        print(f"❌ Невірні дані для {region_name}")
        return

    region_data = data[0]
    last_update = region_data.get("lastUpdate", "Невідомо")
    active_alerts = region_data.get("activeAlerts", [])

    if active_alerts:
        print(f"🚨 Повітряна тривога у {region_name}! ({last_update})")
    else:
        print(f"✅ У {region_name} спокійно. ({last_update})")

# Перевірка обох регіонів
for name, id in REGIONS.items():
    check_alarm(name, id)