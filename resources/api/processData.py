from resources.api.filters import filterKD

# PROCESS JSON DATA


def basicInfo(respuesta, name):   # Creo el string con la informacion basica
    return (name
            + ":\n\n-Nombre: " + respuesta["data"]["username"]
            + "\n-Nivel: " + str(int(respuesta["data"]["level"]))
            + "\n-Wins: " + str(int(respuesta["data"]["lifetime"]["mode"]["br"]["properties"]["wins"]))
            + "\n" + lifetimeKD(respuesta)
            )


def lifetimeKD(respuesta):
    return ("\n-Kills: " + str(int(respuesta["data"]["lifetime"]["mode"]["br"]["properties"]["kills"]))
            + "\n-Deaths: " + str(int(respuesta["data"]["lifetime"]["mode"]["br"]["properties"]["deaths"]))
            + "\n-KD general: " + filterKD(str(round(float(respuesta["data"]["lifetime"]["mode"]["br"]["properties"]["kdRatio"]), 2)))
            + "\n-KD especifico: " + str(round(float(respuesta["data"]["lifetime"]["mode"]["br"]["properties"]["kdRatio"]), 5))
            )


def weeklyInfo(respuesta):  # Creo el string con la informacion semanal
    try:
        return (weeklyKD(respuesta)
                + "\n-Headshot Porcentaje: " + str(int(round(float(respuesta["data"]["weekly"]["all"]["properties"]["headshotPercentage"]), 2)*100)) + "%"
                + weeklyModeKD(respuesta)
                + "\n-Horas: " + str(int(respuesta["data"]["weekly"]["all"]["properties"]["timePlayed"]/3600)) + "hs"
                + "\n-Partidas: " + str(int(respuesta["data"]["weekly"]["all"]["properties"]["matchesPlayed"]))
                )
    except:
        return "\n\nSemanal:\nEl jugador lleva mas de una semana sin jugar"


def weeklyKD(respuesta):
    try:
        return ("\n\nSemanal:\n"
                + "\n-Kills: " + str(int(respuesta["data"]["weekly"]["all"]["properties"]["kills"]))
                + "\n-Deaths: " + str(int(respuesta["data"]["weekly"]["all"]["properties"]["deaths"]))
                + "\n-KD: " + str(round(float(respuesta["data"]["weekly"]["all"]["properties"]["kdRatio"]), 2))
                )
    except:
        return "\n\nSemanal:\nEl jugador lleva mas de una semana sin jugar"


def weeklyModeKD(respuesta):
    kdsByMode = "\n"
    try:
        kdsByMode = kdsByMode + "\n-KD Solos: " + str(round(float(respuesta["data"]["weekly"]["mode"]["br_brsolo"]["properties"]["kdRatio"]), 2))
    except:
        pass
    try:
        kdsByMode = kdsByMode + "\n-KD Duos: " + str(round(float(respuesta["data"]["weekly"]["mode"]["br_brduos"]["properties"]["kdRatio"]), 2))
    except:
        pass
    try:
        kdsByMode = kdsByMode + "\n-KD Trios: " + str(round(float(respuesta["data"]["weekly"]["mode"]["br_brtrios"]["properties"]["kdRatio"]), 2))
    except:
        pass
    try:
        kdsByMode = kdsByMode + "\n-KD Cuartetos: " + str(round(float(respuesta["data"]["weekly"]["mode"]["br_brquads"]["properties"]["kdRatio"]), 2))
    except:
        pass
    return kdsByMode + "\n"
