# Listas.
"""
Son mutables, ordenadas y permiten duplicados.
Se usan corchetes para declarar una lista. []
** Se pueden crear listas con items de distintos
tipos de datos, pero es recomendable manejar listas
que contengan items del mismo tipo de dato.
"""
numeros = [10, 20, 30, 40]
print(f"Lista de numeros: {numeros}")
# [10, 20, 30, 40]

# Acceder a un dato por su indice:
print(f"Indice 0: {numeros[0]}")
# 10

# Mutabilidad.
# Agregando otro item a la lista:
numeros.append(50)
print(f"Se agrega el 50 al final de la lista: {numeros}")
# [10, 20, 30, 40, 50]
# Cambiamos un item usando su indice:
numeros[0] = 100
print(f"Cambiamos el 10 por el 100 usando el indice: {numeros}")
# [100, 20, 30, 40, 50]

# Datos duplicados:
numeros.append(50)
print(f"Agregando otro item 50: {numeros}")
# [100, 20, 30, 40, 50, 50]


# Tuplas.
"""
Son ordenadas, no mutables y permiten duplicados.
Se usan parentesis para declara una tupla. ()
"""
coordenadas = (3.75, -75.01, 3.75)
# Permite duplicados.
print(f"Tupla de coordenadas: {coordenadas}")
# (3.75, -75.01)
# Accedemos a un item por su indice:
print(f"Indice 0: {coordenadas[0]}")
# 3.75

# No son mutables.
# coordenadas.append(55.43)
# AttributeError: 'tuple' object has no attribute 'append'
# coordenadas[0] = 33.45
# TypeError: 'tuple' object does not support item assignment


# Diccionarios:
"""
Maneja orden de inserción, mutable y no permite claves repetidas.
Usa estilo clave valor: {"nombre": "Jhon"}
"""
usuario = {
    "nombre": "Jhon",
    "edad": 20,
    "ciudad": "Cali"
}
print(usuario)
# {'nombre': 'Jhon', 'edad': 20, 'ciudad': 'Cali'}
# Accedemos por clave:
print(usuario["nombre"])
# Jhon

# Agregamos una nueva clave valor:
usuario["carrera"] = "ING de sistemas"
print(f"Agregamos la clave carrera: {usuario}")
# {'nombre': 'Jhon', 'edad': 20, 'ciudad': 'Cali', 'carrera': 'ING de sistemas'}
# Modificamos el valor de una clave:
usuario["nombre"] = "Luis"
print(f"Cambiamos Jhon por Luis en nombre: {usuario["nombre"]}")
# Luis
# Eliminamos un item:
del usuario["carrera"]
print(f"Eliminamos la clave carrera: {usuario}")
# {'nombre': 'Luis', 'edad': 20, 'ciudad': 'Cali'}

# Sets.
set_numeros = {1, 2, 3, 4}
# No permite duplicados:
numeros_2 = {1, 1, 2, 2, 3, 3}  # Elimina los duplicados.
# {1, 2, 3}
print(numeros_2)
# Se puede usar para eliminar duplicados:
usuarios = [
    "Ana",
    "Carlos",
    "Ana",
    "Pedro",
    "Carlos"
]
usuarios_unicos = set(usuarios)
print(usuarios_unicos)

# Operaciones matematicas de conjuntos:
a = {1, 2, 3}
b = {3, 4, 5}
# Union:
print(a | b)
# Interseccion:
print(a & b)
# Diferencia:
print(a - b)

# Set inmutable:
numeros_2 = frozenset({1, 2, 3})

# Anidando estructuras de datos:
# Lista de diccionarios:
lst_usuarios = [
    {
        "nombre": "Ana",
        "edad": 25
    },
    {
        "nombre": "Carlos",
        "edad": 30
    },
    {
        "nombre": "Pedro",
        "edad": 22
    }
]

# Dificultad extra:
"""
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

# lista_prueba =[]
# nombre_prueba= "Jhon"
# telefono_prueba = 3333333333

# def prueba_append(contacto, lista):
#     lista.append(contacto)

# prueba_append({"Nombre": nombre_prueba, "Telefono": telefono_prueba}, lista_prueba)

# print(lista_prueba)

