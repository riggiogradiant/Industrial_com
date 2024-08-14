import socket

def handle_connection(conn, addr):
    data = ""
    try:
        print(f"Conexion iniciada desde {addr}")
        while True:
            try:
                data = conn.recv(1024)
            except ConnectionResetError as err:
                print(err)
                pass
            if not data:
                break
    except OSError as e:
        if e.errno == 107:  # Transport endpoint is not connected
            pass
        else:
            raise
    finally:
        print(f"Conexion finalizada desde {addr}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 5020))
        s.listen(5)
        print("Escuchando en puerto 5020...")
        while True:
            conn, addr = s.accept()
            print(f"Inicio de sesión desde {addr}")
            handle_connection(conn, addr)
            print(f"Fin de sesión desde {addr}")

if __name__ == "__main__":
    main()
