from ncclient import manager #manager object to connect to the device
from xml.dom import minidom #minidom to pretty print the xml output



my_device = {
    "host": "10.10.20.48",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345",
    "hostkey_verify": False
}

with manager.connect(**my_device) as target_file:
    output = target_file.get_config(source="running", filter=("xpath", "/native/banner/motd/banner")).xml #define xpath filter and display the banner motd
    print(minidom.parseString(output).toprettyxml())