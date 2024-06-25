import sys

sys.path.insert(0, "..")
from opcua import ua, uamethod, Server
from opcua.server.user_manager import UserManager
from time import sleep

users_db = {
    'user1': 'pw1',
    'user2': 'pw2',
    'user3': 'pw3'
}

# Función del manejador de usuarios
def user_manager(isession, username, password):
    if username in users_db and password == users_db[username]:
        isession.user = UserManager.User  # Asigna un rol o permiso al usuario
        return True
    return False

if __name__ == "__main__":

    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # Configura nuestro propio espacio de nombres
    uri = "http://industrial_com_opc-ua"
    idx = server.register_namespace(uri)

    objects = server.get_objects_node()

    # Poblar nuestro espacio de direcciones
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 0.0)
    myvar.set_writable()    
    myvar2 = myobj.add_variable(idx, "MyVariable2", 10.0)
    myvar2.set_writable()   
    myvar3 = myobj.add_variable(idx, "MyVariable3", 20.0)
    myvar3.set_writable()  
    myvar4 = myobj.add_variable(idx, "MyVariable4", 30.0)
    myvar4.set_writable()   

    
    server.set_security_policy([
        ua.SecurityPolicyType.NoSecurity  # Deshabilita el cifrado
    ])

    policyIDs = ["riggio"]
    server.set_security_IDs(policyIDs)
    server.user_manager.set_user_manager(user_manager)

    # Modelado OPC-UA
    root_node = server.get_root_node()
    object_node = server.get_objects_node()
    server_node = server.get_server_node()

    server.start()

    try:
        count = 0
        while True:
            sleep(1)
            count += 0.1
            myvar.set_value(count)
    finally:
        server.stop()
