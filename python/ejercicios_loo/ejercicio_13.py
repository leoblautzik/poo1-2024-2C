"""
Se ingresa un valor numérico por consola, determinar e informar 
si se trata de un número primo o no.
"""
n = int(input("Ingrese un numero natural (mayor que 0)"))

i = 2
while (n > i and i < n and n % i != 0):
    i += 1
es_primo = n == i

# if a <= 1:
#     es_primo = False
# else:
# for i in range(2, a, 1):  # for(int i=2; i<a; i++)
#     if a % i == 0:
#         print(i)
#         es_primo = False
#         break

if es_primo:
    print("es primo")
else:
    print("no es primo")
