"""Se ingresa un valor numérico de 8 dígitos 
que representa una fecha con el siguiente formato aaaammdd. 
Se pide informar por separado el día, 
el mes y el año de la fecha ingresada.
"""

fecha = 20250101

anio = fecha // 10000
mes = fecha // 100 % 100
dia = fecha % 100

print(fecha)
print("Dia: ", dia)
print("Mes: ", mes)
print("Año: ", anio)
