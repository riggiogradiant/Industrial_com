from opcua import Client
from opcua import ua

if __name__ == "__main__":
    # Configura la URL del servidor OPC UA
    url = "opc.tcp://0.0.0.0:4840/freeopcua/server/"
    client = Client(url)

    # Configura las credenciales de usuario
    username = "user1"
    password = "pw1"
    client.set_user(username)
    client.set_password(password)

    # Cargar certificados y configurar políticas de seguridad
    client.set_security_string("Basic256Sha256,SignAndEncrypt,cert.pem,key_no_pass.pem")

    try:
        # Conéctate al servidor
        client.connect()
        print("Cliente conectado al servidor OPC UA")

        root = client.get_root_node()
        objects = client.get_objects_node()
        server_node = client.get_server_node()
        server_status = server_node.get_child(["0:ServerStatus"])
        print("\nServer Status: ", server_status.get_value())
        namespaces = client.get_namespace_array()
        print("\nNamespaces: ", namespaces)
        endpoints = client.get_endpoints()
        for endpoint in endpoints:
            print("\nEndpoint: ", endpoint)
        myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyVariable"])
        print("\nCurrent value: ", myvar.get_value())

    except Exception as e:
        print("Error al conectar o interactuar con el servidor OPC UA:", e)

    finally:
        # Desconéctate del servidor
        client.disconnect()
        print("Cliente desconectado del servidor OPC UA")
