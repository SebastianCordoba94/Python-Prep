import sys

if len(sys.argv) == 4:
    print("El primer parámetro es:",sys.argv[1])
    print("El segundo parámetro es:",sys.argv[2])
    print("El tercer parámetro es:",sys.argv[3])
else:
    print("ERROR: Se introdujo una cantidad de argumentos distinta de tres (3)")
    print("Ejemplo: clase09_ej1.py a b c")