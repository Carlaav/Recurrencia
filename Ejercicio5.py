lista= [1,3,8,14,32,56,71]
limite_derecho= len(lista)-1
limite_izquierdo= 0
numero=8

def busqueda(lista,limite_derecho, limite_izquierdo, numero):  
    index= (limite_derecho+limite_izquierdo)//2
    if lista[index]== numero:
        print("encontrado en:",index)
    elif lista[index]>numero:
        limite_derecho= index
        busqueda(lista,limite_derecho,limite_izquierdo,numero)
    else:
        limite_izquierdo= index
        busqueda(lista,limite_derecho,limite_izquierdo,numero)
        
        
        
busqueda(lista,limite_derecho,limite_izquierdo,numero)