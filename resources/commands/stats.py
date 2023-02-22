from resources.api.codapi import info_Player, info_Player_kd
from resources.commands.commandsMenu import defineLogs


# Stats
def bolsonaro(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bolsonaro")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player("psn", "agu_q1988", "El Peluca Milei"))


def bolsonarokd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Bolsonaro KD")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player_kd("psn", "agu_q1988", "El Peluca Milei"))


def elch000(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Elch000")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player("psn", "Elch000", "Berisso1"))


def elch000kd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Elch000 KD")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player_kd("psn", "Elch000", "Berisso1"))


def hormigator(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Hormigator")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player("psn", "Hormigator1", "Hormigator"))


def hormigatorkd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Hormigator KD")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player_kd("psn", "Hormigator1", "Hormigator"))


def leko(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Leko")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player("psn", "Aleko22lp", "Leko"))


def lekokd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Leko KD")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player_kd("psn", "Aleko22lp", "Leko"))


def luquitas(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Luquitas")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player("psn", "luquitasc70", "LuquitasC70"))


def luquitaskd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Luquitas KD")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player_kd("psn", "luquitasc70", "LuquitasC70"))


def mandalorian(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Mandalorian")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player("battle", "Mandalorian%2311726", "MandaloriaN"))


def mandaloriankd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Mandalorian KD")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player_kd("battle", "Mandalorian%2311726", "ElFisgonMorboson"))


def pablo(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Pablo")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player("psn", "carripablin10", "Carripablin10"))


def pablokd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Pablo KD")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player_kd("psn", "carripablin10", "Carripablin10"))


def rapax(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Rapax7")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player("battle", "rapax7%231438", "Rapax7"))


def rapaxkd(update, context):
    defineLogs().info(f"El usuario {update.effective_user['username']}, consulto por Rapax7 KD")
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_Player_kd("battle", "rapax7%231438", "Rapax7"))
