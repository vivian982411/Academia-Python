import pymysql

class Conexion:
    def __init__(self):
        self.connected=0
        self.error=""

    def mysqlConnect(self,us,pw,database):
        """
        Realiza la conexion con la base de datos
        Tiene que recibir:
            - user
            - pw => password
            - database => database name
        Puede recibir:
            - port
        Devuelve True o False
        """
        try:
            self.db = con= pymysql.connect(host='localhost',port=3306,user=us,password=pw,db=database)
            self.cursor = self.db.cursor()
            self.connected=1
            return True
        except:
            self.error="Error desconocido"
        return False

    def prepare(self,query,params=None,execute=True):
        """
        Funcion que ejecuta una instruccion mysql
        Tiene que recibir:
            - query
        Puede recibir:
            - params => tupla con las variables
            - execute => devuelve los registros
        Devuelve False en caso de error
        """
        if self.connected:
            self.error=""
            try:
                self.cursor.execute(query)
                self.db.commit()
                if execute:
                    result = []
                    result=self.cursor.fetchall()
                    return result
                return True
            except Exception:
                self.error="Error:"
        return False

    def mysqlClose(self):
        """
        Funcion para cerrar la conexion con la base de datos
        """
        self.connected=0
        try:
            self.cursor.close()
        except:pass
        try:
            self.cnx.close()
        except:pass


if __name__=="__main__":
    obj=Conexion()
    result=obj.mysqlConnect('root','2411','Paises')
    if result:
        print("ok")
        result=obj.prepare("select * from pais")
        if result:
            print(result)
    else:
        print("Base no conectada")
    obj.mysqlClose()
