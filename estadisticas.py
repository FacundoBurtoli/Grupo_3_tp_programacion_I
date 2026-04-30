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