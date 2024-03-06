from string import ascii_lowercase
import getpass

dic = ascii_lowercase
password = getpass.getpass ("ingrese la clave: ")

cont = 0

for letra in password:
    for caracter in dic:
        cont += 1
        if letra == caracter:
            break
print(f"la pass se encontro en {cont} iteraciones")
