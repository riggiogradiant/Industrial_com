# import BAC0

# # Crear un dispositivo BACnet que actúa como servidor en localhost
# device_server = BAC0.lite(ip='127.0.0.1')

# # Crear un objeto Analog Value en el servidor
# # device_server.this_application.add_object(BAC0.core.objects.AnalogValueObject(
# #     objectIdentifier=('analogValue', 1),
# #     objectName='TemperatureSensor',
# #     presentValue=22.5,
# # ))

# print("Servidor BACnet configurado en localhost")

import BAC0

# Función para manejar solicitudes de lectura
def handle_read_request(obj_type, obj_instance, prop):
    # Aquí podrías implementar la lógica para manejar la solicitud de lectura
    print(f"Request to read {obj_type}:{obj_instance} - {prop}")
    # Por ejemplo, podrías devolver un valor específico o leer desde algún sensor

# Crear un dispositivo BACnet que actúa como servidor en localhost
device_server = BAC0.lite(ip='127.0.0.1')

# Manejar eventos para mantener el servidor BACnet abierto continuamente
try:
    while True:
        device_server.whois()
        device_server.iam()
        #device_server.read( handle_read_request )

except KeyboardInterrupt:
    print("Cerrado con exito")
