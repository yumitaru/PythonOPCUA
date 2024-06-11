from opcua import Client
import time

#OPC UA Server Simulator from Integration Objects
url = "opc.tcp://desktop-vics7it:62640/IntegrationObjects/ServerSimulator/"
nodeId = "ns=2;s=Tag7"
client = Client(url)
client.connect()

counter = 0
try:
    while True:
        node = client.get_node(nodeId)
        value = int(counter)
        node.set_data_value(value)
        counter = counter + 1
        time.sleep(10)
except KeyboardInterrupt:
    print("WRITING END :( SEE YOU SOON")        
client.disconnect()