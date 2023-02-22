import time
import requests
from operator import itemgetter
from collections import OrderedDict
from resources.api.filters import filterKD, filterKills, filterPosition, lobbyColour, verifyLarge
from resources.api.processData import basicInfo, lifetimeKD, weeklyInfo, weeklyKD
from .guarsonapi import getLobbyFromApi


lastLobbyID = ''
lastLobby = ''

# LOGIN
def login():        # Login contra callofduty.com
    """
    cookie = {"ACT_SSO_COOKIE":os.getenv('sso_token')}
    try:
        resp = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/psn/gamer/Hormigator1/profile/type/wz', cookies=cookie, timeout=30).json()
        if resp['status'] == "error" and resp['data']['message'] == "Not permitted: not authenticated":     ##Consulto si no se pudo logear
            return "ERROR: 'Not permitted: not authenticated'\nCertificado vencido"
        else:
            return cookie
    except requests.exceptions.Timeout as err:
        return "ERROR TIMEOUT: al hacer loggin en cod api"
    """
    pass


# Modularizacion
def getLobbyIdCodApi(platform, user, cookie):  # Obtengo el ID de la ultima lobby desde la api de COD
    # NO FUNCIONA DESDE LOS CAMBIOS EN LA API QUE TIRA TIMEOUT Y UNAUTHENTICATED Y HAY QUE USAR LA API DE WZSTATS
    try:
        resp_lastMatches = requests.get('https://my.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/' + platform + '/gamer/' + user + '/matches/wz/start/0/end/0/details', cookies=cookie, params='1', timeout=30).json()
        return resp_lastMatches["data"]["matches"][0]["matchID"]
    except requests.exceptions.Timeout:
        return "ERROR TIMEOUT: al obtener la lista de partidas en cod api"
    except:
        return "ERROR: no se pudo obtener el ID de la partida desde 'my.callofduty.com'"


def getLobbyIdWZStats(platform, user):  # Obtengo el ID de la ultima lobby desde la api de WZSTATS
    try:
        resp_lastMatches = requests.get('https://app.wzstats.gg/v2/player/match/withPlayers/?username=' + user + '&platform=' + platform, timeout=30).json()
        return resp_lastMatches["matches"][0]["id"]
    except requests.exceptions.Timeout:
        return "ERROR TIMEOUT: al obtener la lista de partidas en wzstats.gg"
    except:
        return "ERROR: no se pudo obtener el ID de la partida desde 'wzstats.gg'"


def getLobbyInfo(lobbyId):  # Obtengo toda la informacion del lobby
    if "ERROR" in lobbyId:
        return lobbyId
    else:
        try:    # Intentar obtener la data de la ultima partida
            lobby = requests.get('https://app.wzstats.gg/v2/?matchId='+lobbyId, timeout=30).json()
        except requests.exceptions.Timeout:
            return "ERROR TIMEOUT: al obtener la partida en wzstats"
        except:     # Si no obtiene la data de la ultima partida arroja error
            return "ERROR: No se pudo conectar con wzstats.gg."

        jugadores = getLobbyFromApi(lobby["data"]["mode"]) + time.strftime('%d/%m/%Y %H:%M', time.localtime(lobby["data"]["startedAt"] - 10800)) + "hs\n\n-KD---KILLS---NAME\n\n"    # Obtengo la hora de la partida y le resto 3hs
        data = {}   # Estructura donde guardo la info de cada jugador. Dict
        prom = 0
        y = 0   # Contador
        sinkd = 0   # Contador de jugadores sin kd encontrados
        for _ in lobby["data"]["players"]:
            try:    # Intentar encontrar KD
                prom = prom + round(float(lobby["data"]["players"][y]["playerStat"]["lifetime"]["mode"]["br"]["properties"]["kdRatio"]), 2)  # Sumo el kd a un general para despues sacar promedio
                data[y] = "-" + filterKD(str(round(float(lobby["data"]["players"][y]["playerStat"]["lifetime"]["mode"]["br"]["properties"]["kdRatio"]), 2))) + "   "  # Dejo el kd prolijo
            except:     # Si no encuentra el kd le pone como 0.00
                data[y] = "-0.00   "
                sinkd += 1

            try:    # Esto es por si es un plunder o blood money que no tiene teamplacement
                data[y] = data[y] + filterKills(str(lobby["data"]["players"][y]["playerMatchStat"]["playerStats"]["kills"])) + lobby["data"]["players"][y]["playerMatchStat"]["player"]["username"] + filterPosition(lobby["data"]["players"][y]["playerMatchStat"]["playerStats"]["teamPlacement"])
            except:
                data[y] = data[y] + filterKills(str(lobby["data"]["players"][y]["playerMatchStat"]["playerStats"]["kills"])) + lobby["data"]["players"][y]["playerMatchStat"]["player"]["username"] + "\n"
            y += 1

        for key, value in OrderedDict(sorted(data.items(), key=itemgetter(1), reverse=True)).items():   # Itero por todos los jugadores
            jugadores = jugadores + value   # Guardo su info en string

        lastLobbyID = lobbyId
        lastLobby = verifyLarge(jugadores + "\n" + str(y) + " Jugadores\n" + "Promedio KD Lobby: " + filterKD(str(round((prom/(y-sinkd)), 2))) + "\n" + lobbyColour(round((prom/(y-sinkd)), 3)))   # Saco el promedio de todos los que tienen kd
        return lastLobby


def getLobbyTotalInfo(platform, name):  # Al metodo que obtiene toda la informacion le paso el resultado del metodo que obtiene el ID de la lobby
    lobbyID = getLobbyIdWZStats(platform, name)
    if lastLobbyID == lobbyID:  # Si el ID de la lobby es el mismo que consulte antes, devuelvo el mismo resultado que antes y ahorro una consulta
        return lastLobby
    return getLobbyInfo(lobbyID)
    """
    cookie = login()
    if cookie == "ERROR: 'Not permitted: not authenticated'\nCertificado vencido":
        return cookie
    else:
        return getLobbyInfo(getLobbyId(platform, name, cookie))
    """


def players_connected(resp_connected):  # Armo msj de conectados
    connected = "Amigos de Hormigator Conectados:\n\n"
    y = 0
    for _ in resp_connected["data"]["uno"]:
        if resp_connected["data"]["uno"][y]["status"]["online"] is True:
            connected = connected + "-" + resp_connected["data"]["uno"][y]["username"].split('#', 1)[0] + "\n"
        y += 1
    return connected


# INFORMACION DE JUGADORES
def info_Player(platform, username, name):  # Hago login y obtengo el perfil del jugador
    cookie = login()
    if cookie == "ERROR: 'Not permitted: not authenticated'\nCertificado vencido":
        return cookie
    else:
        try:
            resp_profile = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/'+platform+'/gamer/'+username+'/profile/type/wz', cookies=cookie, timeout=30)
            return basicInfo(resp_profile.json(), name) + weeklyInfo(resp_profile.json())
        except requests.exceptions.Timeout:
            return "ERROR TIMEOUT: al obtener el perfil en cod api"
        except:
            return "ERROR: no se pudo obtener el perfil del usuario"


def info_Player_kd(platform, username, name):  # Hago login y obtengo el perfil del jugador
    cookie = login()
    if cookie == "ERROR: 'Not permitted: not authenticated'\nCertificado vencido":
        return cookie
    else:
        try:
            resp_profile = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/'+platform+'/gamer/'+username+'/profile/type/wz', cookies=cookie, timeout=30)
            return name + "\n" + lifetimeKD(resp_profile.json()) + weeklyKD(resp_profile.json())
        except:
            return "ERROR: no se pudo obtener el perfil del usuario"


# AMIGOS CONECTADOS
def hormigator_friends():   # Hago login y accedo a la informacion de los amigos
    cookie = login()
    if cookie == "ERROR: 'Not permitted: not authenticated'\nCertificado vencido":
        return cookie
    else:
        try:
            resp_connected = requests.get('https://my.callofduty.com/api/papi-client/codfriends/v1/compendium', cookies=cookie, timeout=30).json()
            return players_connected(resp_connected)
        except requests.exceptions.Timeout:
            return "ERROR TIMEOUT: al obtener la lista de amigos en cod api"
        except:
            return "ERROR: no se pudo obtener el listado de amigos"


# DOLAR
def get_value_dolar():
    response = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales', timeout=30).json()
    return ("Dolar hoy: \n\n"
        + response[0]['casa']['nombre'] + ": " + response[0]['casa']['compra'] + " | " + response[0]['casa']['venta'] + "\n"
        + response[6]['casa']['nombre'] + ": " + response[6]['casa']['compra'] + " | " + response[6]['casa']['venta'] + "\n"
        + response[1]['casa']['nombre'] + ": " + response[1]['casa']['compra'] + " | " + response[1]['casa']['venta']
        )
