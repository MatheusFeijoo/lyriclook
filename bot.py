import telebot
from telebot import types
import time
from coletando_info import pega


bot_token = "795674646:AAHY7s8Xetv-XZK8HKtTQGnzdG2_cL6NDII"

bot = telebot.TeleBot(token=bot_token)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.music = None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Hi if you want me to search for a music lyric type /music
For more informations type /help

This bot was developed by @matheusfeijoo
Feel free to send your feedback :)
You can see the code of this bot in https://github.com/MatheusFeijoo/lyriclook
""")

@bot.message_handler(commands=['help'])
def send_help(message):
    message = bot.reply_to(message, """\
Hi if you want me to search for a music lyric type /music

------- OMG YOU CAN'T FIND THE LYRICS -------
I know I know, I'm not perfect, yet!
I use a brazilian website to search the lyrics, and sometimes they don't use the same name of the music.
A example is with the artist Passenger, they saved as The Passenger Reino Unido, wich is a bit strange.

Another example is with feat.
You need to write the feat in the music. For exemple: Princess of China feat. Rihanna
---------------------------------------------

This bot was developed by @matheusfeijoo
Feel free to send your feedback :)
You can see the code of this bot in https://github.com/MatheusFeijoo/lyriclook
""")


@bot.message_handler(commands=['music'])
def send_music(message):
    msg = bot.reply_to(message, """\
From which artist?
""")
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Which music?')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'Something went wrong! Need to start again with /music')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        music = message.text
        user = user_dict[chat_id]
        user.music = music
        chat_id = message.chat.id
        lyrics = pega(user.name, user.music)
        bot.send_message(chat_id, lyrics)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Sorry I am not perfect yet. \n You can Try again with /music')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.polling()