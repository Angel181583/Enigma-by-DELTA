#Esta libreria tiene como fin crear la llave para encriptar y leer las USB conectadas a la computadora para poder inyectar la llave
#No me pregunten como funciona lo hice a las 3 am :3
import os
import hashlib
import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

#Primeramente esta funcion tiene como fin buscar y crear una lista de las usb montadas en el equipo
def obtener_usb():
    usb = []
    # Filtramos solo los discos extraíbles
    for p in psutil.disk_partitions():
        if 'removable' in p.opts:
            try:
                usage = psutil.disk_usage(p.mountpoint)
                gb_size = usage.total / (1024**3)
                usb.append({
                    "ruta": p.mountpoint, 
                    "size": f"{gb_size:.2f} GB"
                })
            except Exception:
                pass # Ignoramos si la unidad está vacia o no se deja leer
    return usb

#Esta funcion busca la llave entre todas las usb momntadas en el equipo 
def buscar_llave():   
    lectura=obtener_usb()#llamamos a la super funcion que crea las listas de dispositivos
    for usb in lectura:
        archivo_objetivo = os.path.join(usb['ruta'], "llave.eng")#buscamos la llave
        if os.path.exists(archivo_objetivo):
            print(f"[*] Llave detectada en: {usb['ruta']}")
            with open(archivo_objetivo, "rb") as f:
                return list(f.read())#leemos la llave y tomamos su valor 
    return None 

#Esta es la funcion donde se crea la llave aqui hay interfaces y la funcion que genera el hash
def crear_llave():
    usb = obtener_usb()
    
    if not usb:
        console.print("[bold red]❌ Error: Conecta una USB primero.[/bold red]")
        return

    # Una tablita locochona :3 
    tabla = Table(title="Dispositivos detectados")
    tabla.add_column("ID", style="cyan", justify="center")
    tabla.add_column("Ruta", style="cyan")
    tabla.add_column("Tamaño", style="green")

    for i, dispositivo in enumerate(usb):
        tabla.add_row(str(i), dispositivo['ruta'], dispositivo['size'])

    console.print(tabla)

    # Menu para que el usuario seleccione el dispositivo que se convertira en COLD STORAGE
    try:
        opcion = int(Prompt.ask("Selecciona el [bold cyan]ID[/bold cyan] destino", choices=[str(i) for i in range(len(usb))]))
    except ValueError:
        return

    destino = usb[opcion]['ruta']
    
    with console.status("[bold yellow]Generando llave..."):
        ruido = os.urandom(2048)#toma 2kb de ruido del equipo actual
        key = hashlib.sha256(ruido).digest() #creamos hash unico de una sola vuelta para iniciar  la maquina
        key_path = os.path.join(destino, "llave.eng")#guardamos el hash en un archivo llamado llave con la extencion .eng (enigma)
        try:
            with open(key_path, "wb") as f:
                f.write(key)
            console.print(f"\n[bold green]✔ LISTO:[/bold green] Llave guardada en [white]{key_path}[/white]")
            console.print("[dim]Ojo: Sin este archivo no se podra recuperar nada que haya sido cifrado con 'Enigma by DELTA'.[/dim]")
        except Exception as e:
            console.print(f"\n[bold red]❌ Error al intentar escribir en la USB Checa eso porfa UwU:[/bold red] {e}")

if __name__ == "__main__":
    crear_llave()

#Made by D3m05 UwU 