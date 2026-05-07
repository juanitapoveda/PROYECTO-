"""
Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.


NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """     

    d = {}  # creamos el diccionario para almacenar las peliculas
    d['nombre'] = nombre  # como ya estan definidos los datos que deben entregarse en la funcion entonces, se creara el diccionario con cada una de las variables requeridas
    d['genero'] = genero  # es decir que al diccionario se le otorgara la variable genero ingresada en la funcion y asi sucesivamente con cada una de las variables.
    d['duracion'] = duracion
    d['anio'] = anio
    d['clasificacion'] = clasificacion
    d['hora'] = hora
    d['dia'] = dia
    
    return d  # al final se retorna el diccionario que fue completado con los datos ingresados en el momento de llamar a la funcion

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro.
        None si no se encuentra una pelicula con ese nombre.
    """
    
    peliculas_1=[p1,p2,p3,p4,p5]  #se crea una lista que contenga todos los diccionarios con las peliculas creadas anteriormente para poder iterar y buscar en estos.
    
    for i in peliculas_1: # usamos un bucle for para poder iterar en cada una de las peliculas de la lista.
      if i['nombre']==nombre_pelicula: # usamos un condicional if para buscar la pelicula que coincida con el nombre ingresado en la variable de la funcion
        return i #retornamos i si coincide con el nombre
    
    return None # de lo contrario retornamos none

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    
    peliculas_2 = [p1, p2, p3, p4, p5]  # creamos una lista con todos los diccionarios de las peliculas
    larga = peliculas_2[0] # creamos una variable que empiece desde la primera pelicula de la lista peliculas_2
    
    for i in peliculas_2: # usamos un bucle for para poder iterar en la lista creada
        
        if i['duracion'] > larga['duracion']:  # Usamos un condicional if para establecer 
            larga = i
    
    return larga
    
def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    # sumamos las duraciones de las peliculas de cada diccionario y dividimos entre 5( la cantidad de peliculas)
    promedio = (p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] + p5["duracion"]) // 5

    # sacamos las horas y minutos, dividimos en 60 sin residuo para las horas, y sacamos el mod para los minutos
    horas = promedio // 60
    minutos = promedio % 60

    # retornamos el resultado concactenando las horas y minutos convertidos en str
    return str(horas) + ":" + str(minutos)
   
def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    
    peliculas_3 = [p1, p2, p3, p4, p5]  # creamos una lista con todos los diccionarios de las peliculas
    estrenos = []  # Creamos otra lista donde se guardaran las peliculas que sean estrenos
    
    for i in peliculas_3: # usamos un bucle for para poder iterar en la lista creada
        if i['anio'] > anio:  # usamos un condicional if para encontrar la pelicula que cumpla la condicion de tener como fecha de estreno una fecha superior a la ingresada en la funcion
            estrenos.append(i['nombre'])  # si se cumple la condicion llenaremos la lista de estrenos con el nombre de la pelicula encontrada
    
    if len(estrenos) == 0: # si la lista de estrenos nunca fue rellenada (por ende la longitud de la lista debe ser igual a 0) quiere decir que nop hay peliculas de estrenos, por ende se retorna ninguna
        return "Ninguna"
    else: # de lo contrario si su longitud es mayor a 0, quiere decir que si se encontro almenos una pelicula en estreno por ende se retorna la lista
        return ", ".join(estrenos)  # usamos la funcion join que se encarga de convertir en una str la lista de estrenos y unirlos separandolos en este caso con una coma.
    # retornamos finalmente la lista convertida en una str


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    
    peliculas4 = [p1, p2, p3, p4, p5] # creamos una lista con todos los diccionarios de las peliculas
    contador = 0 # iniciamos un contador en cero para sumar las peliculas con clasificacion +18
    
    for i in peliculas4: # iniciamos un ciclo for para recorrer la lista con los diccionarios
        if i['clasificacion'] == '18+': # usamos un condicional if para identificar que pelicula tiene como clasificacion +18
             contador += 1 # si la condicion se cumple se suma 1 al contador
    
    return contador #una vez recorrida toda la lista se retorna el contador
    

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    peliculas5 = [p1, p2, p3, p4, p5] # creamos una lista con todos los diccionarios de las peliculas para poder iterar en estos
    
    for i in peliculas5: # Con un bucle verificamos que la pelicula no inicie en el mismo dia y hora de otra pelicula
        if i != peli and i['hora'] == nueva_hora and i['dia'] == nuevo_dia:
            return False
        
    for i in peliculas5: # Con un bucle verificaremos que la pelicula no se sobreponga con otras 
        if i != peli and i['dia'] == nuevo_dia:
            # convertiremos las horas nuevas en minutos para verificar que las peliculas no se sobreponen
            inicio_nueva = (nueva_hora // 100) * 60 + (nueva_hora % 100) # dividimos la hora en 100, esto nos dara el total de horas, despues se multiplica por 60 para saber el total de minutos, sacaremos el modulo y lo sumaremos si la hora no es exacta para agregar los minutos faltantes
            
            fin_nueva = inicio_nueva + peli['duracion']
            
            # convertiremos la hora de la otra pelicula
            inicio_i = (i['hora'] // 100) * 60 + (i['hora'] % 100)

            fin_otra = inicio_i + i['duracion']
            
        # verificaremos que la pelicula no se sobreponga
            if inicio_nueva < fin_otra and fin_nueva > inicio_i: # si la nuva inicia antes de que la otra finalice o termina desoues de que la otra inicie entonces sera falso
               return False
    # verificamos requisitos del problema
    if (control_horario == True) and (nuevo_dia in ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']) and (nueva_hora < 600 or nueva_hora >= 2300):
        return False
    
    elif (control_horario == True ) and ('Documental' in peli['genero']) and (nueva_hora >= 2200):
        return False
    
    elif (control_horario == True) and ('Drama' in peli['genero']) and (nuevo_dia == 'Viernes'):
        return False
    
    else:
        peli['hora'] = nueva_hora
        peli['dia'] = nuevo_dia
        
        return True
     
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    # Saco el género del diccionario de la película y el.lower() es para convertir ese texto a minúsculas asi funciona sin dar error si el usuario, llega a ingresarlo en minuscula
    genero = peli["genero"].lower() 

    # Se saca la clasificación del diccionario de la pelicula ingresda en la funcion y se guarda en una variable.
    clasificacion = peli["clasificacion"]

    # usamos un condicional if para saber si se cumple la condicion si tiene 10 años o menos y el género es diferente de "familiar" responde False (No puede entrar, booleano)
    if edad_invitado <= 10 and genero != "familiar":
        return False

    # usamos un condicional if para saber si se cumple la condicion si tiene menos de 15 años y el género es igual a "terror" responde False (No puede entrar, booleano).
    if edad_invitado < 15 and genero == "terror":
        return False

    # empezamos asumiendo que la edad mínima es 0, es decir un caso base para la variable.
    edad_minima = 0
    
    # Si el texto dice "7+" se cambia la variable de edad_minima al número 7, y así con las demás.
    if clasificacion == "7+":
        edad_minima = 7
    elif clasificacion == "13+":
        edad_minima = 13
    elif clasificacion == "16+":
        edad_minima = 16
    elif clasificacion == "18+":
        edad_minima = 18

    # se verifica si el invitado es menor a la edad mínima que acabamos de averiguar.
    if edad_invitado < edad_minima:
        
        # Si la película es un documental, el permiso no sirve y se le niega la entrada.
        if ['Documental'] in peli['genero']:
            return False 
            
        # Si no es documental y si tiene el permiso de los padres, entonces si puede entrar, se retorna true.
        elif autorizacion_padres == True:
            return True
            
        # Si no es documental y no tiene permiso de los papás no puede entrar.
        else:
            return False


    # Si el programa revisó todas las reglas y nunca encontró un "return False" significa que no rompió ninguna regla, así que al final responde True que significa que si puede entrar.
    return True








