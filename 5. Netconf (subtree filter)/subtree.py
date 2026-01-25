from ncclient import manager
from xml.dom import minidom

dev_conn = {
    "host": "10.10.20.48",
    "port": "830", 
    "username": "developer", 
    "password": "C1sco12345",
    "hostkey_verify": False
}


sub_tree_filter ="""
 <routing-state xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
 <routing-protocols>
 <name>
 </name>
 </routing-protocols>
 </routing-state>
"""

with manager.connect(**dev_conn) as netconf_target:
    ouput = netconf_target.get_config(source="running", filter=("subtree", sub_tree_filter)).xml