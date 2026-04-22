def contar_digitos(num):
    num = str(num)
    contador = 0
    for caractere in num:
        contador += 1
    return contador
n1 = input("digite um numero grande ou palavra grande: ")
print(contar_digitos(n1))