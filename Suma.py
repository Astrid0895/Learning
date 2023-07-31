# Ejercicio de suma de los primeros numeros n pares

#Primer intento
primer_numero = 2
segundo_numero = 4
tercer_numero = 6
cuarto_numero = 8

sum = primer_numero + segundo_numero + tercer_numero + cuarto_numero
print(f"La suma de los primeros n numeros pares es: {sum}")


#Segundo intento, despues de entender la operacion

n = input()
n = int(n)
suma = (2*n*(n+1))//2
print(suma)