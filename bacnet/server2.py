import BAC0

# Configurar y arrancar un dispositivo BACnet
ip_address = '127.0.0.1'  # Dirección IP del dispositivo
port = 47808  # Puerto BACnet

# Crear una instancia BACnet/IP
# bacnet = BAC0.lite(ip=ip_address, port=port)
bacnet = BAC0.lite()
# Enviar un mensaje I-Am manualmente para asegurarse de que el dispositivo es descubrible
iam = bacnet.iam()
print(iam)

print("Servidor BACnet iniciado y listo para descubrir.")

# Mantener el servidor corriendo
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Servidor BACnet detenido.")
