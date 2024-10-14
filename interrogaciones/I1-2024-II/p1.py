# Escribe tu código aquí

lim_inf = float(input())
lim_sup = float(input())
cont = 0
while True:
    num = float(input())
    if num == -1:
        break
    if num >= lim_inf and num <= lim_sup:
        cont += 1

print(cont)
