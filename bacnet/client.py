import BAC0

# # Función para manejar la conexión exitosa
# def handle_connection():
#     print("CONNECTED")

client = BAC0.lite(ip='127.0.0.1', port= 47809)

try:
    devices = client.whois()
    print("DISPOSITIVOS DESCUBIERTOS: {}".format(devices))
    client.iam() #Devuelve True

    print("Cliente conectado...")
    # Enviar una solicitud de escritura al servidor
    
    # # Dirección del dispositivo en formato Network:Address
    # addr = '127.0.0.1:47808'

    # # Construir el argumento de la función write
    # args = f'{addr} analogValue 1 presentValue 22.0 - 8'

    # # Llamar a la función write
    # status = client.write(args)

    # # Imprimir el resultado
    # if status:
    #     print("Escritura exitosa")
    # else:
    #     print("Fallo en la escritura")

    #     # Enviar una solicitud de lectura al servidor
    #     result = client.read('127.0.0.1', ('analogValue', 1), 'presentValue')
    #     print(f"Resultado de la lectura: {result}")

except KeyboardInterrupt:
    print("Cliente detenido por el usuario.")
