def definir_lugares(zona):
    if zona == "Zona Norte":
        return "Salta, Jujuy, o Cataratas del Iguazú"
    elif zona == "Zona Sur":
        return "Bariloche, Chubut, o Tierra del Fuego"
    else:
        return "Buenos Aires, Cordoba, o Mendoza"

def definir_mensaje(temporadas, zona, presupuesto, tipo_viaje, nivel_estres, tipo_hotel, edad, maletas, duracion_estadia, excursiones):
    mensajes = []
    lugares = definir_lugares(zona)

    lista_reglas = [
        {
            "condiciones": [temporadas == "Verano", zona == "Zona Central", presupuesto > 80000],
            "mensaje": f"Se le recomienda lugares como {lugares}, que podrían ayudarte a tomarte un descanso."
        },
        {
            "condiciones": [temporadas == "Otoño", zona == "Zona Central"],
            "mensaje": f"Se le recomienda lugares como {lugares}, y llevar abrigo."
        },
        {
            "condiciones": [zona == 'Zona Central', maletas > 2, tipo_viaje == 'Auto'],
            "mensaje": f"Se le recomienda lugares como {lugares}, tener un baul amplio en su vehiculo."
        },
        {
            "condiciones": [temporadas == "Verano", zona == "Zona Norte", presupuesto > 70000],
            "mensaje": f"Se le recomienda lugares como {lugares}, que podrían ayudarte a relajarte."
        },
        {
            "condiciones": [nivel_estres > 7],
            "mensaje": f"Su nivel de estrés es alto, lugares como {lugares} podrían ayudarle a poder tener unas vacaciones relajadas y así bajar su alto estrés."
        },
        {
            "condiciones": [nivel_estres >= 5, nivel_estres <= 7],
            "mensaje": f"Le podemos recomendar un viaje tranquilo, a lugares como {lugares}, para así bajar un poco el ritmo."
        },
        {
            "condiciones": [nivel_estres < 5],
            "mensaje": f"Tenés una buena energía, podriamos recomendarte lugares como {lugares} para poder hacer algunas actividades."
        },
        {
            "condiciones": [tipo_hotel == 5, presupuesto < 60000],
            "mensaje": "Elegiste un hotel de 5 estrellas, pero el presupuesto no te alcanzará para poder pagar dicha estadia."
        },
        {
            "condiciones": [edad >= 18, edad <= 30],
            "mensaje": "Por tu edad, podrías disfrutar de destinos con mucho movimiento y vida nocturna como los antes mencionados."
        },
        {
            "condiciones": [edad < 18],
            "mensaje": "Por tu edad, podrías disfrutar de un viaje familiar hacia lugares como los antes mencionados, con actividades tranquilas y seguras."
        },
        {
            "condiciones": [zona == "Zona Sur", tipo_viaje == "Auto", maletas > 2],
            "mensaje": "Si viajas al sur en auto, el trayecto será largo. Aunque usted debería optimizar la cantidad de maletas dentro del auto."
        },
        {
            "condiciones": [presupuesto < 40000 or duracion_estadia > 10],
            "mensaje": "Teniendo en cuenta tu presupuesto y tu duración en el viaje, te convendría optar por lugares económicos"
        },
        {
            "condiciones": [excursiones != "Guiada"],
            "mensaje": "Si vas a ir por tu cuenta al viaje, tendrás que investigar bien las excursiones antes de viajar al lugar que haya elegido."
        },
        {
            "condiciones": [nivel_estres > 8, temporadas == "Invierno", tipo_hotel >= 4],
            "mensaje": "Vaya, excelente elección mi amigo! Destinos como estos, le podría resultar útil para poder descansar y despejar su mente en esta temporada invernal."
        },
        {
            "condiciones": [duracion_estadia > 7, presupuesto <= 50000],
            "mensaje": "Vas a estar varios días en lugares como los antes mencionados. Por lo tanto, recomendamos que organices bien tus gastos! Ya que si usas mucho tu dinero, vas a quedarte corto en presupuesto."
        },
        {
            "condiciones": [tipo_viaje == "Avión", zona == "Zona Sur"],
            "mensaje": "Buena idea, ya que tomar el avión para viajar a los lugares de la zona sur, ayuda a ahorrar mucho tiempo."
        },
        {
            "condiciones": [tipo_hotel == 1 or tipo_hotel == 2],
            "mensaje": "Viaje largo con presupuesto ajustado: planificar gastos."
        },
        {
            "condiciones": [temporadas == "Verano", nivel_estres > 6, presupuesto > 70000, tipo_hotel >= 4],
            "mensaje": "Esto le resultará un viaje ideal, debido a que tendrá un verano de relajación total con un hotel premium."
        },
        {
            "condiciones": [tipo_viaje == "Colectivo", zona == "Zona Sur", duracion_estadia < 5],
            "mensaje": "Viajar al sur en colectivo podría volverse bastante largo. Tal vez te conviene aumentar los días de estadía para aprovechar mejor manera el viaje."
        },
        {
            "condiciones": [tipo_viaje == "Colectivo", nivel_estres > 7],
            "mensaje": "Como tenés un nivel de estrés alto, te recomendamos que priorices la comodidad durante el viaje. En trayectos largos en colectivo, podrías sentirte un poco incómodo, por lo que sería bueno elegir asientos más confortables, o considerar otra opción."
        },
        {
            "condiciones": [tipo_viaje == "Colectivo", duracion_estadia <= 3],
            "mensaje": "Para viajes cortos, el colectivo puede ser práctico y económico"
        },
        {
            "condiciones": [tipo_viaje == "Colectivo", zona == "Zona Norte"],
            "mensaje": "Viajar en colectivo al norte, es una buena opción. Apesar de ser un viaje largo, te permite viajar de forma más tranquilidad."
        },
        {
            "condiciones": [tipo_viaje == "Colectivo", temporadas == "Verano"],
            "mensaje": "Viajar en colectivo en verano te será cómodo gracias al aire acondicionado que posee el mismo, también te recomendamos llevar agua fría y ropa liviana para mayor comodidad."
        },
        {
            "condiciones": [tipo_viaje == "Colectivo", zona == "Zona Norte", presupuesto < 60000, maletas <= 2],
            "mensaje": "Viajar en colectivo al Norte, te podría resultar accesible para el viaje. Además al no llevar poco equipaje, te resultará viajar mucho mas cómodo."
        },
        {
            "condiciones": [maletas > 3],
            "mensaje": "Y se recomienda llevar menor equipaje."
        },
        {
            "condiciones": [maletas <= 3],
            "mensaje": "Y su cantidad de equipaje adecuada."
        }
    ]

    for regla in lista_reglas:
        cumple_todas = True
        for condicion in regla["condiciones"]:
            if not condicion:
                cumple_todas = False
                break
        if cumple_todas:
            mensajes.append(regla["mensaje"])

    return mensajes

def recomendar_hotel_y_costo(tipo_hotel, zona, categoria):
    match tipo_hotel:
        case 1:
            if zona == "Zona Norte":
                hotel_recomendado = "Se le recomienda el Hostel Marilian en Salta, o el Pacha Hosten en Jujuy"
                costo_hotel = 25000
            elif zona == "Zona Sur":
                hotel_recomendado = "Se le recomienda el Hostel Piuke Mapu en Chubut, o la Yaghan Hostel en Tierra del Fuego."
                costo_hotel = 40000
            else:
                hotel_recomendado = "Se le recomienda el Hostel Sheraton en Buenos Aires, o Gran hotel victoria en Cordoba o Hilton en mendoza ."
                costo_hotel = 30000
        case 2:
            if zona == "Zona Norte":
                hotel_recomendado = "Se le recomienda el La Posada del Parque en Salta, o Beer Hotel en Iguazú."
                costo_hotel = 40000
            elif zona == "Zona Sur":
                hotel_recomendado = "Se le recomienda el Hostel Inn en Bariloche, o el Gaulicho Hostel en Chubut."
                costo_hotel = 55000
            else:
                hotel_recomendado = "Se le recomienda el Hostel Central cordoba en Buenos Aires, o sussex hotel en Cordoba o hotel abril boutique en mendoza ."
                costo_hotel = 45000
        case 3:
            if zona == "Zona Norte":
                hotel_recomendado = "Se le recomienda el Apartamento la Posta en Jujuy, o el Hotel Sol Cataratas en Iguazú"
                costo_hotel = 55000
            elif zona == "Zona Sur":
                hotel_recomendado = "Se le recomienda el Ruca Hue en Chubut, o Hosteria Oikos en Bariloche"
                costo_hotel = 70000
            else: 
                hotel_recomendado = "Se le recomienda el Ibis buenos aires obelisco en Buenos Aires, o holiday  en Cordoba o hotel raices aconcagua en mendoza ."
                costo_hotel = 60000
        case 4:
            if zona == "Zona Norte":
                hotel_recomendado = "Se le recomienda el Hotel Munay en Jujuy, o el Hotel las Chirimoyas en Salta"
                costo_hotel = 70000
            elif zona == "Zona Sur":
                hotel_recomendado = "Se le recomienda el Hotel Austral en Tierra del Fuego, o el Aguada Hotel en Chubut"
                costo_hotel = 85000
            else: 
                hotel_recomendado = "Se le recomienda el Hotel pulitzer en Buenos Aires, o yrigoyen 111 en Cordoba o hotel splendor en mendoza ."
                costo_hotel = 75000
        case 5:
            if zona == "Zona Norte":
                hotel_recomendado = "Se le recomienda el Hotel La Reserva Virgin Lodge en Iguazú, o el Hotel Caseros en Salta"
                costo_hotel = 85000
            elif zona == "Zona Sur":
                hotel_recomendado = "Se le recomienda el Hotel Arelauquen Lodge en Bariloche, o el Hotel Los Ñires Ushuaia"
                costo_hotel = 100000
            else:
                hotel_recomendado = "Se le recomienda el palacio dahau en Buenos Aires, o el castillo hotel victoria en Cordoba o Park hyatt en mendoza ."
                costo_hotel = 90000
    if categoria == False:
        valor = costo_hotel
    else: 
        valor = hotel_recomendado
    return valor

def obtener_costo_viaje(zona, temporadas, tipo_viaje):
    costo_viaje = 0
    match zona:
        case "Zona Norte":
            if temporadas == "Verano":
                match tipo_viaje:
                    case "Auto":
                        costo_viaje = 10000
                    case "Colectivo":
                        costo_viaje = 200000
                    case "Avión":
                        costo_viaje = 300000
            elif temporadas == "Invierno":
                match tipo_viaje:
                    case "Auto":
                        costo_viaje = 50000
                    case "Colectivo":
                        costo_viaje = 150000
                    case "Avión":
                        costo_viaje = 250000
            elif temporadas == "Otoño":
                match tipo_viaje:
                    case "Auto":
                        costo_viaje = 30000
                    case "Colectivo":
                        costo_viaje = 170000
                    case "Avión":
                        costo_viaje = 200000
        case "Zona Sur":
            if temporadas == "Verano":
                match tipo_viaje:
                    case "Auto":
                        costo_viaje = 15000
                    case "Colectivo":
                        costo_viaje = 180000
                    case "Avión":
                        costo_viaje = 270000
            elif temporadas == "Invierno":
                match tipo_viaje:
                    case "Auto":
                        costo_viaje = 20000
                    case "Colectivo":
                        costo_viaje = 190000
                    case "Avión":
                        costo_viaje = 310000
            elif temporadas == "Otoño":
                match tipo_viaje:
                    case "Auto":
                        costo_viaje = 30000
                    case "Colectivo":
                        costo_viaje = 200000
                    case "Avión":
                        costo_viaje = 320000
        case "Zona Central":
            if temporadas == "Verano":
                match tipo_viaje:
                    case "Auto":
                        costo_viaje = 15000
                    case "Colectivo":
                        costo_viaje = 250000
                    case "Avión":
                        costo_viaje = 350000
            elif temporadas == "Invierno":
                match tipo_viaje:
                    case "Auto":
                        costo_viaje = 55000
                    case "Colectivo":
                        costo_viaje = 150000
                    case "Avión":
                        costo_viaje = 250000
            elif temporadas == "Otoño":
                match tipo_viaje:
                    case "Auto":
                        costo_viaje = 35000
                    case "Colectivo":
                        costo_viaje = 200000
                    case "Avión":
                        costo_viaje = 250000
    return costo_viaje

def obtener_valor_excursion(excursiones, temporadas, zona):
    valor_excursion = 0
    match excursiones:
        case "Guiada":
            if temporadas == "Verano":
                match zona:
                    case "Zona Norte":
                        valor_excursion = 30000
                    case "Zona Sur":
                        valor_excursion = 15000
                    case 'Zona Central':
                        valor_excursion = 20000
            elif temporadas == "Invierno":
                match zona:
                    case "Zona Norte":
                        valor_excursion = 25000
                    case "Zona Sur":
                        valor_excursion = 40000
                    case 'Zona Central':
                        valor_excursion = 30000
            elif temporadas == "Otoño":
                match zona:
                    case "Zona Norte":
                        valor_excursion = 35000
                    case "Zona Sur":
                        valor_excursion = 20000
                    case 'Zona Central':
                        valor_excursion = 25000
        case "Cuenta Propia":
            if temporadas == "Verano":
                match zona:
                    case "Zona Norte":
                        valor_excursion = 45000
                    case "Zona Sur":
                        valor_excursion = 35000
                    case 'Zona Central':
                        valor_excursion = 30000
            elif temporadas == "Invierno":
                match zona:
                    case "Zona Norte":
                        valor_excursion = 60000
                    case "Zona Sur":
                        valor_excursion = 50000
                    case 'Zona Central':
                        valor_excursion = 55000
            elif temporadas == "Otoño":
                match zona:
                    case "Zona Norte":
                        valor_excursion = 50000
                    case "Zona Sur":
                        valor_excursion = 40000
                    case 'Zona Central':
                        valor_excursion = 45000
    return valor_excursion