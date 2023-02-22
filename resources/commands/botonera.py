from telegram import KeyboardButton, ReplyKeyboardMarkup
from resources.api.codapi import getLobbyTotalInfo
from resources.commands.commandsMenu import armas, comandos, getListStats
from resources.commands.bonus import codsignal
from resources.commands.commandsMenu import defineLogs
from ..api.guarsonapi import getListCommands


# BOTONERA #
def botonera(update, context, text):      # Defino y creo los botones del chat
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por botonera")
    buttons = [[KeyboardButton("Armas")], [KeyboardButton("COD Señal")], [KeyboardButton("Comandos")], [KeyboardButton("Lobbys")]]  # , [KeyboardButton("Conectados")], [KeyboardButton("Lobbys")], [KeyboardButton("Stats")]]
    update.message.reply_text(str(text), reply_markup=ReplyKeyboardMarkup(buttons))


def botoneraAdapter(update, context):      # seteo el texto a enviar al crear la botonera
    botonera(update, context, "Botonera activa")


def botoneraLobbys(update, context):      # Defino y creo los botones del chat para las lobbys
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos de Lobbys")
    keyboar = ReplyKeyboardMarkup([[KeyboardButton("LobbyBolsonaro")], [KeyboardButton("LobbyHormigator")], [KeyboardButton("LobbyMandalorian")], [KeyboardButton("<--")]])
    keyboar.one_time_keyboard = True
    update.message.reply_text(getListCommands('Lobbys'), reply_markup=keyboar)


def botoneraStats(update, context):      # Defino y creo los botones del chat para las lobbys
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Comandos de Stats")
    keyboar = ReplyKeyboardMarkup([[KeyboardButton("Bolsonaro")], [KeyboardButton("Hormigator")], [KeyboardButton("Leko")], [KeyboardButton("Mandalorian")], [KeyboardButton("<--")]])
    keyboar.one_time_keyboard = True
    update.message.reply_text(getListStats(), reply_markup=keyboar)


# MANEJADOR DE MENSAJES #
def messageHandler(update, context):
    if "Armas" in update.message.text:
        return armas(update, context)

    if "COD Señal" in update.message.text:
        return codsignal(update, context)

    if "Comandos" in update.message.text:
        return comandos(update, context)

    if "Lobbys" in update.message.text:
        return botoneraLobbys(update, context)

    if "LobbyBerisso1" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Elch000")
        return botonera(update, context, getLobbyTotalInfo("psn", "Elch000"))

    if "LobbyBolsonaro" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Bolsonaro")
        return botonera(update, context, getLobbyTotalInfo("psn", "agu_q1988"))

    if "LobbyHormigator" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Hormigator")
        return botonera(update, context, getLobbyTotalInfo("psn", "Hormigator1"))

    if "LobbyLeko" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Leko")
        return botonera(update, context, getLobbyTotalInfo("psn", "Aleko22lp"))

    if "LobbyMandalorian" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Lobby Mandalorian")
        return botonera(update, context, getLobbyTotalInfo("battle", "Mandalorian%2311726"))

    if "<--" in update.message.text:
        return botonera(update, context, "back")

    """
    if "Conectados" in update.message.text:
        return conectados(update, context)

    if "Stats" in update.message.text:
        return botoneraStats(update, context)

    if "Berisso1" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Elch000")
        return botonera(update, context, info_Player("psn", "Elch000", "Berisso1"))

    if "Bolsonaro" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bolsonaro")
        return botonera(update, context, info_Player("psn", "agu_q1988", "El Peluca Milei"))

    if "Hormigator" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Hormigator")
        return botonera(update, context, info_Player("psn", "Hormigator1", "Hormigator"))

    if "Leko" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Leko")
        return botonera(update, context, info_Player("psn", "Aleko22lp", "Leko"))

    if "Mandalorian" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Mandalorian")
        return botonera(update, context, info_Player("battle", "Mandalorian%2311726", "ElFisgonMorboson"))

    if "BolsonaroKD" == update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bolsonaro KD")
        return botonera(update, context, info_Player_kd("psn", "agu_q1988", "El Peluca Milei"))

    if "HormigatorKD" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Hormigator KD")
        return botonera(update, context, info_Player_kd("psn", "Hormigator1", "Hormigator"))

    if "LekoKD" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Leko KD")
        return botonera(update, context, info_Player_kd("psn", "Aleko22lp", "Leko"))

    if "MandalorianKD" in update.message.text:
        defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Mandalorian KD")
        return botonera(update, context, info_Player_kd("battle", "Mandalorian%2311726", "ElFisgonMorboson"))
    """
