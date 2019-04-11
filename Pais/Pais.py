import Conexion
import PaisesAPI
class Pais:
    def __init__(self,pais):
        self.nombre=pais.get_nombre()
        self.capital=pais.get_capital()
        self.poblacion=pais.get_poblacion()
        self.bandera=pais.get_bandera()
        self.con=Conexion.Conexion()
        self.res=self.con.mysqlConnect('root','2411','Paises')

    def insertar(self):
        if self.res:
            sql= ('INSERT INTO PAIS VALUES(null,"%s","%s","%s","%s")'%(self.nombre,self.capital,self.poblacion,self.bandera))
            print(sql)
            try:
                res=self.con.prepare(sql)
                print("Dato almacenado en la base")
            except Exception as e:
                print('No se pudo insertar el dato')
        else:
            print("Base no conectada")

    def listar(self):
        if self.res:
            sql= ('SELECT * FROM PAIS')
            try:
                res=self.con.prepare(sql)
                print(res)
            except Exception as e:
                print("Valores inalcanzables")
            
        else:
            print("Base no conectada")
    def actualizar(self,ide,nombre,capital,poblacion,bandera):
        sql=('UPDATE PAIS SET nombre_pai="%s",capital_pai="%s",poblacion_pai=%s,bandera_pai="%s" WHERE id_pai=%s'%(nombre,capital,poblacion,bandera,ide))
        try:
            res=self.con.prepare(sql)
            print("Valores actualizados")
        except Exception as e:
            print("Valores inalcanzables")
            
            

if __name__=="__main__":
    p=PaisesAPI.Paises("colombia")
    pa=Pais(p)
    pa.insertar()
    pa.listar()
    pa.actualizar(1,"Japón","Tokio",1268000000,"https://es.wikipedia.org/wiki/Archivo:Flag_of_Japan.svg")
    pa.listar()
        
        
    
