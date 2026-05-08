from llavero import buscar_llave
from maquina import Enigma

#Esta funcion es todo el proceso de la maquina
def proceso(modo,ruta,llave):
    #se verifica la ruta del archivo
    if not ruta:
        print(f"[-] No se proporciono ninguna ruta")
        return

    #Tomamos la llave y comenzamos el proceso de cifrado
    try:
        #la maquina toma la llave y el archivo carga los datos
        maquina = Enigma(llave)
        with open(ruta,"rb") as archivo_entrada:
            datos = archivo_entrada.read()
        
        bytes_resultantes = bytearray()

        #llamamos a la funcion correspondiente para el cifrado y en la salida cambiamos la terminacion del archivo
        if modo == "Cifrar":
            for byte in datos:
                    bytes_resultantes.append(maquina.trituradora(byte))
            salida = ruta + ".eng"
        #si aqui llamamos a la funcion para descifrar algun archivo con ello eliminas la 
        else:
            for byte in datos:
                bytes_resultantes.append(maquina.pegadora(byte))
            salida = ruta.replace(".eng","")

        with open(salida, 'wb') as archivo_salida:
            archivo_salida.write(bytes_resultantes)
        print(f"[+] Listones", f"Archivo procesado con exito -> {salida}")

    except Exception as e:
        print(f"[!] Error critico proceso finalizado", f"La maquina se rompio en {e} checa eso porfa")