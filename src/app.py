import telebot
import os
from music import descargar_musica
import time
from dotenv import load_dotenv
load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"), parse_mode=None)
telebot.apihelper.CONNECT_TIMEOUT = 60  # Aumenta el tiempo de espera de conexión
telebot.apihelper.READ_TIMEOUT = 60    # Aumenta el tiempo de espera de lectura
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
    ¡Hola! 👋 Soy YtdownMusic, tu bot genial para descargar tu música de YouTube. 
Escribe /help!
    """)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """\
    Envia el link de tu cancion para la descargar
    """)

@bot.message_handler(content_types=['text'])
def download(message):
    try:
        urlyt= ("https://youtu", "https://music.yout")
        if message.text.startswith(urlyt):
            msg = bot.reply_to(message, "Descargando..." \
            "\nEsto puede tardar un poco, por favor espera.")
            
            salida = descargar_musica(message.text)
            with open(salida, 'rb') as cancion:
                bot.send_chat_action(message.chat.id, 'upload_document')
                bot.send_document(message.chat.id, cancion)
            
            bot.delete_message(message.chat.id, msg.message_id)
            os.remove(salida)
        else:
            bot.reply_to(message, "La url no es valida, asegurate de que sea un link de youtube o este bien escrito.")
    except Exception as e:
        bot.reply_to(message, "Ocurrio un error: " + str(e))


bot.infinity_polling() 