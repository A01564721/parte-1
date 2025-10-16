while True:
    palabra = input("Ingrese palabra clave: ")
    with open("documento.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if palabra in linea:
                print("Línea encontrada:", linea.strip())
                continuar = input("¿Desea continuar buscando? (s/n): ").lower()
                if continuar == "n" or continuar == "no":
                    print("Búsqueda terminada por el usuario.")
                    exit()
    print("Búsqueda completada.")
    break
