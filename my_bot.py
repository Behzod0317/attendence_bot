import telebot
import csv
from datetime import datetime

bot = telebot.TeleBot('Your token')

messages = {}  # Dictionary to store user messages

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Ilova ishga tushdi.")

@bot.message_handler(commands=['hisob'])
def save_messages(message):
    user_id = message.from_user.id
    if user_id not in messages:
        bot.send_message(message.chat.id, "")
        return

    with open('davomad.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter='.')
        info = messages[user_id]
        current_date = datetime.now().strftime("%Y-%m-%d")
        username = message.from_user.username
        writer.writerow([current_date, username, info['arriving_time'], info['leaving_time']])
    
    messages.pop(user_id)
    bot.send_document(message.chat.id, open('davomod.csv', 'rb'))

#
bot.infinity_polling()
