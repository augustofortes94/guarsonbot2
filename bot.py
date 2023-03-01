import os
import sys
import telegram
from dotenv import load_dotenv
from pathlib import Path
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from resources.commands.commandsMenu import *
from resources.commands.bonus import *
from resources.commands.botonera import *
from resources.commands.lobbys import *
from resources.commands.stats import *
from resources.commands.weapons import *


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

telegram_token = os.getenv('TELEGRAM_TOKEN')

if os.getenv('MODE') == "dev":
    # Acceso local
    def run(updater):
        updater.start_polling()
        print("CORRIENDO DESARROLLO...")
        updater.idle()  # permite finalizar el bot con ctrl+C

elif os.getenv('MODE') == "prod":
    # Acceso HEROKU (produccion)
    def run(updater):
        port = int(os.environ.get('PORT', '8443'))
        host_url = os.environ.get("HOST_URL")
        updater.start_webhook(listen="0.0.0.0", port=port, url_path=telegram_token, webhook_url= host_url + telegram_token)
        print("CORRIENDO PRODUCCION...")

else:
    defineLogs().info("ERROR: No se especifico el MODE")
    sys.exit

# Creo el bot con el token
if __name__ == "__main__":
    bot = telegram.Bot(token=telegram_token)

# Enlazamos el updater con el bot
updater = Updater(bot.token, use_context=True)

# Creamos un depachador
dp = updater.dispatcher

# LLAMADOS A COMANDOS #

# COMANDOS
dp.add_handler(CommandHandler("Armas", armas))

dp.add_handler(CommandHandler("Comandos", comandos))

dp.add_handler(CommandHandler("Hola", hola))


# ARMAS
dp.add_handler(CommandHandler("Bryson", bryson))

dp.add_handler(CommandHandler("Kastov", kastov))

dp.add_handler(CommandHandler("Lachmann", lachmann))

dp.add_handler(CommandHandler("Lockwood", lockwood))

dp.add_handler(CommandHandler("TAQ", taq))


# COMANDOS DINAMICOS
dp.add_handler(MessageHandler(Filters.regex(r"^/\w+$"), commandRegex))

# RUN
run(updater)
