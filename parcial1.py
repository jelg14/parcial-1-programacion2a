#quinela mundial qatar 2022
class Libro():
class Telefono():
    def set_telefono(ext:str, numero:str):
        telefono = "extension: +"+ext+" telefono: "+numero

class Persona(Telefono,Sexo):
    def __init__(self,nombre:str,apellido:str,telefono:str,codigo:str):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = self.set_telefono(telefono,codigo)
        
        
    
class Sexo():
    def masculino(self):
        return "masculino"
    def femenino(self):
        return "femenino"
    
class RangoEdad():
    def esJoven(edad:int):
        if(edad > 18 or edad < 25):
            return True
    def esTerceraEdad(edad:int):
        if(edad > 60 ):
            return True
    
class ReinoUnido():
    def validacion(pais:str):
        if "reino unido" in pais.lower():
            return True
class Pais():
    def __init__(self, nombre:str,continente:str):
        self.nombre = nombre
        self.continente = continente
        pass
class Texto():
class Imprimir():
class Registro(): #principal
class Apuesta():
class Premiacion(Premio,noParticipantes):
    def prem(self,aciertos:int):
        recaudado= self.dineroRecaudado(1)
        recaudado= recaudado-1
        return self.calcularPremio(aciertos,recaudado)
    
class Premio():
    def calcularPremio(resultados:int, premio:bool):
        match resultados:
            case 15:
                return premio*0.25
            case 14:
                return premio*0.15
            case 13:
                return premio*0.10
            case 12:
                return premio*0.085
            case 11:
                return premio*0.07
            case 10:
                return premio*0.06
class Categoria():
    def simple(): return "simple"
    def multiple(): return "multiple"
    
class noParticipantes():
    def contador():
        i+=1
        return i
    def dineroRecaudado(dinero:bool):
        recaudado+= dinero
        return recaudado