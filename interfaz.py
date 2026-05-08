
from llavero import buscar_llave, crear_llave
from motor import proceso
import sys
import os
import random

def consola():
    banners = [
        r"""
░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓██████████████▓▒░ ░▒▓██████▓▒░       ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░   ░▒▓████████▓▒░▒▓██████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░       ░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓████████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░   ░▒▓█▓▒░          ░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
        """,
        r"""
        ░        ░░   ░░░  ░░        ░░░      ░░░  ░░░░  ░░░      ░░░░░░░░░       ░░░  ░░░░  ░░░░░░░░       ░░░        ░░  ░░░░░░░░        ░░░      ░░
▒  ▒▒▒▒▒▒▒▒    ▒▒  ▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒▒▒   ▒▒   ▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒  ▒
▓      ▓▓▓▓  ▓  ▓  ▓▓▓▓▓  ▓▓▓▓▓  ▓▓▓   ▓▓        ▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓▓       ▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓      ▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓  ▓
█  ████████  ██    █████  █████  ████  ██  █  █  ██        ████████  ████  █████  ███████████  ████  ██  ████████  ███████████  █████        █
█        ██  ███   ██        ███      ███  ████  ██  ████  ████████       ██████  ███████████       ███        ██        █████  █████  ████  █
                                                                                                                                              
        """,
         r"""
            ______      _                          __             ____       ____       
   / ____/___  (_)___ _____ ___  ____ _   / /_  __  __   / __ \___  / / /_____ _
  / __/ / __ \/ / __ `/ __ `__ \/ __ `/  / __ \/ / / /  / / / / _ \/ / __/ __ `/
 / /___/ / / / / /_/ / / / / / / /_/ /  / /_/ / /_/ /  / /_/ /  __/ / /_/ /_/ / 
/_____/_/ /_/_/\__, /_/ /_/ /_/\__,_/  /_.___/\__, /  /_____/\___/_/\__/\__,_/  
              /____/                         /____/                             
        """,
        r"""
                  _ _       ____             _                         _       _____ 
 _ __ _| | |___  / _  |  _   _  __| |  _ __   ___ __ _ _ __ (_) __ _|____ |
| '_ \__ | / _ \| | | | | | | |/ _` | | '_ \ / _ ' _` | '_ \| |/ _` | |_  |
| |_) || | \__  | |_| | | |_| | (_| | | |_) | | | | | | |_) | | | | |___| |
|_.__/__/|_|___/ \____| | .__/ \__,_| |_.__/|_| |_| |_| .__/|_|_| |_|_____|
                         \___|                         \___|               
        """,
        r"""
         ____ ____ ____ ____ ____ ____ _________ ____ ____ _________ ____ ____ ____ ____ ____ 
||E |||n |||i |||g |||m |||a |||       |||b |||y |||       |||D |||e |||l |||t |||a ||
||__|||__|||__|||__|||__|||__|||_______|||__|||__|||_______|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|
        """,
    ]

    print(random.choice(banners))
    print("=" * 55)

    try:
        #desde aqui buscamos la llave
        obtener_llave = buscar_llave()

        if not obtener_llave:
            print("[!] No se detecto la llave físico (.eng).")
            crear = input("[?] ¿Desea inicializar una USB como nueva llave maestra? (s/n): ").strip().lower()
            
            if crear == 's':
                print("\n[*] Creando llave...")
            crear_llave()
            obtener_llave = buscar_llave()

            if not obtener_llave:
                print("No se pudo crear la llave revisa que la usb este conectada correctamente")
                return
            else:
                print("[-] Error: El motor Enigma no puede arrancar sin una llave.")
                return
        print("Llave encontrada maquina lista")

        while True:
            print("\nSelecciona:")
            print("  1. Cifrar archivo")
            print("  2. Descifrar archivo")
            print("  3. Salir")
    
            opcion = input("\nenigma > ").strip()

            if opcion == "3":
                print("[*] Cerrando.")
                break

            if opcion not in ("1", "2"):
                print("[-] Opcion inválida.\n")
                continue

            archivo = input("Ruta del archivo (puedes arrastrarlo aquí): ").strip()
            archivo = archivo.strip("'\"")

           #dirigimos segun la opcion
            modo = "Cifrar" if opcion == "1" else "Descifrar"
            
            try:
                #llamamos a la maquina
                proceso(modo, archivo, obtener_llave)

                #aqui le damos control al usuario si quiere borar el archivo original o no si lo quitamos esto se vuelve un ransomware y no queremos eso... aun
                limpiar = input(f"\n¿Desea eliminar el archivo original ('{archivo}')? (s/n): ").strip().lower()
                if limpiar == "s":
                    if os.path.exists(archivo):
                        os.remove(archivo)
                        print("[*] Archivo original eliminado.")
                else:
                    print("[*] Archivo original aun disponible.")

            except Exception as e:
                print(f"[-] Error durante el proceso: {e}")
            
            print("-" * 55)

    except KeyboardInterrupt:
        print("\n[*] Interrupcion de usuario detectada. Saliendo...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] ERROR FATAL DEL SISTEMA :C : {e}")
        sys.exit(1)