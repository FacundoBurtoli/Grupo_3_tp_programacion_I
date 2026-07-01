from ingresos import *
from reglas import *
from estadisticas import *
from salidas import *
from archivos import comprobar_y_cargar_archivo, guardar_datos_archivo

def main():
    ruta_db = "usuarios.txt"
    lista_usuarios = comprobar_y_cargar_archivo(ruta_db)
    
    contador_id = 0
    if len(lista_usuarios) > 0:
        contador_id = lista_usuarios[-1]["identificador"]

    rol_autenticado = None
    usuario_sesion = ""
    contrasena_sesion = ""

    print("=== SISTEMA DE LOGEO ===")
    print("Para Administrador use: admin / admin123")
    
    login = pedir_categoria("\nDesea logearse? (si/no): ", ['si', 'no'])

    if login == "si":
        creacion_usuario = pedir_cadena("Crear su usuario(minmo 6 caracteres): ", 6)
        creacion_contrasegna = pedir_cadena("Crear su contraseña(minmo 6 caracteres): ", 6)
        
        # Validamos si las credenciales ingresadas corresponden al Administrador
        if creacion_usuario == "admin" and creacion_contrasegna == "admin123":
            rol_autenticado = "Administrador"
            print("[-ACCESO CONCEDIDO - ROL: ADMINISTRADOR-]")
        else:
            intentos = 3
            acceso = False

            while intentos > 0:
                usuario = pedir_cadena("Ingrese su usuario para acceder: ", 6)
                contraseña = pedir_cadena("Ingrese su contraseña para acceder: ", 6)

                if usuario == creacion_usuario and contraseña == creacion_contrasegna:
                    acceso = True
                    rol_autenticado = "Usuario"
                    usuario_sesion = creacion_usuario
                    contrasena_sesion = creacion_contrasegna
                    print("[-ACCESO CONCEDIDO - ROL: USUARIO-]")
                    break
                else:
                    intentos -= 1
                    print(f"Error! Te quedan: {intentos} intentos.")
                
            if not acceso:
                print("Acceso denegado.")
                return
    elif login == "no":
        return

    seguir = "no"
    if rol_autenticado == "Usuario":
        seguir = "si"
        
    while seguir == "si":
        contador_id += 1
        
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

        lugares = definir_lugares(zona)
        mensajes_lista = definir_mensaje(temporadas, zona, presupuesto, tipo_viaje, nivel_estres, tipo_hotel, edad, maletas, duracion_estadia, excursiones)

        hotel_recomendado = recomendar_hotel_y_costo(tipo_hotel, zona, True)
        costo_hotel = recomendar_hotel_y_costo(tipo_hotel, zona, False)
        costo_viaje = obtener_costo_viaje(zona, temporadas, tipo_viaje)
        valor_excursion = obtener_valor_excursion(excursiones, temporadas, zona)
        
        costo_total = costo_hotel + costo_viaje + valor_excursion

        mostrar_datos(nombre, lugares, temporadas, zona)

        usuario_dicc = {
            "identificador": contador_id,
            "datos_ingresados": {
                "nombre": nombre,
                "edad": edad,
                "genero": genero,
                "altura": flotante,
                "nivel_estres": nivel_estres,
                "usuario": usuario_sesion,
                "contrasena": contrasena_sesion
            },
            "recomendaciones": mensajes_lista,
            "datos_necesarios_stats": {
                "presupuesto": presupuesto,
                "zona": zona,
                "tipo_viaje": tipo_viaje,
                "costo_viaje": costo_viaje,
                "hotel_recomendado": hotel_recomendado,
                "costo_hotel": costo_hotel,
                "excursiones": excursiones,
                "valor_excursion": valor_excursion,
                "costo_total": costo_total
            }
        }
        
        lista_usuarios.append(usuario_dicc)
        seguir = pedir_categoria("\nDesea seguir? (si/no): ", ['si', 'no'])

    # Guardamos los datos nuevos en el archivo de texto plano si operó un Usuario
    if rol_autenticado == "Usuario" and len(lista_usuarios) > 0:
        guardar_datos_archivo(ruta_db, lista_usuarios)

    # Bloque de salidas según el rol autenticado
    if len(lista_usuarios) > 0:
        diccionario_stats = calcular_estadisticas(lista_usuarios)
        
        if rol_autenticado == "Administrador":
            mostrar_informe_final(diccionario_stats)
        elif rol_autenticado == "Usuario":
            # Un usuario común solo ve los registros asociados a su nombre de usuario de la sesión
            for u in lista_usuarios:
                if u["datos_ingresados"]["usuario"] == usuario_sesion:
                    mostrar_informe_individual(u, diccionario_stats["promedio"])
    else:
        print("\nNo hay datos en el sistema para procesar.")

main()