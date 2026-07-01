
def filtrar_y_reducir_presupuesto(lista_usuarios, condicion_zona, funcion_reductora):
    """
    Función Genérica y Reutilizable.
    Aplica Parametrización de comportamientos al recibir 'condicion_zona' 
    y 'funcion_reductora' como funciones de primer orden.
    Reduce drásticamente el código repetido.
    """
    valor_final = None
    for usuario in lista_usuarios:
        zona_actual = usuario["datos_necesarios_stats"]["zona"]
        presupuesto = usuario["datos_necesarios_stats"]["presupuesto"]
        
        if condicion_zona(zona_actual):
            if valor_final is None:
                valor_final = presupuesto
            else:
                valor_final = funcion_reductora(valor_final, presupuesto)
                
    return valor_final

def es_zona_sur(zona): 
    return zona == "Zona Sur"

def es_zona_norte(zona): 
    return zona == "Zona Norte"

def es_zona_central(zona): 
    return zona == "Zona Central"

def elegir_maximo(actual, nuevo):
    res = actual
    if nuevo > actual:
        res = nuevo
    return res

def elegir_minimo(actual, nuevo):
    res = actual
    if nuevo < actual:
        res = nuevo
    return res

def cant_tipo_viaje(tipo_viaje, tipo):
    contar = 0
    if tipo_viaje == tipo:
        contar = 1
    return contar

def acumular_presupuesto(acu_presupuesto, presupuesto):
    return acu_presupuesto + presupuesto

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
        tipo_viaje = usuario["datos_necesarios_stats"]["tipo_viaje"]

        stats["total_presupuesto"] = acumular_presupuesto(stats["total_presupuesto"], presupuesto)
        stats["pres_avion"] += cant_tipo_viaje(tipo_viaje, 'Avión')
        stats["pres_auto"] += cant_tipo_viaje(tipo_viaje, 'Auto')
        stats["pres_colectivo"] += cant_tipo_viaje(tipo_viaje, 'Colectivo')

    stats["max_sur"] = filtrar_y_reducir_presupuesto(lista_usuarios, es_zona_sur, elegir_maximo)
    stats["min_sur"] = filtrar_y_reducir_presupuesto(lista_usuarios, es_zona_sur, elegir_minimo)
    
    stats["max_norte"] = filtrar_y_reducir_presupuesto(lista_usuarios, es_zona_norte, elegir_maximo)
    stats["min_norte"] = filtrar_y_reducir_presupuesto(lista_usuarios, es_zona_norte, elegir_minimo)
    
    stats["max_central"] = filtrar_y_reducir_presupuesto(lista_usuarios, es_zona_central, elegir_maximo)
    stats["min_central"] = filtrar_y_reducir_presupuesto(lista_usuarios, es_zona_central, elegir_minimo)

    if stats["usuarios_ingresados"] > 0:
        stats["porc_avion"] = (stats["pres_avion"] / stats["usuarios_ingresados"]) * 100
        stats["porc_auto"] = (stats["pres_auto"] / stats["usuarios_ingresados"]) * 100
        stats["porc_colectivo"] = (stats["pres_colectivo"] / stats["usuarios_ingresados"]) * 100
        stats["promedio"] = stats["total_presupuesto"] / stats["usuarios_ingresados"]

    return stats