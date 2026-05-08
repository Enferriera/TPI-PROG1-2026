def validar_string(palabra):
    if palabra!=" ":
        return True
    return False


if __name__=="__main__":
    lista_pais=[]
    palabra=input("Ingrese un pais: ")
    
    if validar_string(palabra):
        lista_pais.append(palabra)
        print(lista_pais)
    else:
        print("El dato ingresado no es valido")
        
   
    
    