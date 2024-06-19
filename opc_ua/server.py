import sys

# Agrega el directorio padre al inicio del PATH para buscar módulos
sys.path.insert(0, "..")
import time
from opcua import Server

if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://industrial_com_opc-ua"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 0.0)
    myvar.set_writable()    # Set MyVariable to be writable by clients --> clients can update the value
    myvar2 = myobj.add_variable(idx, "MyVariable2", 10.0)
    myvar2.set_writable()    # Set MyVariable2 to be writable by clients

    myvar3 = myobj.add_variable(idx, "MyVariable3", 20.0)
    myvar3.set_writable()    # Set MyVariable3 to be writable by clients

    myvar4 = myobj.add_variable(idx, "MyVariable4", 30.0)
    myvar4.set_writable()    # Set MyVariable4 to be writable by clients



    server.start()

    # increase myvariable by 0.1 each second
    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            myvar.set_value(count)
    finally:
        #close connection, remove subscriptions, etc
        server.stop()