from ncclient import manager #manager object to connec to the device
from xml.dom import minidom #minidom to pretty print the xml output

#device connection details (im using cisco devnet sandbox device)
my_device ={
    "host": "10.10.20.48",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345",
    "hostkey_verify": False
}

#define subtree filter to get all interface information
subtree_filter = """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface>
<name>
</name>
</interface>
</interfaces> 
"""

#connect to the device and get the running configuration with the defined subtree filter
with manager.connect(**my_device) as target: 
    result = target.get_config(source="running", filter=("subtree",subtree_filter)).xml
    print(minidom.parseString(result).toprettyxml()) #pretty print the xml output