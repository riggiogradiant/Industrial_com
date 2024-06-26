# import BAC0

# # Función para manejar solicitudes de lectura
# def handle_read_request(obj_type, obj_instance, prop):
#     # Aquí podrías implementar la lógica para manejar la solicitud de lectura
#     print(f"Request to read {obj_type}:{obj_instance} - {prop}")
#     # Por ejemplo, podrías devolver un valor específico o leer desde algún sensor


# device_server = BAC0.lite(ip='127.0.0.1', port = 47808)


# try:
#     while True:
#         device_server.whois()
#         device_server.iam() #Devuelve True
#         #device_server.read( handle_read_request )

# except KeyboardInterrupt:
#     print("Cerrado con exito")

import BAC0

# Función para manejar solicitudes de lectura
def handle_read_request(obj_type, obj_instance, prop):
    print(f"Request to read {obj_type}:{obj_instance} - {prop}")
    if obj_type == 'analogValue' and prop == 'presentValue':
        return analog_value['presentValue']
    return None

# Función para manejar solicitudes de escritura
def handle_write_request(obj_type, obj_instance, prop, value):
    print(f"Request to write {obj_type}:{obj_instance} - {prop} with value {value}")
    if obj_type == 'analogValue' and prop == 'presentValue':
        analog_value['presentValue'] = value
        return True
    return False

# Configurar servidor BAC0
device_server = BAC0.lite(ip='127.0.0.1', port=47808)

# Crear un objeto AnalogValue simulado
analog_value = {'objectType': 'analogValue', 'instanceNumber': 1, 'presentValue': 0, 'objectName': 'MyAnalogValue'}

# Asignar las funciones de manejo de lectura/escritura
# device_server.this_application.add_read_handler(handle_read_request)
# device_server.this_application.add_write_handler(handle_write_request)

try:
    print("Servidor corriendo...")
    device_server.iam()
    while True:
        pass
except KeyboardInterrupt:
    print("Servidor detenido por el usuario.")


