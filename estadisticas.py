def cant_tipo_viaje(tipo_viaje, tipo):
    if tipo_viaje == tipo:
        contar = 1
    else:
        contar = 0
    return contar

def acumular_presupuesto(acu_presupuesto, presupuesto):
    total = acu_presupuesto + presupuesto
    return total

def obtener_maximo(maximo, presupuesto):
    if maximo is None or presupuesto > maximo:
        maximo = presupuesto
    return maximo

def obtener_minimo(minimo, presupuesto):
    if minimo is None or presupuesto < minimo:
        minimo = presupuesto
    return minimo

def calcular_estadisticas(lista_usuarios):
    stats = {
        "usuarios_ingresados": len(lista_usuarios),
        "total_presupuesto": 0,
        "pres_avion": 0,
        "pres_auto": 0,
        "pres_colectivo": 0,
        "max_sur": None,
        "max_norte": None,
        "max_central": None,
        "min_sur": None,
        "min_norte": None,
        "min_central": None,
        "porc_avion": 0.0,
        "porc_auto": 0.0,
        "porc_colectivo": 0.0,
        "promedio": 0.0
    }

    for usuario in lista_usuarios:
        presupuesto = usuario["datos_necesarios_stats"]["presupuesto"]
        zona = usuario["datos_necesarios_stats"]["zona"]
        tipo_viaje = usuario["datos_necesarios_stats"]["tipo_viaje"]

        stats["total_presupuesto"] = acumular_presupuesto(stats["total_presupuesto"], presupuesto)

        stats["pres_avion"] += cant_tipo_viaje(tipo_viaje, 'Avión')
        stats["pres_auto"] += cant_tipo_viaje(tipo_viaje, 'Auto')
        stats["pres_colectivo"] += cant_tipo_viaje(tipo_viaje, 'Colectivo')

        if zona == "Zona Sur":
            stats["max_sur"] = obtener_maximo(stats["max_sur"], presupuesto)
            stats["min_sur"] = obtener_minimo(stats["min_sur"], presupuesto)
        elif zona == "Zona Norte":
            stats["max_norte"] = obtener_maximo(stats["max_norte"], presupuesto)
            stats["min_norte"] = obtener_minimo(stats["min_norte"], presupuesto)
        elif zona == "Zona Central":
            stats["max_central"] = obtener_maximo(stats["max_central"], presupuesto)
            stats["min_central"] = obtener_minimo(stats["min_central"], presupuesto)

    if stats["usuarios_ingresados"] > 0:
        stats["porc_avion"] = (stats["pres_avion"] / stats["usuarios_ingresados"]) * 100
        stats["porc_auto"] = (stats["pres_auto"] / stats["usuarios_ingresados"]) * 100
        stats["porc_colectivo"] = (stats["pres_colectivo"] / stats["usuarios_ingresados"]) * 100
        stats["promedio"] = stats["total_presupuesto"] / stats["usuarios_ingresados"]

    return stats