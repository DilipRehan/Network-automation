from netmiko import ConnectHandler
import yaml
from rich import print as rprint

with open ("device.yaml","r") as target_file:
    device = yaml.safe_load(target_file)


    #Access to the device dictionary inside the yaml file
    dev = device["device"]

    # Establishing connection to the device
    with ConnectHandler(**dev) as net_connect:
        output = net_connect.send_command("show running-config ")
        print(output)

    with ConnectHandler(**dev) as net_connect2:
        output2 = net_connect2.send_command("show snmp community",use_textfsm=True)
        rprint(output2)
        rprint(output2[1]["name"]) # Accessing the 'name' field from the second entry
        if output2[0]["index"] == "cisco0":
            rprint("This is a Cisco Device")

