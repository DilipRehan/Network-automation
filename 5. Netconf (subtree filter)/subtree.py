from ncclient import manager
from xml.dom import minidom

dev_conn = {
    "host": "10.10.20.48",
    "port": "830", 
    "username": "developer", 
    "password": "C1sco12345",
    "hostkey_verify": False
}


sub_tree_filter = """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface>
<name>
</name>
</interface>
</interfaces> 
"""



with manager.connect(**dev_conn) as netconf_target:
    output = netconf_target.get_config(source="running", filter=("subtree", sub_tree_filter)).xml
    print(minidom.parseString(output).toprettyxml())