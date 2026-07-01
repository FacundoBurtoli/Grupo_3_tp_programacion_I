def limpiar_y_normalizar(cadena):
    cadena_limpia = ""
    dentro_de_palabra = False
    
    for caracter in cadena:
        if caracter != " ":
            cadena_limpia += caracter
            dentro_de_palabra = True
        else:
            if dentro_de_palabra:
                cadena_limpia += " "
                dentro_de_palabra = False
                
    if cadena_limpia and cadena_limpia[-1] == " ":
        cadena_limpia = cadena_limpia[:-1]
        
    cadena_normalizada = ""
    for caracter in cadena_limpia:
        codigo = ord(caracter)
        if codigo >= 65 and codigo <= 90:
            cadena_normalizada += chr(codigo + 32)
        else:
            cadena_normalizada += caracter
            
    return cadena_normalizada

def pedir_cadena(mensaje, minimo):
    cadena = input(mensaje)
    while len(cadena) < minimo:
        cadena = input(f'ERROR: {mensaje} valido: ')
    return cadena

def pedir_entero(mensaje, minimo, maximo):
    numero = int(input(mensaje))
    if maximo is not None:
        while numero < minimo or numero > maximo:
            numero = int(input(f'ERROR: {mensaje} valido: '))
    else: 
        while numero < minimo:
            numero = int(input(f'ERROR: {mensaje} valido: '))
    return numero

def pedir_flotante(mensaje, minimo, maximo):
    floatante = float(input(mensaje))
    while floatante < minimo or floatante > maximo:
        floatante = float(input(f'ERROR: {mensaje} valido: '))
    return floatante

def pedir_categoria(mensaje, opciones):
    seleccion = input(mensaje)
    seleccion_normalizada = limpiar_y_normalizar(seleccion)
    
    opciones_normalizadas = []
    for opcion in opciones:
        opciones_normalizadas.append(limpiar_y_normalizar(opcion))
        
    while seleccion_normalizada not in opciones_normalizadas:
        seleccion = input(f'ERROR: {mensaje} valido: ')
        seleccion_normalizada = limpiar_y_normalizar(seleccion)
        
    res = opciones[0]
    for i in range(len(opciones_normalizadas)):
        if seleccion_normalizada == opciones_normalizadas[i]:
            res = opciones[i]
            
    return res