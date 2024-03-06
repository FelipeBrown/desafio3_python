import sys

ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

umbral = int(sys.argv[1])

meses_mayor_umbral = {mes: ventas[mes] for mes in ventas if ventas[mes] > umbral}

print(f"los meses con mayor umbral son: {meses_mayor_umbral}")

