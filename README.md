# Industrial_com
Establecimiento de conexión entre cliente servidor OPC-UA y entre dispositivos BACnet.

## OPC UA
1. Servidor OPC con 1 objeto y 1 variable la cual aumenta un 0.1 su valor cada segundo que pasa.
2. Cliente OPC que se conecta al servidor y muestra el valor de la variable en el momento de la conexión.

Usando la herramienta opcua-client, podemos tener una interfaz gráfica en la que monitorizar nuestro servidor. Para lanzar introducimos el siguiente comando en una terminal anaconda: opcua-client.

Vease un ejemplo de la interfaz: 
![Interfaz Gráfica](/home/riggio/Industrial_com/opc-ua-client-graph.png)