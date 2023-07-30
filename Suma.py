# Ejercicio de suma de los primeros numeros n pares

#Primer intento
primer_numero = 2
segundo_numero = 4
tercer_numero = 6
cuarto_numero = 8

sum = primer_numero + segundo_numero + tercer_numero + cuarto_numero
print(f"La suma de los primeros n numeros pares es: {sum}")


#Segundo intento
def suma_primeros_n_pares(n):
    suma = n* (n+1)
    return suma

n = int(input('Ingrese el valor de n (numero entero): '))
resultado = suma_primeros_n_pares(n)
print(f'La suma de los primeros {n} numeros pares es: {resultado}')