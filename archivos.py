def comprobar_y_cargar_archivo(ruta_archivo):
    lista_usuarios = []
    try:
        archivo = open(ruta_archivo, "r")
        lineas = archivo.readlines()
        archivo.close()
        
        for linea in lineas:
            linea = linea.strip()
            if linea != "":
                partes = linea.split(";")
                
                usuario_dicc = {
                    "identificador": int(partes[0]),
                    "datos_ingresados": {
                        "nombre": partes[1],
                        "edad": int(partes[2]),
                        "genero": partes[3],
                        "altura": float(partes[4]),
                        "nivel_estres": int(partes[5]),
                        "usuario": partes[6],      
                        "contrasena": partes[7]    
                    },
                    "recomendaciones": partes[8].split(","), 
                    "datos_necesarios_stats": {
                        "presupuesto": int(partes[9]),
                        "zona": partes[10],
                        "tipo_viaje": partes[11],
                        "costo_viaje": int(partes[12]),
                        "hotel_recomendado": partes[13],
                        "costo_hotel": int(partes[14]),
                        "excursiones": partes[15],
                        "valor_excursion": int(partes[16]),
                        "costo_total": int(partes[17])
                    }
                }
                lista_usuarios.append(usuario_dicc)
    except FileNotFoundError:
        pass
        
    return lista_usuarios


def guardar_datos_archivo(ruta_archivo, lista_usuarios):
    exito = True
    try:
        archivo = open(ruta_archivo, "w")
        
        for u in lista_usuarios:
            recomendaciones_str = ",".join(u["recomendaciones"])
            
            linea = (
                f"{u['identificador']};"
                f"{u['datos_ingresados']['nombre']};"
                f"{u['datos_ingresados']['edad']};"
                f"{u['datos_ingresados']['genero']};"
                f"{u['datos_ingresados']['altura']};"
                f"{u['datos_ingresados']['nivel_estres']};"
                f"{u['datos_ingresados']['usuario']};"
                f"{u['datos_ingresados']['contrasena']};"
                f"{recomendaciones_str};"
                f"{u['datos_necesarios_stats']['presupuesto']};"
                f"{u['datos_necesarios_stats']['zona']};"
                f"{u['datos_necesarios_stats']['tipo_viaje']};"
                f"{u['datos_necesarios_stats']['costo_viaje']};"
                f"{u['datos_necesarios_stats']['hotel_recomendado']};"
                f"{u['datos_necesarios_stats']['costo_hotel']};"
                f"{u['datos_necesarios_stats']['excursiones']};"
                f"{u['datos_necesarios_stats']['valor_excursion']};"
                f"{u['datos_necesarios_stats']['costo_total']}\n"
            )
            archivo.write(linea)
            
        archivo.close()
    except Exception:
        exito = False
        
    return exito