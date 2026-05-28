# PA-algoritmos
Proyecto Algoritmos PA 


DESCRIPCIÓN GENERAL:
Este programa es un simulador de consola interactivo que permite a los usuarios 
diseñar y personalizar un peluche temático de Fórmula 1. Integra el uso de estructuras 
de datos avanzadas, control de flujo defensivo ante errores de usuario, y una interfaz 
limpia y dinámica por terminal.


INTEGRANTES DE LA SCUDERIA:
- Paula Bernal (Ingeniera de Pista / Software Developer)
- Laura Quintero (Mecánica Pit Stop / Software Developer)
- Danna Diaz (Ingeniera de Simulación / Software Developer)

Laura realizo los puntos del txt:
Diccionarios


Listas


Funcionalidades del sistema

Del código:
Realizó el código de la pasarela de pagos






Paula realizó 
La descripción general del txt
Del código:
Código Base 


Creo el repositorio


Realizó Estructura del Programa, Menús y Control de Errores








Danna realizó los puntos del txt
Manejos de errores


Talleres de accesorios
Reporte facturación


Del código:
Montó el código para sacar precios y total de la compra

-------------------------------------
FUNCIONALIDADES GENERALES DEL SISTEMA
-------------------------------------
 Algorithm_Proyect

Contiene el proyecto en el que usar todos los temas vistos en clase tales como:

1. Funciones (def)
2. Parámetros y retorno (return)
3. Variables
4. Listas
5. Diccionarios
6. Ciclos while
7. Ciclos for
8. Condicionales
9. Manejo de errores
10. match-case
11. Entrada y salida de datos
12. Comentarios y documentación

---CONTENIDO---

Explicación:
El codigo correponde a un sistema interactivo creado en Python llamado “F1 Build-A-Bear Lab”, cuyo objetivo es permitirle al usuario crear peluche desde cero con accesorios personalizados de formula 1 mediante menus de consolas. El programa combina conceptos de programación estructurada, manejo de datos, validaciones, interacción con el usuario y simulación de un sistema de compras.

El sistema permite hacer:
- Seleccionar un peluche base
- Personalizarlo con accesorios
- Calcular el precio total
- Mostrar una factura detallada
- Elegir un método de pago
- Finalizar la compra

El código utiliza múltiples estructuras y herramientas propias de Python, integrando buenas prácticas de programación modular y validación de errores.

El programa utiliza estructuras de lista para para almancer lo que son los datos de la tienda ordenadamente:

* La lista PELUCHES_F1[]
Esta lista guarda los nombres de los peluches disponibles. Donde cada posicion almacena:
  - Nombre 
  - Tipo 
  - Precio 
Esta lista sirve para relacionar los peluches con sus precios y permite que el usuario ver y selecionar un peluche.

* Lista de precios de los peluches
Esta guarda los precios de los peluches numericamente para poder:
  - Sumarlo
  - Calcular el total 
  - Hacer la factura 
Se relaciona por indice de posicion.

* DICCIONARIO
Un diccionario guarda datos usando Clave: valor. El diccionario en el codigo se ultiliza para almacenar los datos de ACCESORIOS_F1.
Esta contiene 12 categorias y cada categoria contiene 12 accesorios. Permite organizar los accesorios por categorías, así el usuario puede navegar como en una tienda real.

* Diccionario de PRECIOS_ACCESORIOS
Guarda los precios numericos de los accesorios. Cada accesorio tiene el mismo indice que su precio.


FUNCIONES DEL SISTEMA:

* Función limpiar_pantalla()
Esta funcion limpia la terminal utilizando la libreria os ejecutando este comnado en sistema operatipo:
os.system('cls' if os.name == 'nt' else 'clear')
Lo que que hace es ue preguta que sistema operrativo tiene el usuario:
  - si tiene Windows = nt utiliza cls
  - si tiene otro utiliza clear 
Luego ejecuta el comando en la consola.


* Función mostrar_bienvenida()
Muestra la pantalla de bienvenida que consta de limpiar la consola antes de mostrar el menú, imprimeir 55 carritos, ultizar un ciclo for para recorrer una lista de mensaje y luego hacer una pausa de 0.3 segundos para crear animacion con la libreria import time, utilizando el cmando time.sleep(0.3) y cierra con una decoracion de carritos.


-------------------------------------
Sección de base de errores (Función 'seleccionar_base_peluche')
-------------------------------------
¿Qué hace exactamente?: Es el paso inicial de la compra, muestra al usuario los peluches que en este caso son osos disponibles para que elija uno y se asegura de que no digite algo incorrecto.

¿Cómo funciona por dentro?: Realiza un ciclo repetitivo while, que no se detiene hasta que el usuario ponga una opción correcta, Realiza la cuenta de los elementos de 'PELUCHES_F1' y los pinta en la pantalla alumnos del 1 al 10. Cuando el usuario escribe su opción, la función la pasa por dos items de seguridad:
  - Filtro 1 : Si el usuario escribe una letra como la "A" o se equivoca, el programa normalmente se fracturaria y se cerraría. Esta función atrapa ese error, evita que el juego se dañe, le muestra un mensaje que diga que es erroneo y le vuelve a preguntar.
  - Filtro 2 : Si el usuario escribe un número que no existe en la lista que manda ejemplo 35 o -1, la función se da cuenta de que no esta en el rango de la lista a elegir, le dice que no existe y lo regresa al principio del ciclo para que vuelva a intentar.
  - Despacho: Cuando el usuario por fin digita un número del 1 al 10, la función le resta 1 , saca el nombre del oso elegido, rompe el ciclo y se lo manda al resto del programa.


-------------------------------------
Taller de accesorios (Función 'personalizar_accesorios')
-------------------------------------
¿Qué hace exactamente?: Es el Paso 2 es lo mas divertido, es una tienda de secciones donde puedes meterle cuanta ropa y accesorios quieras a tu oso.

¿Cómo funciona por dentro?: Crea una lista vacía llamada 'carrito_accesorios', que es como si fuera un carrito de compras y pone un contador de cosas en 0.
  - Sección 1: Muestra las 12 categorías de ropa y una opción extra que es el 13 que dice "Finalizar", si intentas presionar "Finalizar" sin haber comprado nada el contador quedara en 0, la función se detiene y te lanza una advertencia: "¡Tu peluche va a ir desnudo a la pista! ¿Estás seguro?". Si dices que sí, te deja pasar, si dices que no, te regresa a comprar.
  - Sección 2 : Si eliges una categoría por ejemplo, la opción 1 que son Gorras, la función viaja al diccionario 'ACCESORIOS_F1', saca las las gorras disponibles y te las muestra en una pantalla limpia junto con una opción para "Volver atrás" la 13, si elige un producto, este se guarda en tu bolsa de compras ('carrito_accesorios'), se suma 1 al contador y te regresa automáticamente al menú de categorías para que sigas comprando otra cosa si quieres, cuando decides finalizar, le entrega tu bolsa llena de compras al siguiente paso.


-------------------------------------
Reporte de facturación (Función 'mostrar_recibo_final')
-------------------------------------
¿Qué hace exactamente?: Es la factura de cobro, pero diseñada como si fuera una pantalla de datos de los pits de la Fórmula 1. Calcula el precio de todo lo que armaste.

¿Cómo funciona por dentro?: Esta función recibe dos datos: el oso que elegiste en el Paso 1 y la bolsa de accesorios que armaste en el Paso 2. 
  - Primero, va a la lista 'PELUCHES_F1' para saber en qué posición estaba tu oso, saca el precio de la lista de números ('PRECIOS_PELUCHES') y arranca la cuenta con ese valor.
  - Luego, revisa uno por uno los accesorios que compraste, por cada accesorio, hace un rastreo rápido dentro de los cajones del catálogo para saber a qué categoría pertenece, averigua su posición y va a los precios de accesorios para sacar el costo en número y sumarlo al total.
  - Al final, toma ese gran total y le hace un arreglo estético: le pone los puntos de los miles para que se lea como dinero de Colombiano por ejemplo, transforma 315000 en $315.000 COP y le pasa ese número para el final del cobro .


-------------------------------------
7. PASARELA DE PAGO CON CONTROL DE FLUJO (Función 'metodo_de_pago')
-------------------------------------
¿Qué hace exactamente?: Es el Paso 3 y el final de la experiencia, te realiza el cobro del dinero total y cierra el programa.

¿Cómo funciona por dentro?: Recibe el precio total que calculó la función anterior, abre un ciclo para asegurarse de que pagues bien y te muestra 5 opciones en pantalla: Tarjeta de Crédito, Débito, Nequi, Daviplata o Efectivo, se usa una estructura llamada 'match-case' que funciona como un desviador de caminos: si marcas 1 va por el camino de crédito, si marcas 3 va por Nequi, etc. Si marcas cualquier otro número o una letra, te dice que el método es inválido y te vuelve a preguntar. Una vez que seleccionas un método correcto, el programa simula el pago con éxito, te da un mensaje de agradecimiento, te dice que tu oso ya va para la pista y cierra el programa de forma segura.
