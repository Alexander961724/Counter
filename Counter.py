def counter ():
    text = input("Please enter a text: ")
    cadena = text.split()
    result = len(cadena)
    print (f"Total of words are: {result}")
    diccionario = { }
    for palabra in cadena:
        if palabra in diccionario:
            diccionario[palabra] +=1
        else:
            diccionario[palabra] =1
    print (diccionario)


print("Help us to write something!")
counter()

    