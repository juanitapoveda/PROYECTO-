"""
Agenda de peliculas.
Modulo de interacci0n por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.

"""
import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict)-> None:
    """Imprime los detalles de la pelicula
    Parametros:
        pelicula(dict): La pelicula de la cual se van a mostrar los detalles
        El diccionario que representa una pelicula contiene las siguientes parejas de
        llave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que dia de la semana se planea ver la pelicula
    """       
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)
    
    if (hora//100 < 10):
        hora_formato = "0"+ str(hora//100)
    else:
        hora_formato = str(hora//100)
    
    if (hora%100 < 10):
        min_formato = "0"+ str(hora%100)
    else:
        min_formato = str(hora%100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)

def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de encontrar la pelicula mas larga.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    print('la pelicula más larga es : ' ) # Mostramos al usuario un mensaje.
    print((larga)) # mostramos la infacion de la pelicula encontrada con la funcion

def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de consultar la duracion promedio de las peliculas.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    
    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5) # llamamos a la funcion desde el modulo
    print("La duración promedio de las películas es: " + promedio + " mins.") # mostramos un mensaje al usuraio con la informacion
    

def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """ Ejecuta la opcion de buscar peliculas de estreno. Esto es: las peliculas que sean 
        mas recientes que un anio dado.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    # Preguntamos parametros
    anio = int(input('Ingrese el año para cosiderar estreno: ')) 
    encontrar= mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio) #operamos funcion
    print(encontrar) #retornamos funcion
    
def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de consultar cuantas peliculas de la agenda tienen clasificacion
    18+.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    mas18 = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5) # llamamos a la funcion desde el modulo
    
    print('hay en total ', mas18, 'peliculas con clasificacion +18') # mostramos un mensaje al usuario con el resultado
    
def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de reagendar una pelicula
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Reagendar una pelicula de la agenda")
    #Preguntamos parametros
    nombre = input("Ingrese el nombre de la pelicula que desea reagendar: ")
    nueva_hora = int(input('Ingrese la nueva hora para agendar la pelicula: (Hora militar) '))
    nuevo_dia = input('Ingrese el nuevo dia para agendar la pelicula: ')
    control_horario = bool(input('El contro horario esta activo? : (True/False) '))
    #Buscamos el diccionario de la pelicula
    pelicula1 = mod.encontrar_pelicula(nombre,p1,p2,p3,p4,p5)

    if pelicula1 is None:
        print("No hay ninguna pelicula con este nombre")
        
    reagendar = mod.reagendar_pelicula(pelicula1, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5) # operamos la funcion
    
    print('La pelicula pudo ser reagendada: ', reagendar) #Mostramos el resultado

def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de decidir si se puede invitar a alguien a ver una pelicula o no.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Decidir si se puede invitar a alguien a ver una pelicula")
    # Preguntamos parametros
    pelicula= input('Ingrese el nombre de la pelicula: ')
    edad= int(input('Ingrese la edad del invitado: '))
    autorizacion= bool(input('Tiene atorizacion de los padres?: (True/False) '))
    
    peli = mod.encontrar_pelicula(pelicula, p1, p2, p3, p4, p5) # buscamos el dic de la pelicula
    invitar = mod.decidir_invitar(peli, edad, autorizacion) 
    
    print('El usuario puede ser invitado: ', invitar)
    
def ejecutar_encontrar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:

    nom_peli = input("Ingrese el nombre de la pelicula: ")
    
    pelicula = mod.encontrar_pelicula(nom_peli,p1,p2,p3,p4,p5)

    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
        
    print(pelicula)
  
def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola.
    Esta funcion primero crea las cinco peliculas que se van a manejar en la agenda.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    pelicula1 = mod.crear_pelicula(
        nombre = "Shrek",  
        genero="Familiar, Comedia", 
        duracion=92, 
        anio=2001, 
        clasificacion='Todos', 
        hora=1700, 
        dia="Viernes")
    pelicula2 = mod.crear_pelicula(
        nombre="Get Out",  
        genero="Suspenso, Terror", 
        duracion=104, 
        anio=2017, 
        clasificacion='18+', 
        hora=2330, 
        dia="Sábado")  
    pelicula3 = mod.crear_pelicula(
        nombre="Icarus",  
        genero="Documental, Suspenso", 
        duracion= 122, 
        anio=2017, 
        clasificacion='18+', 
        hora=800, 
        dia="Domingo")
    pelicula4 = mod.crear_pelicula(
        nombre="Inception", 
        genero= "Acción, Drama", 
        duracion=148, 
        anio=2010,
        clasificacion= '13+', 
        hora=1300, 
        dia="Lunes")
    pelicula5 = mod.crear_pelicula(
        nombre="The Empire Strikes Back", 
        genero= "Familiar, Ciencia-Ficción", 
        duracion=124, 
        anio=1980, 
        clasificacion='7+', 
        hora=1415, 
        dia="Miércoles")   
    
    ejecutando = True
    
    while ejecutando:            
        print("\n\nMi agenda de peliculas para la semana de receso" +"\n"+("-"*50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-"*50)
        
        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-"*50)
        
        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-"*50)
        
        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-"*50)
        
        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente 
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opción para salir 
        de la aplicacion.
    """
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien") 
    print(" 7 - Encontrar pelicula")
    print(" 8 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5) 
    elif opcion_elegida == '7':
        ejecutar_encontrar_pelicula(p1, p2, p3, p4, p5)
    elif opcion_elegida == "8":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando


iniciar_aplicacion()
