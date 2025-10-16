archivo = open("documento.txt", "r")

palabra = input("Ingrese palabra clave: ")

for linea in archivo:
    if palabra in linea:
        print("Línea encontrada:", linea.strip())
        continuar = input("¿Desea continuar buscando? (s/n): ")
        if continuar == "n":
            print("Búsqueda terminada por el usuario.")
            break

archivo.close()
