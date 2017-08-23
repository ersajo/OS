from time import time
with open('cadena.txt', 'r') as in_file:
    cadena = in_file.read()
cadena = list(cadena)
i = -1
j = 0
t_inicio = time()
while True:
    if j == len(cadena)/2:
        break
    inicio = cadena[j]
    final = cadena[i]
    cadena[j] = final
    cadena[i] = inicio
    i -= 1
    j += 1
t_final = time()
t_ejec = t_final - t_inicio
print ''.join(cadena)
print 'El tiempo de ejecucion fue:' + str(t_ejec*1000 ) + ' milisegundos'
