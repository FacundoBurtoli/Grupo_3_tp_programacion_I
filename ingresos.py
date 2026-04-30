def pedir_cadena(mensaje, minimo):
    cadena = input(mensaje)
    while len(cadena) < minimo:
        cadena = input(f'ERROR: ', {mensaje}, 'valido')
    return cadena

def pedir_entero(mensaje, minimo, maximo):
    numero = int(input(mensaje))
    if maximo is not None:
        while numero < minimo or numero > maximo:
            numero = int(input(f'ERROR: {mensaje} valido.'))
    else: 
        while numero < minimo:
            numero = int(input(f'ERROR: {mensaje} valido.'))
    return numero

def pedir_flotante(mensaje, minimo, maximo):
    flotante = float(input(mensaje))
    while flotante < minimo or flotante > maximo:
        flotante = int(input(f'ERROR: {mensaje} valido.'))
    return flotante

def pedir_categoria(mensaje, opciones):
    bandera = False
    while bandera == False:
        seleccion = input(mensaje)
        for i in range(len(opciones)):
            if seleccion == opciones[i]:
                bandera == True
                break
    return  seleccion

