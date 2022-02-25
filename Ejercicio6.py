comprobar= True
palabra = "oso!!"
izquierda= 0
derecha= len(palabra)-1

def palindromo(comprobar,palabra,izquierda,derecha): 
    if izquierda==derecha:
        return comprobar
    else:
        if palabra[izquierda]==palabra[derecha]:
            izquierda= izquierda+1
            derecha= derecha-1
            return palindromo(comprobar,palabra,izquierda,derecha)
        else:
            comprobar=False
            return comprobar   
palabra = palabra.lower()
print("es palindromo:", palindromo(comprobar,palabra,izquierda,derecha))          
#para quitar acentos o otros caracteres se usaria regex, no lo hemos visto (David me ha dicho eso)