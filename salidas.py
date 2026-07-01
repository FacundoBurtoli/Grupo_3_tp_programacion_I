def mostrar_datos(nombre, lugares, temporadas, zona):
    print("\nSISTEMA DE RECOMENDACIONES.")
    print(f"Bienvenido, {nombre}! A continuación podrás ver los resultados de nuestras recomendaciones: ")
    print("[-DESTINO-]")
    print(f"Su zona elegida fue: {zona}.")
    print(f"Lugares que nosotros podemos recomendarle: {lugares}.")
    print(f"Su temporada seleccionada fue: {temporadas}")

def mostrar_informe_individual(usuario, promedio_global):
    print("\n[-INFORME DEL VIAJE-]")
    print(f"Usuario: {usuario['datos_ingresados']['nombre']} (ID: {usuario['identificador']})")
    
    print("[-COSTO DEL VIAJE-]")
    print(f"Su modo de viaje será en: {usuario['datos_necesarios_stats']['tipo_viaje']}")
    print(f"El costo del viaje es: ${usuario['datos_necesarios_stats']['costo_viaje']}")

    print("[-HOTEL-]")
    print(f"{usuario['datos_necesarios_stats']['hotel_recomendado']}")
    print(f"El costo del hotel es: ${usuario['datos_necesarios_stats']['costo_hotel']}")

    print("[-EXCURSIONES-]")
    print(f"Su tipo de excursión será: {usuario['datos_necesarios_stats']['excursiones']}")
    print(f"El valor de la excursión es: ${usuario['datos_necesarios_stats']['valor_excursion']}")

    print("[-COSTO TOTAL-]")
    print(f"El total del costo es: ${usuario['datos_necesarios_stats']['costo_total']}")

    print("[-MENSAJES EXTRA-]")
    for mensaje in usuario["recomendaciones"]:
        if mensaje.strip() != "":
            print(f"- {mensaje}")

    print("[-ANALISIS-]")
    if usuario['datos_necesarios_stats']['costo_total'] > usuario['datos_necesarios_stats']['presupuesto']:
        print("El viaje no está dentro del presupuesto!")
        print("No vas a poder disfrutar del viaje debido a los problemas económicos!")
    else:
        print("El viaje está dentro del presupuesto!")
        print("Te recomendamos ajustar el tipo del hotel, transporte y/o excursiones")

    if usuario['datos_necesarios_stats']['costo_total'] > promedio_global:
        print("Además, el viaje no está dentro del promedio de otros usuarios.")
    else:
        print("Además, el viaje está dentro del promedio de otros usuarios!")

def mostrar_informe_final(stats):
    print("\n[-INFORME GLOBAL DE ESTADÍSTICAS-]")
    print(f"Total de usuarios procesados: {stats['usuarios_ingresados']}")
    print(f"Presupuesto promedio: ${stats['promedio']:.2f}")
    
    print("[-PORCENTAJES DE TRANSPORTE-]")
    print(f"Porcentaje en avión: {stats['porc_avion']:.2f}%")
    print(f"Porcentaje en auto: {stats['porc_auto']:.2f}%")
    print(f"Porcentaje en colectivo: {stats['porc_colectivo']:.2f}%")

    print("[-GRÁFICO DE VIAJES-]")
    print("Gráfico de avión:     " + "*" * stats["pres_avion"])
    print("Gráfico de auto:      " + "*" * stats["pres_auto"])
    print("Gráfico de colectivo: " + "*" * stats["pres_colectivo"])
    
    print("\nMuchas gracias por usar nuestro programa!")