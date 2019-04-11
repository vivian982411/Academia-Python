import requests
class Paises:
    
    def __init__(self,nombre):
        sitio="https://restcountries.eu/rest/v2/name/"+nombre
        self.response = requests.get(sitio)
        if self.response.status_code == 200:
            results = self.response.content
            r=self.response.json()
            for result in r:
                self.nom=(result["name"])
                self.cap=(result["capital"])
                self.pob=(result["population"])
                self.band=(result["flag"])
                    
        else:
            print ("Error code %s" % response.status_code)

    def get_nombre(self):
        return self.nom
    def get_capital(self):
        return self.cap
    def get_poblacion(self):
        return self.pob
    def get_bandera(self):
        return self.band
    
        
