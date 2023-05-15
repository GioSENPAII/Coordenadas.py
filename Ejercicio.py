#Sin usuario (el usuario no pone la coordenada a buscar)
import math
import random
import time
inicio=time.time()
lista_coordenadas= coordenadas = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(40)]
almacen=[]
temporal=[]
resultados=[]
resultados_finales=[]
def cercanos(lista,coordenada):
    
    if coordenada not in lista:
        return 0
    
    temporal.append(coordenada)
    lista.remove(coordenada)
    for punto in lista:
        almacen.append(math.dist(coordenada,punto))
    combinacion=list(zip(lista,almacen))
    print(combinacion)
    for i in range(2):
        resultados.append(min(almacen))
        almacen.remove(min(almacen))
    for i in range(2):
        for elemento in combinacion:
            if resultados[i] in elemento:
                resultados_finales.append(elemento[0])
    print("Las coordenadas más crecanas a la coordenada {} son: {}".format(coordenada,resultados_finales))
    almacen.clear()
    resultados.clear()
    resultados_finales.clear()
    lista.append(temporal[0])
    temporal.clear()
print(lista_coordenadas)
usuario_coordenada=lista_coordenadas[random.randint(0,20)]

cercanos(lista_coordenadas,usuario_coordenada)
final=time.time()
print((final-inicio)*1000)
