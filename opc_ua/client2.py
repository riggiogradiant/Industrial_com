from opcua import Client

if __name__ == "__main__":
    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    try:
        client.connect()
        print("++++++ CONNECTED ++++++")
    finally:
        client.disconnect()
