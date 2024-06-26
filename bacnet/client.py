import BAC0

# # Función para manejar la conexión exitosa
# def handle_connection():
#     print("CONNECTED")

client = BAC0.lite(ip='127.0.0.1', port= 47809)

try:
    client.whois()
    client.iam() #Devuelve True

    print("Cliente conectado...")
    # Enviar una solicitud de escritura al servidor
    
    target_address = '127.0.0.1'
    object_type = 'analogValue'
    instance_number = 1
    property_name = 'presentValue'
    value_to_write = 42.0

    # Enviar una solicitud de escritura al servidor
    client.write(target_address, (object_type, instance_number), property_name, value_to_write)
    


    # Enviar una solicitud de lectura al servidor
    result = client.read('127.0.0.1', ('analogValue', 1), 'presentValue')
    print(f"Resultado de la lectura: {result}")

except KeyboardInterrupt:
    print("Cliente detenido por el usuario.")
