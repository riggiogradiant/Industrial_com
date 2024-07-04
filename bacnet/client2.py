import BAC0

# Iniciar la instancia BACnet
# client = BAC0.lite(ip='127.0.0.1', port= 47809)
ip_address = '172.25.24.127'  # Dirección IP del dispositivo
port = 47809  # Puerto BACnet

client = BAC0.lite(port = port)


#Enviar solicitud Who-Is
devices = client.whois()

print("Dispositivos descubiertos:")
for device in devices:
    print(device)
