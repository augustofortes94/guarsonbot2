# FILTERS


def filterKD(kd):       # Si el kd del jugador es por ejemplo 1.7 le agrego un 0 al final
    if len(kd) == 3:
        return kd + "0"
    else:
        return kd


def filterKills(kills):     # Si hace menos de 10 kills sumo un espacio para que quede el texto parejo
    if len(kills) == 1:
        return "| " + kills + "    "
    else:
        return "|" + kills + "   "


def filterPosition(pos):        # Si es el que gano, lo marco como 1°
    if pos == 1:
        return "    1°\n"
    else:
        return "\n"


def lobbyColour(kdProm):    # Segun el kd indico el color de la lobby
    if kdProm >= 1.14:
        return "Diamante 1"

    elif kdProm >= 1.113 and kdProm < 1.14:
        return "Diamante 2"

    elif kdProm >= 1.095 and kdProm < 1.113:
        return "Diamante 3"

    elif kdProm >= 1.078 and kdProm < 1.095:
        return "Diamante 4"

    elif kdProm >= 1.06 and kdProm < 1.078:
        return "Platino 1"

    elif kdProm >= 1.04 and kdProm < 1.06:
        return "Platino 2"

    elif kdProm >= 1.012 and kdProm < 1.04:
        return "Platino 3"

    elif kdProm >= 0.974 and kdProm < 1.012:
        return "Platino 4"

    elif kdProm >= 0.936 and kdProm < 0.974:
        return "Oro 1"

    elif kdProm >= 0.907 and kdProm < 0.936:
        return "Oro 2"

    elif kdProm >= 0.884 and kdProm < 0.907:
        return "Oro 3"

    elif kdProm >= 0.865 and kdProm < 0.884:
        return "Oro 4"

    elif kdProm >= 0.845 and kdProm < 0.865:
        return "Plata 1"

    elif kdProm >= 0.822 and kdProm < 0.845:
        return "Plata 2"

    elif kdProm >= 0.792 and kdProm < 0.822:
        return "Plata 3"

    elif kdProm >= 0.743 and kdProm < 0.792:
        return "Plata 4"

    elif kdProm >= 0.671 and kdProm < 0.743:
        return "Bronce 1"

    elif kdProm >= 0.619 and kdProm < 0.671:
        return "Bronce 2"

    elif kdProm >= 0.578 and kdProm < 0.619:
        return "Bronce 3"

    elif kdProm < 0.578:
        return "Bronce 4"

    else:
        return "ERROR"


def lobbyColourTable():     # Indico los kd y porcentajes de cada color de lobby
    return "TABLA DE LOBBYS POR COLOR\n\n---COLOR--------RANK---RANGO KD-\n\n-DIAMANTE 1  |95%|   1.14 -> 1.19\n-DIAMANTE 2  |90%|   1.11 -> 1.14\n-DIAMANTE 3  |85%|   1.09 -> 1.11\n-DIAMANTE 4  |80%|   1.07 -> 1.09\n-PLATINO 1      |75%|   1.06 -> 1.07\n-PLATINO 2      |70%|   1.04 -> 1.06\n-PLATINO 3      |65%|   1.01 -> 1.04\n-PLATINO 4      |60%|   0.97 -> 1.01\n-ORO 1               |55%|   0.93 -> 0.97\n-ORO 2               |50%|   0.90 -> 0.93\n-ORO 3               |45%|   0.88 -> 0.90\n-ORO 4               |40%|   0.86 -> 0.88\n-PLATA 1           |35%|   0.84 -> 0.86\n-PLATA 2           |30%|   0.82 -> 0.84\n-PLATA 3           |25%|   0.79 -> 0.82\n-PLATA 4           |20%|   0.74 -> 0.79\n-BRONCE 1       |15%|   0.67 -> 0.74\n-BRONCE 2       |10%|   0.61 -> 0.67\n-BRONCE 3       |05%|   0.57 -> 0.61\n-BRONCE 4       |00%|   0.52 -> 0.57"


def verifyLarge(result):    # Verifico el largo del mensaje ya que telegram solo permite mensajes hasta 4096 caracteres de largo
    if len(result) > 4096:
        return "ERROR: Mensaje demasiado largo > 4096"
    else:
        return result
