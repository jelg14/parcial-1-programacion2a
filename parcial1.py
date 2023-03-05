#quinela mundial qatar 2022
import sys
from collections import *
v = deque()

class Libro():
    def __init__(self,apostador:str,edad,pais:str,telefono:str,cantidad) :
        self.apostador = apostador
        self.edad = edad
        self.pais = pais
        self.telefono = telefono
        self.cantidad = cantidad

class Telefono():
    def set_telefono(self,ext:str, numero:str):
        telefono = {"extension":ext," telefono":numero}
        return telefono

class Sexo():
    def genero(self,g:str):
        if g.lower() == "m": return "masculino"
        else: return "femenino"

class RangoEdad():
    def redad(self,edad:int):
        if(edad > 18 and edad <= 59):
            return "joven o adulto"
        elif( edad > 60 ):
            return "tercera edad"
        else: return "persona demasiado joven para participar en las apuestas"

class ReinoUnido():
    def validacion(self,pais:str):
        if "reino unido" in pais.lower():
            return True

class Pais():
    def datosP(self, nombre:str,continente:str):
        return {"continente":continente,"Pais":nombre}

class Persona(Telefono,Sexo,ReinoUnido,Pais):
    def __init__(self,nombre:str,apellido:str,telefono:str,codigo:str,rangoEdad,sexo:str,pais:str):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = self.set_telefono(telefono,codigo)
        self.rangoEdad = rangoEdad
        self.sexo = self.genero(sexo)
        if self.validacion(pais)==True: self.pais == "Reino unido"
        #else: self.pais == self.datosP(pais,"America")
        
class Imprimir():
    def imprimiendoTxt(self,nombre:str,rangoEdad,telefono:str,apuesta):
        for l in apuesta:
            if l["nombre del apostador"] == nombre:
                return "apostador: "+nombre+" telefono: "+telefono+"Rango edad:"+rangoEdad+" apuesta: {Cantidad= "+l["cantidad de apuestas"]+"/ monto total de la apuesta: "+l["montoTotal"]+"}"

class Texto(Imprimir):
    def datosAimprimir(self,a,e,t,c):
        return self.imprimiendoTxt(a,e,t,c)

class Registro(Sexo,RangoEdad): #principal
    def __init__(self, nombre,apellido,telefono,codigo,rango,sexo,pais,apuesta):
        self.nombre = nombre
        self.apellido =apellido
        self.telefono = telefono
        self.codigo = codigo
        self.rango = self.redad(rango)
        self.sexo = self.genero(sexo)
        self.pais = pais
        self.apuesta = apuesta

class Apuesta():
    def realizarApuesta(self,nombre:str,noApuestas:int,monto:float):
        listadoApuestas = []
        apuesta={"nombre del apostador":nombre,"cantidad de apuestas":noApuestas,"montoTotal":monto}
        listadoApuestas.append(apuesta)
        return listadoApuestas

class noParticipantes():
    def dineroRecaudado(dinero:bool):
        __recaudado+= dinero
    
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
            
class Premiacion(Premio,noParticipantes):
    def prem(self,aciertos:int):
        recaudado= self.dineroRecaudado(1)
        recaudado= recaudado-1
        return self.calcularPremio(aciertos,recaudado)

class Categoria(Texto):
    def simple(): return "simple"
    def multiple(): return "multiple"
    

print("""
***************************************************
            ___  ___ _____  _   _  _   _
            |  \/  ||  ___|| \ | || | | |
            | .  . || |__  |  \| || | | |
            | |\/| ||  __| | . ` || | | |
            | |  | || |___ | |\  || |_| |
            \_|  |_/\____/ \_| \_/ \___/
***************************************************
""")

while(True):
    print("""
**************SELECCIONE TIPO DE IMPRESION:********
***************************************************
**Agregar apuesta...........(1)
**imprimir libro............(2)
**Salir de la aplicacion....(3)
***************************************************""")
    opcion = int(input())
    c=Imprimir()

    match opcion:
        case 1:
            registroDatos = ["encabezado"]
            nombre=input("ingrese nombre del apostador: ")
            apellido = input("ingrese apellido del apostador: ")
            codigo = input("ingrese codigo telefonico de su pais: ")
            telefono = input("agregue no. de telefono: ")
            edad = int(input("ingrese su edad: "))
            genero = input("ingrese genero: m=masculino, f=femenino")
            pais = input("ingrese pais de residencia: ")
            apuestac= input("ingrese cantidad de apuestas")
            monto= input("ingrese monto total de las apuestas")
            datoApuesta =  Apuesta()
            a = datoApuesta.realizarApuesta(nombre,apuestac,monto)
            registro = Registro(nombre,apellido,telefono,codigo,edad,genero,pais,a)
            v.append(registro)
        case 2:
            for i in v:
                print (c.imprimiendoTxt(i.nombre,i.rango,i.telefono,i.apuesta))
        case 3:
            print("...Adios")
            break
        case _:
            print("ERROR: opcion no disponible") 
