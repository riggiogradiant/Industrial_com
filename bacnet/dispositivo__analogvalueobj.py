# import BAC0
# from bacpypes.object import AnalogValueObject, BinaryValueObject
# from bacpypes.basetypes import StatusFlags, CharacterString

# # Método para crear el objeto
# def create_object(
#     object_class, oid, objectName, description, presentValue=None, commandable=False
# ):
#     new_object = object_class(
#         objectIdentifier=(object_class.objectType, oid),
#         objectName="{}".format(objectName),
#         presentValue=presentValue,
#         description=CharacterString("{}".format(description)),
#         statusFlags=StatusFlags([0, 0, 0, 0]),
#     )
#     # Aquí deberías llamar a la función para deprecar el mensaje (si aplica)
#     # deprecate_msg()
#     return _make_mutable(new_object, mutable=commandable)

# # Método para establecer el valor presente
# def set_pv(obj=None, value=None, flags=[0, 0, 0, 0]):
#     obj.presentValue = value
#     obj.statusFlags = StatusFlags(flags)

# # Método para hacer que el objeto sea mutable
# def _make_mutable(obj, mutable=False):
#     obj._mutable = mutable
#     return obj

# # Ejemplo de creación de un objeto AnalogValueObject
# analog_value = create_object(
#     AnalogValueObject,
#     oid=1,
#     objectName="Temperature Sensor",
#     description="Sensor de temperatura de ejemplo",
#     presentValue=23.5,
#     commandable=True
# )

# # Establecer el valor presente del objeto
# set_pv(analog_value, value=24.0, flags=[0, 0, 0, 0])

# # Imprimir el objeto para verificar
# print("Object Identifier:", analog_value.objectIdentifier)
# print("Object Name:", analog_value.objectName)
# print("Present Value:", analog_value.presentValue)
# print("Description:", analog_value.description)
# print("Status Flags:", analog_value.statusFlags)
# print("Is Mutable:", analog_value._mutable)

# # Configuración del primer dispositivo BACnet
# device1 = BAC0.lite(ip='127.0.0.1', port=47809)

# iam = device1.iam()
# print(iam)

# print("Servidor BACnet iniciado y listo para descubrir.")

# # Mantener el servidor corriendo
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     print("Servidor BACnet detenido.")

# # Agregar el objeto al dispositivo BACnet
# # device1.add_object(analog_value)

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

# Mantener el servidor corriendo
print("Servidor BACnet iniciado y listo para descubrir.")
enable_sleeping()
run()

# Para detener el servidor presiona Ctrl+C
