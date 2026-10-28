from funciones import *

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
print(contactos)



while True:
    print("*** Agenda de contactos ***")
    print("¿Que deseas hacer? \n" \
    "- Buscar un contacto (0)\n" \
    "- Insertar un contacto (1)\n" \
    "- Eliminar un contacto (2)\n" \
    "- Actualizar un contacto (3)\n" \
    "- Salir (4) \n")

    seleccion = int(input("Escribe la opcion que desees: "))

    if seleccion == 0:
        nombre_contacto = input("Escribe el nombre del contacto a buscar: ")
        buscar(nombre_contacto)
    elif seleccion == 1:
        nombre_contacto = input("Escribe el nombre del contacto a insertar: ")
        telefono_nuevo = int(input("Ingrese el telefono: "))
        registro(nombre_contacto, telefono_nuevo)
    elif seleccion == 2:
        nombre_contacto = input("Escribe el nombre del contacto a borrar: ")
        eliminar(nombre_contacto)
    elif seleccion == 3:
        nombre_contacto = input("Escribe el nombre del contacto a editar: ")
        actualizar_contacto(nombre_contacto)
    elif seleccion == 4:
        print("Cerrando el programa.")
        break
