from opcua import Client
import time
#OPC UA Server Simulator from Integration Objects
url = "opc.tcp://desktop-vics7it:62640/IntegrationObjects/ServerSimulator/"
nodeId = "ns=2;s=Tag7"
client = Client(url)
client.connect()
try:
    while True:
        node = client.get_node(nodeId)
        value = node.get_value()
        print(value)
        time.sleep(10)
except KeyboardInterrupt:
    print("READING END :( SEE YOU SOON")        
client.disconnect()