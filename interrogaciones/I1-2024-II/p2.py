# Escribe tu código aquí

cont = 0
num_prev = 0
num_prev_prev = 0
cont_rachas = 0

i = 0
while True:
    num = int(input())
    if num == -1:
        break
    if i == 0:
        num_prev_prev = num
        num_prev = num
    if i == 1:
        num_prev_prev = num_prev
        num_prev = num

    if i >= 2:
        if (num_prev_prev < num_prev < num):
            cont_rachas += 1
        num_prev_prev = num_prev
        num_prev = num
        # cont+=1
        # i+=1

    i += 1
    cont += 1

print(cont_rachas)