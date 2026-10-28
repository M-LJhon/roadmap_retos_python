contactos = []


def registro(nombre, telefono):
    if len(str(telefono)) == 10:
        contactos.append({
            "nombre": nombre,
            "telefono": telefono
        })
        print(contactos)
    else:
         print("El numero de telefono debe de tener 10 caracteres.")



def buscar(nombre):
    for contacto in contactos:
            print("Buscando el contacto...")
            if nombre in contacto["nombre"]:
                nombre_contacto = contacto["nombre"]
                telefono_contacto = contacto["telefono"]
                print("Contacto encontrado.\n"
                    f"Nombre: {nombre_contacto}\n"
                    f"Telefono: {telefono_contacto}")
                break
            nuevo_registro = input("El contacto no existe, desea registrarlo? \n" \
            "(si)(no): ")
            if nuevo_registro.lower() == "si":
                telefono_usuario_nuevo = input("Ingresa el numero de telefono: ")
                if len(telefono_usuario_nuevo) == 10:
                    registro(nombre, telefono_usuario_nuevo)
                else:
                     print("Ingrese un numero valido. (10 digitos)...")
            else:
                 break


def eliminar(nombre):
     for contacto in contactos:
          if nombre in contacto["nombre"]:
               del contacto
               print("Contacto borrado.")
               break
          else:
               print("Contacto no encontrado")
               break


def actualizar_contacto(nombre_contacto):
     for contacto in contactos:
          if nombre_contacto in contacto["nombre"]:
                nuevo_nombre = input("Desea actualizar el nombre del contacto?\n"\
                                                        "(si)(no): ").lower()
                nuevo_numero = input("Desea actualizar el numero del contacto?\n"\
                                                        "(si)(no): ").lower()
                if nuevo_nombre and nuevo_numero == "si":
                    while True:
                        inp_nombre_actualizado = input("Ingrese el nombre nuevo: ")
                        if inp_nombre_actualizado != "":
                            contacto["nombre"] = inp_nombre_actualizado
                            break
                        else:
                            print("El nombre no puede estar vacio... Vuelva a intentarlo.")

                    while True:
                        try:
                            inp_numero_actualizado = int(input("Ingrese el numero nuevo (10 digitos): "))
                        except TypeError:
                            print("Solo puedes ingresar numeros en el telefono...Vuelve a intentar.")

                        if len(str(inp_numero_actualizado)) == 10:
                            contacto["telefono"] = inp_numero_actualizado
                            break
                        else:
                            print("El numero debe de tener 10 digitos...Vuelve a intentar.")
                        
                        

                
                