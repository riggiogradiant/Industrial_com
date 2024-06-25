import BAC0

# Función para manejar la conexión exitosa
def handle_connection():
    print("CONNECTED")

# Dirección IP del servidor BACnet
server_ip = '127.0.0.1'

# Crear un cliente BACnet que se conecta al servidor
client = BAC0.lite(ip=server_ip)

# Manejar eventos para el cliente BACnet
try:
    client.whois()
    client.iam()
    handle_connection()

except KeyboardInterrupt:
    # Manejar la interrupción del teclado si se desea
    print("Cliente detenido por el usuario.")
