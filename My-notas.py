# Programa para escribir y leer un archivo de texto

print("Elige una opción:")
print("1. Usar notas por defecto")
print("2. Escribir mis propias notas")
opcion = input("Ingresa 1 o 2: ")

# Si elige la opción 1, se escriben notas por defecto
if opcion == "1":
    archivo = open("my_notes.txt", "w")  # abre el archivo para escribir
    archivo.write("Hoy practiqué cómo escribir archivos en Python.\n")
    archivo.write("Aprendí a usar write() y readline().\n")
    archivo.write("También aprendí a cerrar el archivo con close().\n")
    archivo.close()  # cierra el archivo

# Si elige la opción 2, el usuario escribe sus propias notas
elif opcion == "2":
    archivo = open("my_notes.txt", "w")  # abre el archivo para escribir
    print("Escribe tus notas. Escribe 'fin' para terminar.")
    while True:
        nota = input("Nota: ")
        if nota.lower() == "fin":
            break  # termina si el usuario escribe 'fin'
        archivo.write(nota + "\n")  # escribe la nota en el archivo
    archivo.close()  # cierra el archivo

else:
    print("Opción no válida.")
    exit()  # sale del programa si la opción no es 1 ni 2

# Ahora leemos el archivo
archivo = open("my_notes.txt", "r")  # abre el archivo para leer

print("\nLeyendo tus notas:")
linea = archivo.readline()  # lee una línea
while linea != "":  # mientras la línea no esté vacía
    print(linea.strip())  # muestra la línea sin el salto de línea
    linea = archivo.readline()  # lee la siguiente línea

archivo.close()  # cierra el archivo
