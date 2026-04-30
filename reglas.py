def definir_lugares(zona):
        if zona == "Zona Norte":
            lugares = "Salta, Jujuy, o Cataratas del Iguazú"
        elif zona == "Zona Sur":
            lugares = "Bariloche, Chubut, o Tierra del Fuego"
        else:
            lugares = "Buenos Aires, Cordoba, o Mendoza"
        return lugares

def definir_mensaje(temporadas, zona, presupuesto, tipo_viaje, nivel_estres, tipo_hotel, edad, maletas, duracion_estadia, excursiones):
    if  temporadas == "Verano" and zona == "Zona Central" and presupuesto > 80000:
        mensajes += (f"Se le recomienda lugares como {definir_lugares}, que podrían ayudarte a tomarte un descanso.")

    if temporadas == "Otoño" and zona == "Zona Central":
        mensajes += (f"Se le recomienda lugares como {definir_lugares}, y llevar abrigo.")

    if zona == 'Zona Central' and maletas > 2 and tipo_viaje == 'Auto':
        mensajes += (f"Se le recomienda lugares como {definir_lugares}, tener un baul amplio en su vehiculo.")

    if temporadas == "Verano" and zona == "Zona Norte" and presupuesto > 70000:
        mensajes += (f"Se le recomienda lugares como {definir_lugares}, que podrían ayudarte a relajarte.")

    if nivel_estres > 7:
        mensajes += (f" Su nivel de estrés es alto, lugares como {definir_lugares} podrían ayudarle a poder tener unas vacaciones relajadas y así bajar su alto estrés.")
    else:
        if nivel_estres >= 5:
            mensajes += (f"Le podemos recomendar un viaje tranquilo, a lugares como {definir_lugares}, para así bajar un poco el ritmo.")
        else:
            mensajes += (f" Tenés una buena energía, podriamos recomendarte lugares como {definir_lugares} para poder hacer algunas actividades.")

    if tipo_hotel == 5 and presupuesto < 60000:
        mensajes += (" Elegiste un hotel de 5 estrellas, pero el presupuesto no te alcanzará para poder pagar dicha estadia.")

    if edad >= 18 and edad <= 30:
        mensajes += (" Por tu edad, podrías disfrutar de destinos con mucho movimiento y vida nocturna como los antes mencionados.")
    elif edad < 18:
        mensajes += (" Por tu edad, podrías disfrutar de un viaje familiar hacia lugares como los antes mencionados, con actividades tranquilas y seguras.")

    if zona == "Zona Sur" and tipo_viaje == "Auto" and maletas > 2:
        mensajes += (" Si viajas al sur en auto, el trayecto será largo. Aunque usted debería optimizar la cantidad de maletas dentro del auto.")

    if presupuesto < 40000 or duracion_estadia > 10:
        mensajes += (" Teniendo en cuenta tu presupuesto y tu duración en el viaje, te convendría optar por lugares económicos")

    if not excursiones == "Guiada":
        mensajes += (" Si vas a ir por tu cuenta al viaje, tendrás que investigar bien las excursiones antes de viajar al lugar que haya elegido.")

    if nivel_estres > 8 and temporadas == "Invierno" and tipo_hotel >= 4:
        mensajes += (" Vaya, excelente elección mi amigo! Destinos como estos, le podría resultar útil para poder descansar y despejar su mente en esta temporada invernal.")

    if duracion_estadia > 7 and presupuesto <= 50000:
        mensajes += (" Vas a estar varios días en lugares como los antes mencionados. Por lo tanto, recomendamos que organices bien tus gastos! Ya que si usas mucho tu dinero, vas a quedarte corto en presupuesto.")

    if tipo_viaje == "Avión" and zona == "Zona Sur":
        mensajes += (" Buena idea, ya que tomar el avión para viajar a los lugares de la zona sur, ayuda a ahorrar mucho tiempo.")

    if tipo_hotel == 1 or tipo_hotel == 2:
        mensajes += (" Viaje largo con presupuesto ajustado: planificar gastos.")

    if temporadas == "Verano" and nivel_estres > 6 and presupuesto > 70000 and tipo_hotel >= 4:
        mensajes += (" Esto le resultará un viaje ideal, debido a que tendrá un verano de relajación total con un hotel premium.")

    if tipo_viaje == "Colectivo" and zona == "Zona Sur" and duracion_estadia < 5:
        mensajes += (" Viajar al sur en colectivo podría volverse bastante largo. Tal vez te conviene aumentar los días de estadía para aprovechar mejor manera el viaje.")

    if tipo_viaje == "Colectivo" and nivel_estres > 7:
        mensajes += (" Como tenés un nivel de estrés alto, te recomendamos que priorices la comodidad durante el viaje. En trayectos largos en colectivo, podrías sentirte un poco incómodo, por lo que sería bueno elegir asientos más confortables, o considerar otra opción.")

    if tipo_viaje == "Colectivo" and duracion_estadia <= 3:
        mensajes += (" Para viajes cortos, el colectivo puede ser práctico y económico")

    if tipo_viaje == "Colectivo" and zona == "Zona Norte":
        mensajes += (" Viajar en colectivo al norte, es una buena opción. Apesar de ser un viaje largo, te permite viajar de forma más tranquila.")

    if tipo_viaje == "Colectivo" and temporadas == "Verano":
        mensajes += (" Viajar en colectivo en verano te será cómodo gracias al aire acondicionado que posee el mismo, también te recomendamos llevar agua fría y ropa liviana para mayor comodidad.")

    if tipo_viaje == "Colectivo" and zona == "Zona Norte" and presupuesto < 60000 and maletas <= 2:
        mensajes += (" Viajar en colectivo al Norte, te podría resultar accesible para el viaje. Además al no llevar poco equipaje, te resultará viajar mucho mas cómodo.")

    if maletas > 3:
        mensajes += (" Y se recomienda llevar menor equipaje.")
    else:
        mensajes += (" Y su cantidad de equipaje adecuada.")

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
        Valor = costo_hotel
    else: 
        valor = hotel_recomendado
    return valor

def obtener_costo_viaje(zona, temporadas, tipo_viaje):
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
