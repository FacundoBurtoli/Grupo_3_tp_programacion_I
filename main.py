from ingresos import *
from reglas import *
from estadisticas import *
from salidas import *
from calculos_generales import *

def main():
    seguir = "si"

    usuarios_ingresados = 0
    total_presupuesto = 0

    pres_minimo = None
    pres_maximo = None

    pres_avion = 0
    pres_auto = 0
    pres_colectivo = 0

    acu_presupuesto = 0

    maximo_sur = None
    maximo_norte = None
    maximo_central = None
    minimo_sur = None
    minimo_norte = None
    minimo_central = None

    login = pedir_categoria("\nDesea logearse? (si/no): ", ['si', 'no'])

    if login == "si":
        creacion_usuario = pedir_cadena("Crear su usuario(minmo 6 caracteres): ", 6)
        creacion_contraseña = pedir_cadena("Crear su contraseña(minmo 6 caracteres): ", 6)
        intentos = 3
        acceso = False

        while intentos > 0:
            usuario = pedir_cadena("Crear su usuario(minmo 6 caracteres): ", 6)
            contraseña = pedir_cadena("Crear su contraseña(minmo 6 caracteres): ", 6)

            if usuario == creacion_usuario and contraseña == creacion_contraseña:
                acceso = True
                print("[-ACCESO CONCEDIDO-]")
                break
            else:
                intentos -= 1
                print(f"Error! Te quedan: {intentos} intentos.")
            
        if not acceso:
            print("Acceso denegado.")
            exit()
    elif login == "no":
        exit()

    # --- INICIO DEL BUCLE DE VIAJEROS ---
    while seguir == "si":
        nombre = pedir_cadena("Ingrese su nombre: ", 2)
        edad = pedir_entero("Ingrese su edad (1-100): ", 1, 100)
        genero = pedir_categoria("Ingrese su genero: (Masculino, Femenino, No-Binario): ", ['Masculino', 'Femenino', 'No-Binario'])
        flotante = pedir_flotante("Ingrese su altura(1.00-3.00): ", 1.00, 3.00)
        nivel_estres = pedir_entero("¿Cuál es su nivel de estrés?(1-10): ", 1, 10)
        temporadas = pedir_categoria("¿Qué tipo de temporada que prefiere? [Invierno, Otoño, Verano]: ", ['Invierno', 'Otoño', 'Verano'])
        zona = pedir_categoria('A qué zona desea ir en su viaje? (Zona Norte, Zona Sur, Zona Central)', ['Zona Norte', 'Zona Sur', 'Zona Central'])
        presupuesto = pedir_entero("¿Cúanto es la cantidad de saldo que llevara?(Debe ser mayor a 1): ", 1, maximo=None)
        tipo_hotel = pedir_entero("¿Cuánto es el rating del hotel deseado?(1-5): ", 1, 5)
        duracion_estadia = pedir_entero("¿Cuánto son los días que usted se quedará?: ", 1, maximo=None)
        maletas = pedir_entero("¿Cuántas maletas son las que llevará?(1-3): ", 1, 3)
        tipo_viaje = pedir_categoria("¿De qué manera prefiere ir? (Auto, Colectivo, Avión): ", ['Auto', 'Colectivo', 'Avión'])
        excursiones = pedir_categoria("¿Cómo desea realizar usted las excursiones? (Guiada o Cuenta Propia): ", ['Guiada', 'Cuenta Propia'])

        usuarios_ingresados += 1
        total_presupuesto += presupuesto

        # PROCESO INDIVIDUAL (Dentro del while)
        
        # Parte 1: CONTADORES (Se debe acumular usando +=)
        # Nota: Ajustado a 'Avión' con tilde para que coincida con el input
        pres_avion += cant_tipo_viaje(tipo_viaje, 'Avión')
        pres_auto += cant_tipo_viaje(tipo_viaje, 'Auto')
        pres_colectivo += cant_tipo_viaje(tipo_viaje, 'Colectivo')

        # Acumular presupuesto
        acu_presupuesto = acumular_presupuesto(acu_presupuesto, presupuesto)
        
        # Obtener pres maximo y minimo generales
        pres_maximo = obtener_maximo(pres_maximo, presupuesto)
        pres_minimo = obtener_minimo(pres_minimo, presupuesto)

        # Máximos y mínimos por zona
        if zona == "Zona Sur":
            maximo_sur = obtener_maximo(maximo_sur, presupuesto)
            minimo_sur = obtener_minimo(minimo_sur, presupuesto)
        elif zona == "Zona Norte":
            maximo_norte = obtener_maximo(maximo_norte, presupuesto)
            minimo_norte = obtener_minimo(minimo_norte, presupuesto)
        else: 
            maximo_central = obtener_maximo(maximo_central, presupuesto)
            minimo_central = obtener_minimo(minimo_central, presupuesto)
        
        # Parte 2: LUGARES SEGÚN SU ZONA
        lugares = definir_lugares(zona)

        # Parte 3: REGLAS (Guardamos el resultado en la variable 'mensajes')
        mensajes = definir_mensaje(temporadas, zona, presupuesto, tipo_viaje, nivel_estres, tipo_hotel, edad, maletas, duracion_estadia, excursiones)

        # Parte 4: CLASIFICACIONES DEL HOTEL
        hotel_recomendado = recomendar_hotel_y_costo(tipo_hotel, zona, True)
        costo_hotel = recomendar_hotel_y_costo(tipo_hotel, zona, False)

        # Parte 5: TIPOS DE VIAJE Y SUS COSTOS
        costo_viaje = obtener_costo_viaje(zona, temporadas, tipo_viaje)

        # Parte 6: VALORES DE LAS EXCURSIONES
        valor_excursion = obtener_valor_excursion(excursiones, temporadas, zona)
        
        # Calcular el costo total de este viaje individual
        costo_total = costo_hotel + costo_viaje + valor_excursion

        # SALIDA INDIVIDUAL (Muestra los datos del usuario actual antes de preguntar si sigue)
        mostrar_datos(nombre, lugares, temporadas, zona)

        # Preguntar si desea continuar (Última instrucción dentro del while)
        seguir = pedir_categoria("\nDesea seguir? (si/no): ", ['si', 'no'])
    
    # --- FIN DEL BUCLE DE VIAJEROS ---

    # CÁLCULOS GLOBALES (Afuera del while, cuando ya cargaron todos los usuarios)
    if usuarios_ingresados > 0:
        porc_avion = (pres_avion / usuarios_ingresados) * 100
        porc_auto =  (pres_auto / usuarios_ingresados) * 100
        porc_colectivo = (pres_colectivo / usuarios_ingresados) * 100
        promedio = total_presupuesto / usuarios_ingresados

        # MOSTRAR INFORME FINAL (Con todas las variables ordenadas correctamente)
        mostrar_inorme_final(
            tipo_viaje, costo_viaje, hotel_recomendado, costo_hotel, 
            excursiones, valor_excursion, costo_total, porc_avion, 
            porc_auto, porc_colectivo, pres_avion, pres_auto, 
            pres_colectivo, promedio, presupuesto, mensajes
        )

# Fin.