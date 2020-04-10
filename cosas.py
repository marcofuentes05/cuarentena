import numpy
import matplotlib.pyplot as plt

#x es el porcentaje del total de la poblacion
def caos_function(c,x):
    return c*x*(1-x)
num = 1000
numero = 5
listaEstable = []
jump = 0.0001
initValue = 0.4
for rate in numpy.arange (0,numero,jump):
    #Valor inicial de la poblacion, no tiene relevancia significativa
    lista = [initValue]
    #Buscar la poblacion estable
    for i in range(0,num):
        lista.append(caos_function(rate,lista[i-1]))
    listaEstable.append(lista[len(lista)-1])
lt = numpy.arange(0, numero, jump)
s = [0.2 for n in range(len(listaEstable))]
plt.scatter(lt,listaEstable,s=s)
plt.ylabel('Stable population')
plt.xlabel('Growth rate')
print(lt[len(lt) - 2])
print(listaEstable[len(listaEstable)-1])
plt.show()
