def mostrar_datos(nombre, lugares, temporadas, zona):
    print("SISTEMA DE RECOMENDACIONES.")
    print(f"Bienvenido, {nombre}! A continuación podrás ver los resultados de nuestras recomendaciones: ")
    print("[-DESTINO-]")
    print(f"Su zona elegida fue: {zona}.")
    print(f"Lugares que nosotros podemos recomendarle: {lugares}.")
    print(f"Su temporada seleccionada fue: {temporadas}")

def mostrar_inorme_final(tipo_viaje, costo_viaje, hotel_recomendado, costo_hotel, excursiones, valor_excursion, costo_total, porc_avion, porc_auto, porc_colectivo, pres_avion, pres_auto, pres_colectivo, promedio, presupuesto, mensajes):
    print ("[-INFORME FINAL-]")

    print("[-COSTO DEL VIAJE-]")
    print(f"Su modo de viaje será en: {tipo_viaje}")
    print(f"El costo del viaje es: ${costo_viaje}")

    print("[-HOTEL-]")
    print(f"{hotel_recomendado}")
    print(f"El costo del hotel es: ${costo_hotel}")

    print("[-EXCURSIONES-]")
    print(f"Su tipo de excursión será: {excursiones}")
    print(f"El valor de la excursión es: ${valor_excursion}")

    print("[-COSTO TOTAL-]")
    print(f"El total del costo es: ${costo_total}")

    print("[-PORCENTAJES-]")
    print(f"Porcentaje en avión: {porc_avion}%")
    print(f"Porcentaje en auto: {porc_auto}%")
    print(f"Porcentaje en colectivo: {porc_colectivo}%")


    print("[-GRÁFICO DE VIAJES-]")
    print("Gráfico de avión: " + "*" * pres_avion)
    print("Gráfico de auto: " + "*" * pres_auto)
    print("Gráfico de colectivo: " + "*" * pres_colectivo)

    print("[-MENSAJES EXTRA-]")
    print(f"{mensajes}")

    print("[-ANALISIS-]")


    if costo_total > presupuesto:
        print("El viaje no está dentro del presupuesto!")
        print("No vas a poder disfrutar del viaje debido a los problemas económicos!")
    else:
        print("El viaje está dentro del presupuesto!")
        print("Te recomendamos ajustar el tipo del hotel, transporte y/o excursiones")

    if costo_total > promedio:
        print("Además, el viaje no está dentro del promedio de otros usuarios.")
    else:
        print("Además, el viaje está dentro del promedio de otros usuarios!")

    print("Muchas gracias por usar nuestro programa!")