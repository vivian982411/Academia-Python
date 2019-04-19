from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import json
from urllib.parse import urlparse,parse_qs
from PaisesAPI import PaisesAPI
from Conexion import Conexion
from archivo import Archivo
class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        name=parse_qs(urlparse(self.path).query).get('country',None)
        obj=Conexion()
        result=obj.mysqlConnect('root','2411','Paises')
        if result:
            try:
                query=("select * from pais where nombre_pai='%s'"%(name[0]))
                result=obj.prepare(query)
                if result:
                    data = {}
                    data['nombre'] = result[0][1]
                    data['capital'] = result[0][2]
                    data['poblacion'] = result[0][3]
                    data['bandera'] = result[0][4]
                    file=json.dumps(data)
                    self.send_response(200)
                    self.send_header('Content-type',data)
                    self.end_headers()
                    self.wfile.write(bytes(file,'utf-8'))
                else:
                    try:
                            print("No encontrado, buscando en API")
                            p=PaisesAPI(name[0])
                            data = {}
                            data['nombre'] = p.get_nombre()
                            data['capital'] = p.get_capital()
                            data['poblacion'] = p.get_poblacion()
                            data['bandera'] = p.get_bandera()
                            file=json.dumps(data)
                            self.send_response(200)
                            self.send_header('Content-type',data)
                            self.end_headers()
                            self.wfile.write(bytes(file,'utf-8'))
                    except:
                            print("ERROR")
                            file="File not found"
                            self.send_response(404)
            except:
                print("Hecho")
        else:
            print("Base de datos no conectada")
        obj.mysqlClose()

if __name__=="__main__":
        
        httpd=HTTPServer(('localhost',8080),Servidor)
        httpd.serve_forever()

