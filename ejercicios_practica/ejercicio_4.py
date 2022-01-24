# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.
    print("Ejercicio nro 1")
    list_numeros_str = ['5', '2', '3', '', '7', 'NaN']

    lista_numerica = [int(x) if(x.isdigit()) == True else 0 for x in list_numeros_str]
    
    print("Se muestran los numeros: ",lista_numerica) 
                     



    # str1 = '342'
    # print(str1.isdigit())

    # str2 = 'python'
    # print(str2.isdigit())

    # ¿Ya terminaron el ejercicio? ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?
    # ¿Qué sucede con isdigit? Sorprendente no?

    print("Ejercicio nro 2")

    lista_numerica_negativa = [int(x)*-1 if(x.isdigit()) == True else 0 for x in list_numeros_str]
    print("Se muestran los numeros NEGATIVOS: ",lista_numerica_negativa) 
    
    print("terminamos")