import socket
import threading
from time import sleep


def handle_connection(conn, addr):
    print(f"Conexion {addr} establecida")
    while True:
        try:
            data = conn.recv(1024)
        except ConnectionResetError as er:
            print(er)
            break
        if not data:
            break
        print(f"Recibido: {data}")
        conn.sendall(data)
    print(f"Conexion {addr} cerrada")
    conn.close()

def check_threads_alive(threads):
    """
    Esta función recibe una lista de hilos y devuelve True si algún hilo está activo,
    o False si todos los hilos están inactivos.
    """
    return any(thread.is_alive() for thread in threads)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 5020))
    sock.listen(1)
    print("Servidor escuchando en el puerto 5020")

    threads = []
    first_connection = False
    timeout_duration = 20

    try:
        while True:
            if first_connection:
                sock.settimeout(timeout_duration)  # Set t-out after 1 connection
            try:
                conn, addr = sock.accept()
            except socket.timeout:  # If t-out -> no more connections on that session
                print(f"[+] FIN DE SESIÓN DE SOLO 1 CONEXIÓN")
                threads.clear()
                sock.settimeout(None)
                first_connection = False
                continue

            print(f"Conexion establecida con {addr}")
            first_connection = True  # First connection established
            thread = threading.Thread(target=handle_connection, args=(conn, addr))
            thread.start()
            threads.append(thread)

            sleep(0.5)

            print("Hilos totales: ",
                  [(thread.name, thread.ident, thread.is_alive(), thread.native_id) for thread in threads])

            print("Hilos activos: ",
                  [(thread.name, thread.ident, thread.is_alive(), thread.native_id) for thread in threads if
                   thread.is_alive()])

            # Check if all threads are alive and more than 1
            if not check_threads_alive(threads) and len(threads) > 1:
                print("[+] FIN DE LA SESIÓN")
                sock.settimeout(None)
                first_connection = False
                threads.clear()

    except KeyboardInterrupt:
        print("\nServidor detenido.")
    finally:
        print("FIN DEL PROGRAMA")
        sock.close()


if __name__ == "__main__":
    main()

