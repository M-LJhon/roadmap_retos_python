# Opeadores.
# Aritméticos: +, -, *, /, //, %, **
print(2 + 3)  # Suma
print(5 - 2)  # Resta
print(4 * 3)  # Multiplicación
print(10 / 2)  # División
print(10 // 3)  # División entera
print(10 % 3)  # Módulo
print(2 ** 3)  # Potencia

# Comparación: ==, !=, >, <, >=, <=
print(5 == 5)  # Igualdad
print(5 != 3)  # Desigualdad
print(5 > 3)  # Mayor que
print(5 < 3)  # Menor que
print(5 >= 5)  # Mayor o igual que
print(5 <= 3)  # Menor o igual que

# Lógicos: and, or, not
print(True and False)  # AND
print(True or False)  # OR
print(not True)  # NOT

# Asignación: =, +=, -=, *=, /=, //=, %=, **=
x = 5
x += 2  # x = x + 2
print(x)  # 7
x -= 3  # x = x - 3
print(x)  # 4
x *= 2  # x = x * 2
print(x)  # 8
x /= 4  # x = x / 4
print(x)  # 2.0
x //= 2  # x = x // 2
print(x)  # 1.0
x %= 2  # x = x % 2
print(x)  # 1.0
x **= 3  # x = x ** 3
print(x)  # 1.0

# Identidad: is, is not
a = [1, 2, 3]
b = a
print(a is b)  # True, a y b son el mismo objeto
c = [1, 2, 3]
print(a is c)  # False, a y c son objetos diferentes

# Pertenencia: in, not in
print(3 in a)  # True, 3 está en la lista a
print(4 not in a)  # True, 4 no está en la lista a

# Bit a bit: &, |, ^, ~, <<, >>
x = 5  # 0101 en binario
y = 3  # 0011 en binario
print(x & y)  # AND bit a bit: 0101 & 0011 = 0001 (1)
print(x | y)  # OR bit a bit: 0101 | 0011 = 0111 (7)
print(x ^ y)  # XOR bit a bit: 0101 ^ 0011 = 0110 (6)
print(~x)  # NOT bit a bit: ~0101 = 1010 (-6)
print(x << 1)  # Desplazamiento a la izquierda: 0101 << 1 = 1010 (10)
print(x >> 1)  # Desplazamiento a la derecha: 0101 >> 1 = 0010 (2)

# Estructuras de control.
# Condicionales: if, elif, else
# If-elif-else.
edad = 14
if edad >= 18:
    print("Puedes ingresar, eres mayor de edad.")
elif edad >= 15 and edad <=17:
    print("Ya casi, pero aun no puedes ingresar." \
    "Debes ser mayor de edad.")
else:
    print("Solo pueden ingresa mayores de edad.")

# Bucles.
# For -> Imprimir numeros del 0 al 9 ignorando el 8.
for i in range(10):
    if i == 8:
        continue
    else:
        print(i)

# While -> Pide al usuario digitar el numero 5 hasta
# que lo haga correctamente.
cantidad = 0
while cantidad != 5:
    cantidad = int(input("Ingresa el numero 5: "))

# Control de errores: try / except.
numerador = 1
denominador = 1

numerador = int(input("Ingresa el numerador: "))
denominador = int(input("Ingresa el denominador: "))

try:
    operacion = numerador / denominador
    print(f"Resultado: {operacion}")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")


# Dificultad extra:
"""
Crea un programa que imprima por consola todos los
números comprendidos entre 10 y 55 (incluidos), 
pares, y que no son ni el 16 ni múltiplos de 3.
"""

for i in range(10, 56):
    if i == 10 or i == 55:
        print(i)
    elif i == 16:
        continue
    elif i%3 == 0:
        continue
    elif i%2 == 0:
        print(i)
