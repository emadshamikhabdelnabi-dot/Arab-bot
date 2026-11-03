import telebot
import time

TOKEN = "7904511568:AAH7t0hOe3O5p9pM7tV7h0Qj8k9l0m1n2o3p"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "أهلا بيك يا عماد! البوت شغال 24 ساعة ✅")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    bot.reply_to(m, f"استلمت: {m.text}")

print("Bot running...")
while True:
    try:
        bot.infinity_polling()
    except:
        time.sleep(5)
