

# ****************************** CADENAS ***************************************************************************************
c1 = "Cadena1,otra,mari,posa"
c2 = "Cadena2"
res = c1 * 3 # => Cadena1Cadena1Cadena1

c1 in c2 #True si c1 contenida en c2 sino False.
c1 not in c2 #Devuelve True si c1 es una cadena no contenida en c2 y False en caso contrario.

len(c1) # Nº de caracteres cadena c.
min(c1) #: Menor de la cadena c.
max(c1) #: Mayor de la cadena c.
c1 = c1.upper() #: mayúsculas devuelve asi Modifica puedes crear nuevas tambien
c1 = c1.lower() #: minúsculas.
c1 = c1.title() #: Capital "Editorial".
nuevaLista = c1.split(",") #:lista separadas por delimitador

#RANDOM

import random
ale = random.randint(0, 5) #incluye ambos

ale_float = random.uniform(1.5, 5.5) #incluye decimales

ale_random = random.random()  # Genera un número flotante entre 0 y 1

mi_lista = [10, 20, 30, 40, 50]

ale = random.choice(mi_lista)  # Elige un valor aleatorio de mi_lista

random.shuffle(mi_lista)  # Mezcla los elementos de la lista

muestra = random.sample(mi_lista, 3)  # Elige 3 elementos aleatorios sin repetición


# ******************************   FICHEROS  ***************************************************************************************


"""  
r   Lectura
r+  Lectura y escritura
w   Solo escritura / sobrescribe si existe / crea archivo si no existe
w+  Escritura y lectura
a   Agrega Contenido
a+  Agrega y Lee

t   abre fichero modo texto
b   abre fichero modo binario
"""

import csv
import os

#LEER  -------------------------------------------------------------------------------------
jugadores = []
with open('jugadores.csv', encoding='utf8', mode='r')as f:
    lector = csv.DictReader(f)
    
    for i in lector:
        nombre = i['nombre'].strip()
        apellido = i['apellido'].strip()
        Lista = [nombre, apellido,0,0,0,0,0,0,0]
        jugadores.append(Lista)	

#Lee y Si el fichero esta vacio inserta datos ----------------------------------------------

reviza = []
dataEjemplo =["Fernando",1,2,3,4]
if os.path.isfile('./datos.csv'):
    with open('./datos.csv', encoding='utf8', mode='r')as f:  #modo r IMPORTANTE

         if os.path.getsize('./datos.csv') == 0:  #devuele Nº de carateres existentes
                print("entro")

                escritor = csv.writer(f)
                escritor.writerow( ['nombre','v1','v2','v3','v4']) #cabecera

                for item in dataEjemplo:
                    escritor.writerow( item ) # agrega datos ejemplo


# ESCRIBIR ---------------------------------------------------------------------------------

if os.path.isfile("./jugadores.csv"):
    with open('jugadores.csv', encoding='utf8', mode='w', newline='' ) as f:

        escritor = csv.writer(f)
        
        escritor.writerow(['nombre','apellido']) #escribe encabezado
        escritor.writerow(['Fernando','Chang'])	
        escritor.writerow(['Josefina','Garcia']) 


# ***************** LISTAS | TUPLAS | DICCIONARIOS | CONJUNTOS *****************************

lista1 = ["Manzana", "Peras","mandarinas","piña","Azucar",10]
lista2 = [2,3,5,25,8,10]
#ordenar una lista por un campo especifico -------------------------------------------------
Lista = [
	['Pilar', 'Zamora', 22, 8, 31, 41, 46, 17, 28, 0],
	['Pedro', 'Almadovar', 28, 2, 39, 33, 16, 37, 36, 0]
]

Lista.sort(key=lambda x: [1])  #indicamos INDICE x el q se quiere ordenar

#Creación
muestra = list(lista2) # crea usando datos de una coleccion existente

#Sub Lista
print( lista1[1: 4]) # del indice 1 hasta el 3 [el 4 - 1]
print ( lista1[1: 6: 2]) # lista1[i: j: k]  i: indice | j: tope | k: pasos 

# --- LISTAS Operaciones que NO Modifican Listas ***************************************************************

len(lista1) 
min(lista1) 
max(lista1) 
sum(lista2)

#dato in lista :True si esta / False si no.
print ('uvas' in lista1) # if 'uvas in lista1: ...

indices_uvas = [i for i, x in enumerate(lista1) if x == 'uvas'] #obtienes todos los indices de uvas ( esto es si hay varias existencias de 1 valor)

# lista.index(dato) : indice del dato
print( lista1.index('uvas')) 

# lista.count(dato) : Número de veces que el valor dato está contenido en la lista l.
print ( lista1.count('uvas'))

valor = all(lista1) # Devuelve True si todos los elementos son "verdaderos" (o si la lista está vacía).
valor2 = any(lista1) # Devuelve True si al menos un elemento es "verdadero".

# --- LISTAS Operaciones que SI Modifican Listas ***************************************************************

nuevaLista = lista1+lista2 #NO MODIFICA Crea una nueva lista concatenando l1 y l2.

lista1.clear() #limpia la lista

lista1.append('dato') # Añade dato al final de lista.

lista1.extend(lista2) # Añade los datos al final SI MODIFICA.

lista1.insert(2, 'Nueva Cadena') #Inserta dato en la posición índice de la lista l y desplaza los elementos desde índice.

lista1.remove('datiles') # Elimina el primer elemento con valor dato en la lista l y desplaza los que están por detrás de él una posición hacia delante.

ExtraeBorraItemLista = lista1.pop(3) # Devuelve el dato en la posición índice y lo elimina de la lista l, desplazando los elementos por detrás de él una posición hacia delante.

lista1.sort() #Ordena los elementos de la lista l de acuerdo al orden predefinido, siempre que los elementos sean comparables.


"""
 *********** *********** *********** ***********  DICCIONARIOS **********************************************************************************************
"""

 #Diccionario
edades_estudiantes = {
    "Ana": 20,
    "Luis": 22,
    "María": 19,
    "Carlos": 21
}
print( f"edad de Luis {edades_estudiantes['Luis']}" )

#AGREGAR Diccionario / MODIFICAR
edades_estudiantes["Sofia"]= 63 

#ELIMINAR
del edades_estudiantes["Ana"]

# Uso de get()  
print (f"Muestro con Get: {edades_estudiantes.get('Sofia')}")

print("Mensaje de Error:", edades_estudiantes.get("Korra", "No se encontró"))

#--------------------------------------------------------------- Recoger valores solo de Llaves
claves = edades_estudiantes.keys() 
print(claves) # dict_keys(['Luis', 'María', 'Carlos', 'Sofia'])

claves = list(edades_estudiantes.keys())  # Convertimos las claves a lista
print(claves[2])  # Accedemos al índice 2 → "Carlos"

#----------------------------------------------------------------- recoger valores del diccionario
valores = edades_estudiantes.values()
print(valores) # dict_keys(['Luis', 'María', 'Carlos', 'Sofia'])

# ------------------------------------------------------------------Obtener los pares clave-valor del diccionario

items = edades_estudiantes.items() # dict_items([('Luis', 22), ('María', 19), ('Carlos', 21), ('Sofia', 63)])

grupos = list( edades_estudiantes.items() )
print(grupos[0][0]) # Luis

for i in grupos:
    print ( f"nombre: {i[0]} edad: {i[1]}" )

#------------------------------------------------------------------- ---------------------------------Comprobar si existen valores en el diccionario
print (f"Esta Clara en la lista: {'Clara' in edades_estudiantes}")  #Esta Clara en la lista: False

#----------------------------------------------------- Suma de valores
print( sum(edades_estudiantes.values()) ) #125

# ----------------------------------------- max valore de las LLaves Claves
max_clave = max(edades_estudiantes) 
print(max_clave)

# ---------------------------------longitud diccionario
print ( len(edades_estudiantes) ) 


#************************************ TUPLAS **********************************************************************************************
mi_tupla = ('Pilar', 'Zamora', 22, 8, 31, 41, 46, 17, 28, 0)

# Acceso a elementos de la tupla (índice)
print(mi_tupla[1])  # 'Zamora'

# Operaciones en tupla (no modifica la tupla)
print(len(mi_tupla))  # Longitud de la tupla
print(min(mi_tupla))  # Valor mínimo (si son comparables)
print(max(mi_tupla))  # Valor máximo (si son comparables)
print(sum([22, 8, 31, 41, 46, 17, 28, 0]))  # Suma de los valores numéricos

# 'in' verifica si el elemento está en la tupla
print('Zamora' in mi_tupla)  # True

# El índice de un elemento
print(mi_tupla.index('Zamora'))  # 1 (posición en la tupla)

# Contar las ocurrencias de un valor en la tupla
print(mi_tupla.count(8))  # 1

#--------------------------------------------------- CONJUNTOS ===================================================================


mi_conjunto = {22, 8, 31, 41, 46, 17, 28} # Conjunto (colección sin elementos duplicados y sin orden)

# Operaciones en conjunto (no permiten duplicados)
mi_conjunto.add(0)  # Añadir un nuevo elemento
print(mi_conjunto)  # {0, 8, 17, 22, 28, 31, 41, 46}

# Eliminar elemento (sin error si no existe)
mi_conjunto.discard(22)

# Eliminar y devolver el elemento arbitrario
elemento = mi_conjunto.pop()
print(elemento)  # Devuelve y elimina un elemento aleatorio

# Comprobar si un elemento está en el conjunto
print(8 in mi_conjunto)  # True

# Operaciones matemáticas de conjuntos
otro_conjunto = {31, 22, 8}
union_conjuntos = mi_conjunto.union(otro_conjunto)  # Unión de conjuntos
print(union_conjuntos)  # {8, 17, 31, 22, 28, 41, 46}

# Intersección de conjuntos
interseccion_conjuntos = mi_conjunto.intersection(otro_conjunto)
print(interseccion_conjuntos)  # {8, 31, 22}

# Diferencia de conjuntos
diferencia_conjuntos = mi_conjunto.difference(otro_conjunto)
print(diferencia_conjuntos)  # {17, 28, 41, 46}

# Suma de los valores de un conjunto (solo si son numéricos)
print(sum(mi_conjunto))  # Suma de los elementos numéricos del conjunto

# Longitud de conjunto
print(len(mi_conjunto))  # Número de elementos en el conjunto


#----------------------------------------------------------------------------

if os.path.isfile('./datos.csv'):
    with open('./datos.csv', encoding='utf8', mode='a+') as f:
        escritor = csv.writer(f)
        escritor.writerow( ['nombre','v1','v2','v3','v4'] ) #encabezado
        escritor.writerow( ['María',5,10,3,537] )
        escritor.writerow( ['Malenic',6,80,13,2] )


if os.path.isfile('./datos.csv'):
    with open('./datos.csv', encoding='utf8', mode='r' )as f:
        lector = csv.DictReader(f)

        for dato in lector:
            print(dato)        

