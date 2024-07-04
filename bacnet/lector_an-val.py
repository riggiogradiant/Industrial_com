import BAC0

# Configuración del segundo dispositivo BACnet
device2 = BAC0.lite(ip='127.0.0.1', port=47810)

# Dirección del primer dispositivo BACnet (Servidor)
server_ip = '127.0.0.1'
server_port = 47808  # Asegúrate de que el puerto sea el mismo en el servidor y cliente
server_address = f"{server_ip}:{server_port}"

# Identificador del objeto a leer
object_identifier = 'analogValue:1'

# Leer el valor presente del objeto en el servidor
present_value = device2.read(f"{server_address} {object_identifier} presentValue")

# Imprimir el valor leído
print(f"Present Value of the object: {present_value}")

print("Cliente BACnet listo.")
