!pip3 install telebot
import requests
import json
import telebot

url = "https://session.coolmathblox.ca/launch/server_list"  # Подставь настоящий URL
headers = {
"User-Agent": "Mozilla/5.0",
"Accept": "application/json",
"Content-Type": "application/json",
"Authorization": "4408a4b92507ca5697bd66812a1f58e2"
}

TOKEN = '7827487706:AAF56HYqFnmylVIJVWTaoypJCZhIATdZBjs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: "/getworlds" in message.text.lower())
def getworlds(message):
response = requests.post(url, json={}, headers=headers)
data = response.json()

allplanets = data['servers']  # Полностью перезаписываем массив

# Сохраняем в JSON-файл
with open("data.json", "w", encoding="utf-8") as file:
json.dump(allplanets, file, ensure_ascii=False, indent=4)
bot.reply_to(message,"\n".join(allplanets["id"] for allplanets["id"] in allplanets))


bot.polling()
