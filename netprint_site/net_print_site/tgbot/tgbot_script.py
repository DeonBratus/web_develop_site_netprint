import telebot
import sqlite3
import time

bot = telebot.TeleBot('6434629302:AAEpVlT29pZfY3kryTMnYOnk2SYjFFhiFw0')

last_processed_user_id = 0  # Initialize with a value that will not match any user_id initially

def create_message(last_data):
    user_id, name, number, mail, socnets, disc = last_data[0], last_data[1], last_data[2], last_data[3], last_data[4], last_data[5]
    text = f" НОВЫЙ ЗАКАЗ!\n Заказ №{user_id}\n Кто: {name}\n Описание:\n {disc}"
    return text

def send_message(message_text):
    # Here you can use different methods to send notifications, such as sending to your Telegram account.
    # Example using print for debugging:
    time.sleep(0.5)
    bot.send_message('1022445569', message_text)


def check_database():
    global last_processed_user_id
    while True:
        conn = sqlite3.connect("../db.sqlite3")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM main_offers')
        data = cursor.fetchall()
        conn.close()

        if data:
            last_data = data[-1]
            user_id = last_data[0]
            if user_id != last_processed_user_id:
                last_processed_user_id = user_id
                message_text = create_message(last_data)
                send_message(message_text)
            else:
                print("No new data in the database.")
        else:
            print("The database is empty.")

        time.sleep(1)  # Wait for 1 second before checking the database again

check_database()
# Start the bot
bot.polling(none_stop=True)
