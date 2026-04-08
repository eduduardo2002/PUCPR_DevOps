import socket

def ckeck_conexion():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except:
        return False

if ckeck_conexion():
    print("Conexion OK")
else:
    print("Conexion invalid")