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

    try:
        while True:
            conn, addr = sock.accept()
            print(f"Conexion establecida con {addr}")
            thread = threading.Thread(target=handle_connection, args=(conn, addr))
            thread.start()
            threads.append(thread)

            th_alive = True

            if th_alive:
                # Imprimir el estado de todos los hilos
                print("Hilos totales: ",
                      [(thread.name, thread.ident, thread.is_alive(), thread.native_id) for thread in threads])

                # Imprimir el estado de los hilos activos
                print("Hilos activos: ",
                      [(thread.name, thread.ident, thread.is_alive(), thread.native_id) for thread in threads if
                       thread.is_alive()])

                # Imprimir el resultado de check_threads_alive
                print("¿Hay hilos activos?:", check_threads_alive(threads))

                sleep(0.5)  # Espera antes de volver a comprobar el estado de los hilos

            print(" [**] Hilos totales: ",
                  [(thread.name, thread.ident, thread.is_alive(), thread.native_id) for thread in threads])
            if not check_threads_alive(threads) and len(threads) > 1:
                print("[+] FIN DE LA SESIÓN")
                threads.clear()


    except KeyboardInterrupt:
        print("\nServidor detenido.")
    finally:
        print("FIN DE TODOS LOS THREADS")
        sock.close()


if __name__ == "__main__":
    main()

