import json
import os
from PaisesAPI import PaisesAPI
class Archivo:
    def __init__(self,tupla):
        print(tupla)
        data = {}
        data['nombre'] = tupla[1]
        data['capital'] = tupla[2]
        data['poblacion'] = tupla[3]
        data['bandera'] = tupla[4]
        dir = 'C:/Users/Vivian/Documents/Punto Singular'  # También es válido 'C:\\Pruebas' o r'C:\Pruebas'
        print(data['nombre'])
        file_name = data['nombre']+".json"
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(data, file)
if __name__=="__main__":
    a=Archivo("mexico")
