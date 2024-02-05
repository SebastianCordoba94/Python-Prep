import os


montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}
texto = "Nombre,Orden,Cordillera,Pais,Altura"

archivo = open("clase09_ej3.scv","a")
archivo.write(texto+"\n")
for i in range(len(montañas['nombre'])):
    texto=""
    for j, (key, value) in enumerate(montañas.items()):
        texto += str(value[i])+","
    archivo.write(texto[:-1])
    archivo.write("\n")
archivo.close()

# 4) Mostrar el tamaño en MB del archivo generado en el punto 3
print("El tamaño del archivo es de",os.path.getsize("clase09_ej3.scv"),"Bites =",os.path.getsize("clase09_ej3.scv")*0.000000125,"MB")

# 5) Crear una carpeta llamada clase09_montañas_altas

if os.path.exists("clase09_montañas_altas"):
    print("La carpeta ya existe")
else:
    os.makedirs("clase09_montañas_altas")
    print("Carpeta Creada")

# 6) Copiar el archivo clase09_ej3.scv en la carpeta clase09_montañas_altas usando la sentencia **os.system**

try:
    destino = "./clase09_montañas_altas/clase09_ej3.scv"
    os.rename("clase09_ej3.scv",destino)
    print("El archivo se ha movido con exito")
except:
    print("Error al mover el archivo")

#7) Listar el contenido de la carpeta clase09_montañas_altas

print("Lista de la carpeta creara:\n",os.listdir("./clase09_montañas_altas"))
