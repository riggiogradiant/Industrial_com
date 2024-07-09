from bacpypes.core import run, stop, enable_sleeping
from bacpypes.app import BIPSimpleApplication
from bacpypes.local.device import LocalDeviceObject
from bacpypes.local.object import AnalogValueObject

# Definir el objeto dispositivo BACnet
device_info = {
    'objectName': 'Device1',
    'objectIdentifier': 599,
    'maxApduLengthAccepted': 1024,
    'segmentationSupported': 'segmentedBoth',
    'vendorIdentifier': 15
}

this_device = LocalDeviceObject(**device_info)
this_application = BIPSimpleApplication(this_device, '127.0.0.1')

# Crear y agregar el objeto AnalogValueObject
analog_value = AnalogValueObject(
    objectIdentifier=('analogValue', 1),
    objectName='Temperature Sensor',
    presentValue=23.5,
    description='Sensor de temperatura de ejemplo'
)

this_application.add_object(analog_value)

# Imprimir detalles del objeto creado
print("\nDetalles del objeto AnalogValueObject creado:")
print(f"  Identificador: {analog_value.objectIdentifier}")
print(f"  Nombre: {analog_value.objectName}")
print(f"  Valor presente: {analog_value.presentValue}")
print(f"  Descripción: {analog_value.description}")

# Imprimir detalles del servidor BACnet
print("\nDetalles del servidor BACnet:")
print(f"  Dirección IP: {this_application.localAddress.addrTuple[0]}")
print(f"  Puerto: {this_application.localAddress.addrTuple[1]}")
print(f"  Nombre del dispositivo: {this_device.objectName}")
print(f"  Identificador del dispositivo: {this_device.objectIdentifier}")

# Mantener el servidor corriendo
print("\nServidor BACnet iniciado y listo para descubrir.")
enable_sleeping()
run()

# Para detener el servidor presiona Ctrl+C
