
from llavero import buscar_llave
import random

#Esta clase como tal es nuestra maquina compuesta de 8 rotores y recibe la llave de la usb
class Enigma:
    #esta funcion da el nacimiento de la maquina pues extrae la llave y alimenta las demas funciones con ella
    def __init__(self,llave_usb): #__init__ nuestro constructor y establecemos el estado inicial de la maquina desde aqui (se ejecuta solo)
        #Aqui se guarda la llave de la usb
          self.llave = llave_usb
          #aqui se crean nuestros rotores
          self.rotores = []
          #Posicion inicial de los rotres 0 los 8 de ellos
          self.posiciones = [0] * 8
          #creamos los rotores 
          self._crear_rotores()

    #Creamos los rotres con la llave de la usb
    def _crear_rotores(self):
        vllave= sum(self.llave)
        random.seed(vllave)

        for i  in range(8):
            rotor = list(range(256))
            random.shuffle(rotor)
            self.rotores.append(rotor)

    #Esta es la funcion que hara girar nuestros rotores 
    def rotacion(self):
        self.posiciones[0] +=1
        for i in range(7): #revisamos del rotor 0 al 6
            if self.posiciones[i] == 256: 
                self.posiciones[i] = 0
                self.posiciones[i+1] += 1 #nos movemos al siguiente rotor

    #Aqui cambiamos el valor de cada byte segun entra a la maquina aqui ciframos los archivos
    def trituradora(self,entrada):
        resultado = entrada #el byte entra a la maquina
        for i in range(8): #pasamos ese byte por cada uno de los 8 rotores 0,1,2,3,4,5,6,7
            posicion = (resultado + self.posiciones[i]) % 256 #aqui se esconde el byte con otro valor
            resultado = self.rotores[i][posicion]
            #despues de ser escondido con otro valor la maquina gira los rotores
        self.rotacion()
        return resultado
    
    #Esta funcion es la inversa de la trituradora pes para descifrar los archivos 
    def pegadora (self,entrada):
        resultado = entrada
        for i in reversed(range(8)): #reversed nos hara ir en reversa 7,6,5,4,3,2,1,0
            posicion = self.rotores[i].index(resultado) #aqui buscamos el valor original donde sea que lo hayamos guardado (no me pregunten donde son 256 lugares donde esconder un bit)
            resultado = (posicion - self.posiciones[i]) % 256 #en lugar de sumar posiciones restamos 

        #en la  maquina original los rotores siempre giran hacia adelante aqui tambien
        #por que necesitamos que la maquina recree el mismo camino que hizo al cifrar el archivo pero...
        #la logica esta o la magia esta en que lo que va en reversa es la direccion en la que el byte cruza los rotores 
        #al cifrar va del 0-7 al desicfrar va del 7-0
        self.rotacion()
        return resultado #entregamos el byte ya descifrado en su valor original
        pass