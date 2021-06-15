from pila import Pila
from cola import Cola
from lista import Lista

def barrido_cola (cola):
    """Muestra los contenidos de la cola con ayuda de una cola auxiliar para no perder informacion."""
    cola_aux = Cola()
    while not cola.cola_vacia():
        x = cola.atencion()
        cola_aux.arribo(x)
        print (x)
    while not cola_aux.cola_vacia():
        cola.arribo(cola_aux.atencion())

def barrido_pila (pila):
    """Muestra los contenidos de la pila con ayuda de una pila auxiliar para no perder informacion."""
    pila_aux = Pila()
    while not pila.pila_vacia():
        x = pila.desapilar()
        pila_aux.apilar(x)
        print (x)
    while not pila_aux.pila_vacia():
        pila.apilar(pila_aux.desapilar())

#!-----------------------//PUNTO 1//----------------------------!#
# Dado un vector con personaje de las películas de la saga de Star Wars resolver las
# siguientes actividades:
# a. Realizar un barrido recursivo del vector. 
# b. Realizar una función recursiva que permita determinar si ‘Yoda’ está en el vector y en que posición

personajes = ['Leia Organa', 'Han Solo', 'Luke Skywalker', 'Chewbacca', 'Yoda', 'Kylo Ren']

def barrido_recursivo (vector, i):
    """Realiza un barrido recursivo del vector."""
    if i == len(vector)-1:
        print (vector[i])
    else:
        print (vector[i]) 
        barrido_recursivo(vector, i+1)

barrido_recursivo(personajes, 0)
print()

def existe_personaje (vector, personaje, i):
    """Devuelve la posicion de 'personaje' si esta en el vector, y si no devuelve -1."""
    if i<len(personajes):
        if (personajes[i]) == 'Yoda':
            return i
        else:
            return existe_personaje(vector, personaje, i+1)
    else:
        return -1

pos = existe_personaje(personajes, 'Yoda', 0)
if (pos != -1):
    print('Yoda se encuentra en el vector en la posicion', pos)
else:
    print('Yoda no se encuentra en el vector.')

#!-----------------------//PUNTO 2//----------------------------!#
# Dada una cola con las notificaciones de las aplicaciones de red social de un Smartphone, de las cual se cuenta con la hora 
# de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:
# c. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# d. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra 
# ‘Python’, si perder datos en la cola;
# e. utilizar una pila para almacenar temporalmente las notificaciones de Instagram y mostrar el contenido de dicha pila

class Notificacion (object):

    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

    def __str__(self):
        return str(self.hora)[:2] + ':' + str(self.hora)[2:]+ ' - ' + self.aplicacion + ' - ' + self.mensaje

datos = [(1142,'Facebook','notificacion'),(1235,'Twitter','notificacion Python'),(1255,'Instagram','notificacion'),
         (1355,'Twitter','notificacion'), (1412,'Instagram','notificacion'), (1515,'Facebook','notificacion'),
         (1557,'Twitter','Python notificacion'), (1725,'Facebook','notificacion'), (1822,'Instagram','notificacion')]

cola_notificaciones = Cola()
cola_aux = Cola()
pila_instagram = Pila()


for (hora, aplicacion, mensaje) in datos:
    notificacion = Notificacion(hora, aplicacion, mensaje)
    cola_notificaciones.arribo(notificacion)

print()
print('Lista de notificaciones:')
barrido_cola(cola_notificaciones)
print()

def eliminar_notificacion (cola, aplicacion):
    """Elimina todas las notificaciones de la aplicacion dada de la cola."""
    cola_aux = Cola()
    while not cola.cola_vacia():
        x = cola.atencion()
        if x.aplicacion != aplicacion:
            cola_aux.arribo(x)
    while not cola_aux.cola_vacia():
        cola.arribo(cola_aux.atencion())

def mostrar_notificacion (cola, aplicacion, palabra):
    """Muestra las notificaciones de la aplicacion dada que contengan 'palabra' en el mensaje."""
    cola_aux = Cola()
    while not cola.cola_vacia():
        x = cola.atencion()
        cola_aux.arribo(x)
        if (x.aplicacion == aplicacion and palabra in x.mensaje):
            print(x)
    while not cola_aux.cola_vacia():
        cola.arribo(cola_aux.atencion())

# punto c.
eliminar_notificacion(cola_notificaciones, 'Facebook')
print('Lista de notificaciones luego de eliminar las de Facebook:')
barrido_cola(cola_notificaciones)
print()

# punto d. 
print ("Notificaciones de Twitter que contienen la palabra 'Python'")
mostrar_notificacion(cola_notificaciones, 'Twitter', 'Python')
print()

# punto e.
while not cola_notificaciones.cola_vacia():
    x = cola_notificaciones.atencion()
    cola_aux.arribo(x)
    if (x.aplicacion == 'Instagram'):
        pila_instagram.apilar(x)

while not cola_aux.cola_vacia():
    cola_notificaciones.arribo(cola_aux.atencion())

print('Notificaciones de Instagram:')
barrido_pila(pila_instagram)
print()


#!-----------------------//PUNTO 3//----------------------------!#
# Dada una lista con nombres de personajes de la saga de Avengers, resolver las siguientes tareas:
# a. Determinar si ‘Thor’ está en la lista, de ser así indicar en qué posición de la misma;
# b. Modificar el nombre de ‘Scalet Witch’ a ‘Scarlet Witch’;
# c. Dada una lista auxiliar con los siguientes personajes (‘Black Widow’, ‘Hulk’, ‘Rocket Raccoon’, ‘Loki’), 
# agregarlos a la lista principal en el caso de no estar cargados. 
# d. Realizar un barrido ascendente y descendente de la lista. 
# e. Mostrar la información del personaje en la posición 7. 
# f. Mostrar todos los personajes que comienzan con C o S. 
# g. Ahora los datos cambiaron y debe incluir (año de aparición y un campo booleano que indica si es héroe True villano False), 
# luego realizar un barrido ordenado por nombre y otro por año de aparición. Deberá cargar toda la información de nuevo.

datos1 = [
    {'nombre':'Dr. Strange','año_aparicion': 2016, 'heroe' : True},
    {'nombre':'Capitana Marvel','año_aparicion': 2019, 'heroe' : True},
    {'nombre':'Star-Lord','año_aparicion': 2014, 'heroe' : True},
    {'nombre':'Thor','año_aparicion': 2011, 'heroe' : True},
    {'nombre':'Thanos','año_aparicion': 2012, 'heroe' : False},
    {'nombre':'Scalet Witch','año_aparicion': 2014, 'heroe' : True}
]

datos2 = [
    {'nombre':'Black Widow','año_aparicion': 2010, 'heroe' : True},
    {'nombre':'Hulk','año_aparicion': 2008, 'heroe' : True},
    {'nombre':'Rocket Raccoon','año_aparicion': 2014, 'heroe' : True},
    {'nombre':'Loki','año_aparicion': 2011, 'heroe' : False}

]

def mostrar_datos (lista, pos):
    print ('Nombre:', lista.obtener_elemento(pos)['nombre'], '| Año de aparición:', lista.obtener_elemento(pos)['año_aparicion'])
    if lista.obtener_elemento(pos)['heroe']:
        print ('Estado: Heroe')
    else:
        print ('Estado: Villano')

lista_personajes = Lista()
lista_auxiliar = Lista()

for personaje in datos1:
    lista_personajes.insertar(personaje, 'nombre')

for personaje in datos2:
    lista_auxiliar.insertar(personaje, 'nombre')

# punto a.
pos = lista_personajes.busqueda('Thor', 'nombre')
if (pos != -1):
    print('Thor se encuentra en la lista en la posicion', pos)
else:
    print('Thor no se encuentra en la lista.')

print()

# punto b.
pos = lista_personajes.busqueda('Scalet Witch', 'nombre')
if (pos != -1):
    lista_personajes.obtener_elemento(pos)['nombre'] = 'Scarlet Witch'

# punto c.
for i in range (lista_auxiliar.tamanio()):
    pos = lista_personajes.busqueda(lista_auxiliar.obtener_elemento(i)['nombre'], 'nombre')
    if pos == -1:
        lista_personajes.insertar(lista_auxiliar.obtener_elemento(i), 'nombre')

# d. Realizar un barrido ascendente y descendente de la lista.
print('Barrido ascendente:')
for i in range (lista_personajes.tamanio()):
    mostrar_datos(lista_personajes, i)

print()

print('Barrido descendente:')
for i in range (lista_personajes.tamanio()-1,-1,-1):
    mostrar_datos(lista_personajes, i)

print() 

# punto e.
print('Informacion del personaje en la posicion 7:') 
mostrar_datos(lista_personajes, 7)
print()

# punto f.
print('Personajes que comienzan con C o S:')
for i in range(lista_personajes.tamanio()):
    personaje = lista_personajes.obtener_elemento(i)
    if (personaje['nombre'][0]=='C' or personaje['nombre'][0]=='S'):
        print(personaje['nombre'])

print()

# punto g. 

lista_aparicion = Lista()

for i in range(lista_personajes.tamanio()):
    lista_aparicion.insertar(lista_personajes.obtener_elemento(i), 'año_aparicion')

print('Barrido ordenado por nombre:')
lista_personajes.barrido()
print()
print('Barrido ordenado por año de aparicion:')
lista_aparicion.barrido()