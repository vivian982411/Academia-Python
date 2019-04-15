from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import json
from urllib.parse import urlparse,parse_qs
from PaisesAPI import PaisesAPI
from Conexion import Conexion
from archivo import Archivo
class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        dire=parse_qs(urlparse(self.path).query).get('country',None)
        archivo=dire[0]+".json"
        print(dire)
        try:
            file=open(archivo).read()
            self.send_response(200)
        except FileNotFoundError:
            try:
                print("No encontrado, buscando en API")
                p=PaisesAPI(dire[0])
                data = {}
                data['nombre'] = p.get_nombre()
                data['capital'] = p.get_capital()
                data['poblacion'] = p.get_poblacion()
                data['bandera'] = p.get_bandera()
                file=json.dumps(data)
                self.send_response(200)
                self.send_header('Content-type',data)
            except:
                print("ERROR")
                file="File not found"
                self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file,'utf-8'))

if __name__=="__main__":
        obj=Conexion()
        result=obj.mysqlConnect('root','2411','Paises')
        if result:
            result=obj.prepare("select * from pais")
            if result:
                for r in result:
                    a=Archivo(r)                  
        else:
            print("Base no conectada")
        obj.mysqlClose()
        httpd=HTTPServer(('localhost',8080),Servidor)
        httpd.serve_forever()
