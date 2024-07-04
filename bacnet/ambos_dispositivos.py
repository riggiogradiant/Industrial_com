import BAC0


# Configuración del primer dispositivo BACnet
device1 = BAC0.connect(ip='127.0.0.1', port=47809)

print("\n")

# Configuración del segundo dispositivo BACnet
device2 = BAC0.connect(ip='127.0.0.1', port=47810)






















# Función para imprimir el valor del objeto en el dispositivo2
def print_value(value):
    print(f"Received value: {value}")

# Suscribirse a los cambios del objeto en el dispositivo2
device2.subscribe_to_cov(
    ('analogValue', 1),
    print_value,
    confirmed_notifications=True,
    lifetime=60000
)

# Escribir un valor en el objeto del dispositivo2 desde el dispositivo1
device1.write(('analogValue', 1), 'presentValue', 42.0)

# Mantener el programa en ejecución para permitir la recepción de datos
import time
while True:
    time.sleep(1)
