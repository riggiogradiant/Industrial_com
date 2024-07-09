# from bacpypes.core import run, stop, enable_sleeping
# from bacpypes.app import BIPSimpleApplication
# from bacpypes.local.device import LocalDeviceObject
# from bacpypes.pdu import Address
# from bacpypes.apdu import ReadPropertyRequest, ReadPropertyACK
# from bacpypes.primitivedata import ObjectIdentifier, Unsigned
# from bacpypes.iocb import IOCB

# # Definir el objeto dispositivo BACnet del cliente
# client_info = {
#     'objectName': 'ClientDevice',
#     'objectIdentifier': 600,
#     'maxApduLengthAccepted': 1024,
#     'segmentationSupported': 'segmentedBoth',
#     'vendorIdentifier': 15
# }

# this_device = LocalDeviceObject(**client_info)
# this_application = BIPSimpleApplication(this_device, '10.5.4.87')

# # Dirección del dispositivo servidor
# server_address = Address('127.0.0.1')

# # Crear una solicitud de lectura
# request = ReadPropertyRequest(
#     objectIdentifier=('analogValue', 1),
#     propertyIdentifier='presentValue'
# )
# request.pduDestination = server_address

# # Crear el IOCB
# iocab = IOCB(request)

# # Manejar la respuesta
# def request_complete(iocb):
#     if iocb.ioResponse:
#         response = iocb.ioResponse
#         if isinstance(response, ReadPropertyACK):
#             print("Valor del sensor de temperatura:", response.propertyValue.cast_out(Unsigned))
#         else:
#             print("Error en la lectura:", response)
#     elif iocb.ioError:
#         print("Error en la solicitud:", iocb.ioError)

#     stop()  # Detener el cliente después de recibir la respuesta

# # Asignar la función de callback al IOCB
# iocab.add_callback(request_complete)

# # Enviar la solicitud de lectura
# this_application.request_io(iocab)

# # Mantener el cliente corriendo
# enable_sleeping()
# run()


from bacpypes.core import run, stop, enable_sleeping
from bacpypes.app import BIPSimpleApplication
from bacpypes.local.device import LocalDeviceObject
from bacpypes.pdu import Address
from bacpypes.apdu import ReadPropertyRequest, ReadPropertyACK
from bacpypes.primitivedata import ObjectIdentifier, Unsigned
from bacpypes.iocb import IOCB

# Definir el objeto dispositivo BACnet del cliente
client_info = {
    'objectName': 'ClientDevice',
    'objectIdentifier': 600,
    'maxApduLengthAccepted': 1024,
    'segmentationSupported': 'segmentedBoth',
    'vendorIdentifier': 15
}

this_device = LocalDeviceObject(**client_info)
this_application = BIPSimpleApplication(this_device, '10.5.4.87')

# Dirección del dispositivo servidor
server_address = Address('127.0.0.1')

# Crear una solicitud de lectura
request = ReadPropertyRequest(
    objectIdentifier=('analogValue', 1),
    propertyIdentifier='presentValue'
)
request.pduDestination = server_address

# Crear el IOCB
iocab = IOCB(request)
print("EL IOCAB ES: {}".format(iocab))

# Manejar la respuesta
def request_complete(iocb):
    if iocb.ioResponse:
        response = iocb.ioResponse
        print("[+]La response es: {}".format(response))
        if isinstance(response, ReadPropertyACK):
            print("Valor del sensor de temperatura:", response.propertyValue.cast_out(Unsigned))
        else:
            print("Error en la lectura:", response)
    elif iocb.ioError:
        print("Error en la solicitud:", iocb.ioError)

    stop()  # Detener el cliente después de recibir la respuesta


# Asignar la función de callback al IOCB
iocab.add_callback(request_complete)

# Enviar la solicitud de lectura
this_application.request_io(iocab)
print("[+] SOLICITUD ENVIADA")

# Mantener el cliente corriendo
enable_sleeping()
run()
