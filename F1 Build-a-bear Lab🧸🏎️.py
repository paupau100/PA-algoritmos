"""Integrantes de la scuderia"""
"""Ingeniera de Pista/Software Developer Paula Bernal"""
"""Mecánica Pit Stop/Software Developer Laura Quintero"""
"""Ingeniera de Simulación/Sofware Developer Danna Diaz"""

"""
Módulo de Configuración - F1 Build-A-Bear Lab
Acá tenemos los datos de los accesorios disponibles de una manera organizada.
"""
import time
import os

# Para hacerlo más lindo y ordenado usaremos una función que limpie la terminal
# según el sistema (linux/macOS/Windows)
def limpiar_pantalla() -> None:
    """Limpia la terminal según el sistema operativo para mantener el orden visual."""
    # Pregunta si el sistema operativo es Windows y selecciona el comando para limpiar la consola
    # Condicional inline para ejecutar comando según la variable interna os.name
    os.system('cls' if os.name == 'nt' else 'clear')

# Tenemos una Lista con 10 tipos de peluches originales
PELUCHES_F1 = [
    "McLaren Speed-Bear ($130.000)", "Ferrari Rosso-Teddy ($165.000)", "Mercedes Silver-Cub ($145.000)", 
    "Red Bull Charging-Fluff ($140.000)", "Alpine Blue-Aero ($120.000)", "Haas American-Grizzly ($110.000)", 
    "Cadillac Iron-Paws ($125.000)", "Williams Racing-Classic ($115.000)", "Racing Bulls Honey-Badger ($125.000)", 
    "Audi Neon-Ring ($130.000)"
]

# PRECIOS ASOCIADOS A LA LISTA DE PELUCHES
PRECIOS_PELUCHES = [
    130000, 165000, 145000, 
    140000, 120000, 110000, 
    125000, 115000, 125000, 
    130000
]

# El diccionario con 12 categorías las cuales tienen 12 opciones cada una originales
ACCESORIOS_F1 = {
    "Gorras de Escudería": [
        "Gorra McLaren ($55.000)", "Gorra Ferrari ($60.000)", "Gorra Mercedes ($58.000)", "Gorra Red Bull ($62.000)", "Gorra Alpine ($52.000)", 
        "Gorra Haas ($45.000)", "Gorra Cadillac ($50.000)", "Gorra Williams ($48.000)", "Gorra Racing Bulls ($50.000)", "Gorra Audi ($55.000)", 
        "Visera Plana Paddock ($42.000)", "Gorrito de Lana Mecánico ($38.000)"
    ],
    "Collares y Colgantes": [
        "Cadena Bandera a Cuadros ($32.000)", "Dije Volante de Oro ($45.000)", "Gargantilla Neumático Soft ($26.000)", "Collar Fibra de Carbono ($38.000)", 
        "Cordón VIP Paddock ($22.000)", "Rosario Monza ($34.000)", "Dije Casco Miniatura ($30.000)", "Dije Monoplaza ($35.000)", 
        "Placa Piloto Oficial ($28.000)", "Cadena Plata DRS ($42.000)", "Collar Bujía ($25.000)", "Llavero Mini Pistón ($20.000)"
    ],
    "Camisetas de Piloto": [
        "Jersey Lando Norris ($85.000)", "Jersey Charles Leclerc ($90.000)", "Jersey Lewis Hamilton ($95.000)", "Jersey Max Verstappen ($95.000)", 
        "Jersey Pierre Gasly ($78.000)", "Jersey Alex Albon ($75.000)", "Polo Team Crew ($68.000)", "Camiseta Campeón Mundial ($98.000)", 
        "Remera Retro Ayrton Senna ($105.000)", "Camiseta Técnica Intermedia ($65.000)", "Camiseta Manga Larga Box ($62.000)", "Polo Clásico VIP ($80.000)"
    ],
    "Pantalones y Overoles": [
        "Overol Ignífugo Completo ($110.000)", "Jeans Mecánico Cómodos ($58.000)", "Pantalón de Lona de Boxes ($55.000)", "Short de Verano GP ($45.000)", 
        "Jogger Escudería Negro ($68.000)", "Pantalón Cargo de Telemetría ($72.000)", "Mameluco Grid Girl ($85.000)", "Pantalón Reflectivo ($60.000)", 
        "Mallas Deportivas F1 ($58.000)", "Pantalón Blanco Podio ($75.000)", "Overol de Prácticas ($95.000)", "Short Corto Pitlane ($42.000)"
    ],
    "Manillas y Brazaletes": [
        "Brazalete Acceso VIP ($18.000)", "Manilla Goma Neumático Hard ($15.000)", "Pulsera Cuero F1 ($28.000)", "Brazalete Capitán de Boxes ($22.000)", 
        "Brazalete Sensor Telemetría ($34.000)", "Manilla de Fibra Tejida ($20.000)", "Pulsera Bandera de Largada ($16.000)", "Brazalete Luz LED ($30.000)", 
        "Manilla Silicona Escudería ($15.000)", "Pulsera Acero Inoxidable ($38.000)", "Manilla Hilo Rojo Suerte ($12.000)", "Brazalete Radio Control ($42.000)"
    ],
    "Zapatos Deportivos": [
        "Botas Neopreno Piloto ($68.000)", "Zapatillas Pirelli Amarillas ($62.000)", "Tenis Deportivos Puma F1 ($75.000)", "Mocasines VIP Paddock ($82.000)", 
        "Botas Mecánico Reforzadas ($65.000)", "Zapatillas Confort Boxes ($52.000)", "Tenis Eléctricos Audi ($72.000)", "Botines Clásicos Cuero ($80.000)", 
        "Sandalias de Descanso ($38.000)", "Zapatillas Ultraligeras DRS ($70.000)", "Zapatos Lluvia Extrema ($58.000)", "Tenis Fibra de Carbono ($92.000)"
    ],
    "Cascos Miniatura": [
        "Casco Réplica Mini Hamilton ($95.000)", "Casco Réplica Verstappen ($95.000)", "Casco Réplica Leclerc ($95.000)", "Casco Diseño Retro ($78.000)", 
        "Casco Edición Mónaco ($105.000)", "Casco Cromado Dorado ($115.000)", "Casco Fibra de Carbono Real ($130.000)", "Casco con Visera Polarizada ($90.000)", 
        "Casco Neón Brillante ($85.000)", "Casco Mate Oficial ($88.000)", "Casco Abierto Vintage ($70.000)", "Casco Diseño Especial Japón ($102.000)"
    ],
    "Guantes de Conducción": [
        "Guantes Ignífugos Oficiales ($45.000)", "Guantes Mecánico sin Dedos ($32.000)", "Guantes Cuero Vintage ($52.000)", "Guantes de Agarre Extremo ($42.000)", 
        "Guantes de Silicona Confort ($36.000)", "Guantes Neopreno Lluvia ($38.000)", "Guantes Térmicos Boxes ($35.000)", "Guantes Blancos Podio ($48.000)", 
        "Guantes Costura Externa Piloto ($46.000)", "Guantes Elásticos Ajustables ($34.000)", "Guantes Edición Colección ($60.000)", "Guantes de Práctica ($30.000)"
    ],
    "Mochilas y Bolsos": [
        "Mochila Aerodinámica Piloto ($90.000)", "Bolso Deportivo de Viaje ($98.000)", "Tote Bag Bandera Cuadros ($38.000)", "Mochila Escudería Oficial ($85.000)", 
        "Riñonera Pitlane Cómoda ($48.000)", "Bolso de Herramientas Mini ($55.000)", "Mochila Impermeable Lluvia ($70.000)", "Maletín Ejecutivo VIP ($115.000)", 
        "Mochila Hidratación Activa ($78.000)", "Bolso Bandolera Casual ($52.000)", "Bolso de Lona Paddock ($60.000)", "Mochila Compacta de Viaje ($65.000)"
    ],
    "Chalecos de Seguridad": [
        "Chaleco Reflectivo Boxes ($42.000)", "Chaleco Técnico Multi-bolsillos ($58.000)", "Chaleco Inflable Térmico ($68.000)", "Chaleco de Prensa Oficial ($52.000)", 
        "Chaleco Comisario de Pista ($48.000)", "Chaleco VIP Acolchado ($65.000)", "Chaleco de Neopreno Ligero ($46.000)", "Chaleco Deportivo sin Mangas ($45.000)", 
        "Chaleco de Cuero Vintage ($82.000)", "Chaleco Amarillo Seguridad ($38.000)", "Chaleco Naranja Rescate ($40.000)", "Chaleco Técnico Ligero ($50.000)"
    ],
    "Parches y Pines Decorativos": [
        "Pin Volante F1 Oro ($16.000)", "Parche Bandera Cuadros ($12.000)", "Pin Neumático Pirelli ($15.000)", "Parche Logo Escudería ($14.000)", 
        "Pin Casco Miniatura ($15.000)", "Parche Podio Número 1 ($12.000)", "Pin Monoplaza de Plata ($18.000)", "Parche Circuito de Spa ($14.000)", 
        "Pin Copa de Campeón ($16.000)", "Parche Tuerca de Box ($10.000)", "Pin Semáforo de Salida ($15.000)", "Parche Laureles de Victoria ($12.000)"
    ],
    "Llaveros y Colgantes del Oso": [
        "Llavero Pistón Miniatura ($15.000)", "Cinta Cuello Pase VIP ($18.000)", "Llavero Silbato Oficial ($14.000)", "Colgante Oso Piloto ($22.000)", 
        "Llavero Rueda de Goma ($16.000)", "Cinta Cuello Bandera Cuadros ($15.000)", "Llavero Mosquetón Aluminio ($12.000)", "Colgante Mini Volante ($20.000)", 
        "Llavero Cronómetro ($18.000)", "Cinta Cuello Color Escudería ($16.000)", "Llavero Bujía Plateada ($15.000)", "Llavero Medalla Campeón ($22.000)"
    ]
}

# MATRIZ DE PRECIOS RELACIONADA POR POSICIÓN DE ÍNDICE
PRECIOS_ACCESORIOS = {
    "Gorras de Escudería": [55000, 60000, 58000, 62000, 52000, 45000, 50000, 48000, 50000, 55000, 42000, 38000],
    "Collares y Colgantes": [32000, 45000, 26000, 38000, 22000, 34000, 30000, 35000, 28000, 42000, 25000, 20000],
    "Camisetas de Piloto": [85000, 90000, 95000, 95000, 78000, 75000, 68000, 98000, 105000, 65000, 62000, 80000],
    "Pantalones y Overoles": [110000, 58000, 55000, 45000, 68000, 72000, 85000, 60000, 58000, 75000, 95000, 42000],
    "Manillas y Brazaletes": [18000, 15000, 28000, 22000, 34000, 20000, 16000, 30000, 15000, 38000, 12000, 42000],
    "Zapatos Deportivos": [68000, 62000, 75000, 82000, 65000, 52000, 72000, 80000, 38000, 70000, 58000, 92000],
    "Cascos Miniatura": [95000, 95000, 95000, 78000, 105000, 115000, 130000, 90000, 85000, 88000, 70000, 102000],
    "Guantes de Conducción": [45000, 32000, 52000, 42000, 36000, 38000, 35000, 48000, 46000, 34000, 60000, 30000],
    "Mochilas y Bolsos": [90000, 98000, 38000, 85000, 48000, 55000, 70000, 115000, 78000, 52000, 60000, 65000],
    "Chalecos de Seguridad": [42000, 58000, 68000, 52000, 48000, 65000, 46000, 45000, 82000, 38000, 40000, 50000],
    "Parches y Pines Decorativos": [16000, 12000, 15000, 14000, 15000, 12000, 18000, 14000, 16000, 10000, 15000, 12000],
    "Llaveros y Colgantes del Oso": [15000, 18000, 14000, 22000, 16000, 15000, 12000, 20000, 18000, 16000, 15000, 22000]
}

def mostrar_bienvenida() -> None:
    """Muestra un banner dinámico de bienvenida al usuario."""
    limpiar_pantalla()
    print("🏎️" * 55) # Imprime una línea decorativa de 22 carritos 
    # Usamos For para una animación de las dos líneas de saludo
    for linea in ["🏎️   ¡BIENVENIDO A LA F1 BUILD-A-BEAR LAB!   🏎️", "Empieza a diseñar tu peluche de F1, crea el peluche de tus sueños!."]:
        print(linea)
        time.sleep(0.3) # Detiene el programa por 0.3 segundos para un efecto visual
    print("🏎️" * 55) # Cierra la decoración de carritos

def seleccionar_base_peluche() -> str: 
    # Usamos while true para validar que la entrada sea correcta 
    while True: # Ciclo infinito hasta que el usuario elija un número válido
        print("\n--- 🧸PASO 1: SELECCIONAL TU BASE DE PELUCHE🏎️ ---")
        
        # Recorremos la lista con for e in range
        for i in range(len(PELUCHES_F1)): # El sistema cuenta cuántos osos hay y genera la secuencia numérica indexada
            print(f"{i + 1}. {PELUCHES_F1[i]}") # Muestra la lista del 1 al 10 emparejando el nombre en su posición exacta
                                                
        try: # Python intentará ejecutar lo que está acá dentro para capturar errores de entrada
            opcion = int(input("\nIngresa el número de la escudería elegida: ")) # Se detiene a esperar la respuesta del usuario
            
            # Condicionales if/else para validar que el rango numérico sea el correcto
            if 1 <= opcion <= len(PELUCHES_F1): # Revisa que esté dentro de las opciones que mostramos arriba
                # Operación de acceso directo por índice O(1)
                peluche_elegido = PELUCHES_F1[opcion - 1] # Le resta 1 para adaptarlo al sistema de índices que arranca en 0
                print(f"\n✅ ¡Excelente elección! Has seleccionado: {peluche_elegido}")
                return peluche_elegido # Retorna el oso seleccionado y rompe el bucle de inmediato
            else: # Si meten un número fuera de rango el condicional da falso y salta acá
                print("❌ Número fuera de rango. Por favor, selecciona una opción válida.")
                
        except ValueError: # Si el usuario digita letras o símbolos, este bloque evita que el programa se rompa
            print("❌ Entrada inválida. Debes ingresar un número entero.")
            
        time.sleep(1.5) # Pausa estética de seguridad para que el usuario alcance a leer el mensaje de error

def personalizar_accesorios() -> list:
    """
    Menú multinivel para escoger accesorios entre 12 categorías con 12 opciones cada una.
    Al terminar la selección, retorna la lista completa con los ítems comprados.
    """
    carrito_accesorios = [] # Iniciamos una 'lista' vacía para ir guardando los accesorios que elija
    contador_accesorios = 0 # Variable especial para llevar la cuenta de artículos en tiempo real
    categorias = list(ACCESORIOS_F1) # Extraemos las llaves del diccionario para convertirlas en una lista navegable de categorías

    while True: # El usuario se mantendrá en este menú principal hasta que decida finalizar la orden
        limpiar_pantalla()
        print(f"\n--- PASO 2: TALLER DE PERSONALIZACIÓN (Accesorios: {contador_accesorios}) ---")
        # El print de arriba le muestra dinámicamente al cliente cuántas cosas lleva en su carrito
        print("Selecciona una categoría de accesorio para tu peluche:\n")
        
        # Imprimiremos las categorías disponibles mapeando la lista con un for
        for i in range(len(categorias)): # Enumeramos las categorías del 1 al 12
            print(f"{i + 1}. {categorias[i]}")
        # Insertamos manualmente una última opción al final de la lista para gestionar la salida
        print(f"{len(categorias) + 1}. 🏁 Finalizar diseño del peluche y ver tu orden")
        
        try: 
            opcion_categoria = int(input("\nSelecciona una categoría (o finaliza): "))
            
            # Condicional para interceptar si el usuario marca la opción de salida (el número 13)
            if opcion_categoria == len(categorias) + 1:
                if contador_accesorios == 0: # Control de seguridad por si intenta irse con las manos vacías
                    print("\n⚠️ ¡Tu peluche irá desnudo a la pista! No seleccionaste accesorios.")
                    confirmar = input("¿Deseas finalizar de todas formas? (s/n): ").lower()
                    if confirmar == 's': # Si confirma, rompemos el ciclo y dejamos que avance
                        break
                    else: # Si se arrepiente, ignoramos la salida y lo devolvemos al menú principal
                        continue 
                else: # Si el carrito ya tiene ropa o pines, cerramos el diseño con éxito
                    print("\n🏁 ¡Diseño completado con éxito! Preparando el podio...")
                    break 
            
            # Validamos que la categoría seleccionada exista dentro del rango real (1-12)
            if 1 <= opcion_categoria <= len(categorias):
                categoria_seleccionada = categorias[opcion_categoria - 1] # Ajustamos el índice restando 1
                # Obtenemos el listado de accesorios que corresponden a esa clave del diccionario
                lista_items = ACCESORIOS_F1[categoria_seleccionada]
                
                # Entramos al submenú interno para desglosar la categoría elegida
                while True:
                    limpiar_pantalla()
                    print(f"\n--- ACCESORIOS DISPONIBLES EN: {categoria_seleccionada.upper()} ---")
                    
                    for j in range(len(lista_items)): # Mapeamos y listamos las 12 opciones internas del producto
                        print(f"{j + 1}. {lista_items[j]}")
                    print("13. ↩️ Volver al menú anterior") # Cláusula de escape para dar marcha atrás sin comprar
                    
                    opcion_item = int(input("\nSelecciona el accesorio que deseas añadir: "))
                    
                    if opcion_item == 13: # Si digita 13, abortamos el submenú y regresamos al catálogo de categorías
                        break 
                        
                    if 1 <= opcion_item <= 12: # Si el ítem es válido, lo procesamos
                        item_elegido = lista_items[opcion_item - 1]
                        carrito_accesorios.append(item_elegido) # Empujamos el string del accesorio al arreglo global
                        contador_accesorios += 1 # Actualizamos el acumulador de prendas
                        
                        print(f"\n✨ ¡'{item_elegido}' añadido a tu peluche!")
                        input("\nPresiona Enter para continuar...")
                        break # Volvemos al menú de categorías para que pueda seguir combinando artículos
                    else:
                        print("❌ Opción inválida. Intenta nuevamente.")
                        time.sleep(1)
            else:
                print("❌ Categoría no válida.")
                time.sleep(1)
                
        except ValueError: # Captura errores de entrada tipo string cuando se esperan enteros en los menús
            print("❌ Error de formato. Ingresa solo números enteros.")
            time.sleep(1.5)
            
    return carrito_accesorios # Al romper los ciclos, despachamos el carrito con las elecciones hechas


def mostrar_recibo_final(peluche: str, accesorios: list) -> None: # Esta función a diferencia de las demás tiene parámetros
    # 'peluche' el cual espera recibir una cadena de texto (ej: nombre del oso elegido con su precio)
    # 'accesorios' el cual espera recibir una lista con todos los strings de los accesorios guardados en el carrito 
    """
    Muestra los detalles de la creación del usuario y calcula el total de forma matemática.
    """
    limpiar_pantalla() # Llamamos a la función que nos limpie la terminal
    # Ahora imprimiremos el diseño de la factura 

    print("\n" + "🏁 " * 15) # Estamos multiplicando strings para repetir 15 veces eso en una línea 
    print("   [LIVE] F1 BEAR GARAGE - CONFIGURATION REPORT  ")
    print("" + "🏁 " * 15)
    # Generamos la línea superior e inferior del título 

    # Buscamos la posición exacta del oso en la lista global para extraer matemáticamente su costo equivalente
    idx_peluche = PELUCHES_F1.index(peluche)
    precio_base = PRECIOS_PELUCHES[idx_peluche]
    total_compra = precio_base # Inicializamos el acumulador de la factura con el valor base del muñeco

    print(f"\n CHASSIS DEV : {peluche.upper()}") # Acá metemos variables dentro del texto usando llaves y transformamos el texto a mayúsculas
    # En F1 los códigos del chasis siempre van en mayúsculas (ej: SF-24, RB20)
    print(f" UPGRADES    : {len(accesorios)} Componentes Equipados") # Cuenta cuántos elementos hay dentro de la lista y retorna el número exacto
    print("-" * 58) # Dibuja una línea divisoria usando 58 guiones (se ensanchó para dar espacio a los textos de los precios)
    print(" STG | COMPONENTE DETECTADO                | ESTADO   ") # Son los títulos tipo base de datos de Telemetría
    print("-" * 58) # Dibuja una línea divisoria usando 58 guiones

    # Desglose de la lista de accesorios estilo posiciones de carrera (P1, P2...)
    for i, acc in enumerate(accesorios, start=1): # Le estamos pidiendo que empiece a contar desde 1 
        precio_acc = 0
        # Escaneamos el diccionario buscando a qué categoría pertenece el accesorio para heredar su precio
        for cat, items in ACCESORIOS_F1.items():
            if acc in items:
                idx_acc = items.index(acc) # Sacamos el índice exacto del accesorio dentro de su sublista
                precio_acc = PRECIOS_ACCESORIOS[cat][idx_acc] # Cruzamos ese índice con la matriz numérica de costos
                break # Rompemos este ciclo interno al encontrar la coincidencia de precio
        
        total_compra += precio_acc # Sumamos el valor del accesorio actual al gran total de la orden
        print(f" P{i:<2} | {acc:<35} | [ READY ]") # La variable 'i' guarda la posición, 'acc' el nombre con precio y mantiene la alineación de columnas

    print("-" * 58) # Dibuja una línea divisoria usando 58 guiones
    # LÍNEA IMPRESA: Muestra el costo total acumulado con el formato matemático de miles reemplazando comas por puntos
    print(f" >>> COSTO TOTAL DEL MONOPLAZA: ${total_compra:,} COP".replace(',', '.'))
    print("-" * 58) # Dibuja una línea divisoria usando 58 guiones
    print(" STATUS: Pit-stop listo. Monoplaza (Peluche) a pista. 🏎️💨\n") # Imprimimos una línea final confirmando que el 'coche' peluche está listo para salir del garage
    return total_compra # Despachamos el valor final de la sumatoria para que la pasarela lo reciba

def metodo_de_pago(total: int) -> None: # Declaramos la función que procesa la pasarela, recibe el total calculado en la factura
    """permite al usuario elegir el metod de pago para finalizar la compra"""
    while True: # Hace que el menú se repita de forma obligatoria hasta que el usuario elija una opción válida
        print("\n--- PASO 3: MÉTODO DE PAGO ---")
        print("1 Targeta de credito")
        print("2 Targeta de débito")
        print("3 Nequi")
        print("4 Daviplata")
        print("5 Efectivo")
        
        try: # Python intentará validar que lo ingresado no rompa el tipo de dato esperado
            opcion_pago = int(input("\nSelecciona tu método de pago: ")) # Se detiene a esperar el número del usuario
            # Usamos match case para manejar las opciones de pago de forma clara y ordenada (evalúa el caso numérico)
            match opcion_pago:
                case 1:
                     print("\n Pago con tarjeta de credito ")
                     break # Sale del bucle si la opción es válida y finaliza la transacción
                case 2: 
                    print("\n Pago con tarjeta de débito ")
                    break
                case 3:
                    print("\n Pago con Nequi ")
                    break
                case 4:
                    print("\n Pago con Daviplata ")
                    break
                case 5:
                    print("\n Pago en efectivo ")
                    break
                case _: # Funciona como un 'else'; se ejecuta si ponen cualquier otro número (ej: 8 o -2)
                    print("metodo invalido")
        except ValueError: # Si el usuario mete letras, palabras o símbolos en el campo numérico salta acá
            print("Debes ingresar un nuemero") # Evita el cierre forzado del programa y lo devuelve al inicio del menú de pagos
            
    print("Compra finalizada con éxito. ¡Gracias por elegir F1 Build-A-Bear Lab! 🏎️🧸")

def main() -> None: # Coordinamos el orden de ejecución con la función main, es una función sin parámetros
    mostrar_bienvenida() # Limpia la pantalla y muestra el banner de bienvenida de F1
    time.sleep(1) # Pausa un segundo para que se alcance a leer el saludo inicial
    
    # Asignación del resultado de las funciones modulares a variables locales
    base_peluche = seleccionar_base_peluche() # Llamamos la función que permite elegir el peluche, espera la selección y la guarda en la variable
    accesorios_elegidos = personalizar_accesorios() # Abrimos el taller multinivel y guarda el arreglo final en 'accesorios_elegidos'
    
    # Capturamos el retorno de la factura (el total numérico de la compra) en una nueva variable local
    total_final = mostrar_recibo_final(base_peluche, accesorios_elegidos) # Toma los datos guardados, calcula y dibuja el reporte
    metodo_de_pago(total_final) # Le pasa el costo total a la pasarela para ejecutar el cobro y cerrar el programa


if __name__ == "__main__":
     main() # Se encarga de disparar y arrancar absolutamente todo al ejecutar el archivo directo