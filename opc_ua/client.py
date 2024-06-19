import sys
from opcua import Client, ua

class SubHandler:
    def datachange_notification(self, node, val, data):
        print(f'Variable {node} ha cambiado a: {val}')

# def browse_node(node):
#     children = node.get_children()
#     for child in children:
#         browse_name = child.get_browse_name()
#         display_name = child.get_display_name().Text
#         node_class = child.get_node_class()
#         if node_class == ua.NodeClass.Variable:
#             print(f"Variable found: {display_name} (Browse Name: {browse_name}, Node ID: {child.nodeid})")
#         browse_node(child)

if __name__ == "__main__":
    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    try:
        client.connect()
        root = client.get_root_node()
        objects = client.get_objects_node()
        # browse_node(objects)
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

        myvar.set_value(ua.Variant(42, ua.VariantType.Int32))
        print("\nNew value set --> Myvar = {}".format(myvar.get_value()))

        # while True:
        #     handler = SubHandler()
        #     sub = client.create_subscription(500, handler)
        #     handle = sub.subscribe_data_change(myvar)
    finally:
        client.disconnect()
