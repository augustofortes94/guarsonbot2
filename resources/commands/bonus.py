from resources.api.codapi import get_value_dolar, hormigator_friends
from resources.commands.commandsMenu import defineLogs


# BONUS
def botrapido(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por botrapido")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Tranquilo a mi no me apures que no soy tu sirviente, pelotudo")


def botconchatumadre(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por botconchatumadre")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Que te pasa boludo?")


def codsignal(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por COD")
    context.bot.send_photo(update.message.chat.id, photo='https://drive.google.com/file/d/1EZYtZdUJqdGddTEX_H7SdrrgMpimgZ8j/view?usp=sharing', caption="Vamo a juga?")


def conectados(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Conectados")
    context.bot.send_message(chat_id=update.effective_chat.id, text=hormigator_friends())


def dolar(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Dolar")
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_value_dolar())


# Documentacion https://docs.python-telegram-bot.org/en/stable/telegram.bot.html#telegram.Bot
def fortnite(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Fortnite")
    update.message.bot.send_animation(update.message.chat.id, animation='https://c.tenor.com/4gPD1ccxrVgAAAAC/rick-ashley-dance.gif', caption="Sale ese Fortnite?")
