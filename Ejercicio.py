import math
lista_coordenadas=[(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]
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

cercanos(lista_coordenadas,(2,3))
