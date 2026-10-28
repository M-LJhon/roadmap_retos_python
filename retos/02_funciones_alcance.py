# Funciones con parámetros:

# Funcion para sumar dos numeros (dos parametros).
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado  # Con retorno.

resultado_suma = sumar(5, 64)
print(resultado_suma)

# Funcion anidada:
def externa(nombre):
    def interna():
        print(f"Hola, {nombre}")
    interna()

externa("Jhonsin")

# Scope.
var_global = 55
def numeros():
    var_local = 30
    print(var_local)

numeros()
print(var_global)
# print(var_local) -> NameError: name 'var_local' is not defined. Did you mean: 'var_global'?

# Funciones propias de Python:
lista_numeros = [1, 3, 6]
print(sum(lista_numeros))

# Recursividad:
def contador (cont):
    if cont == 0:
        print(cont)
        return
    print(cont)
    contador(cont - 1)

contador(10)


# Dificultad extra.
"""
DIFICULTAD EXTRA (opcional):
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def imp_numeros(pal_1, pal_2):
    for i in range(1, 101):
        if i%3 == 0 and i%5 == 0:
            print(pal_1, " ", pal_2)
        elif i%3 == 0:
            print(pal_1)
        elif i%5 == 0:
            print(pal_2)
        else:
            print(i)

imp_numeros("fizz", "buzz")