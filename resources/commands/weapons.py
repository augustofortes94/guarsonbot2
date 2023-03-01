from resources.commands.commandsMenu import defineLogs
from ..api.guarsonapi import getWeaponFromApi

def bryson(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bryson")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bryson:\n\n-Para las escopetas Bryson:\n-/Bryson800\n-/Bryson890")

def kastov(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Kastov")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Kastov:\n\n-Para los Fusiles de Asalto Kastov:\n-/Kastov545\n-/Kastov74\n-/Kastov762")

def lachmann(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lachmann")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Lachmann:\n\n-Para el Fusil de Asalto Lachmann /Lachmann556\n-Para el Fusil de Combate Lachmann /Lachmann762\n-Para el Subfusil Lachmann /LachmannSub")

def lockwood(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lockwood")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Lockwood:\n\n-Para la Escopeta Lockwood /Lockwood300\n-Para el Fusil Tactico Lockwood /MK2")

def taq(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por TAQ")
    context.bot.send_message(chat_id=update.effective_chat.id, text="TAQ:\n\n-Para el Fusil de Asalto TAQ /TAQ56\n-Para el Fusil de Combate TAQ /TAQV\n-Para el Fusil Tactico TAQ /TAQM")
