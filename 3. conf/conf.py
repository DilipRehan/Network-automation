from netmiko import ConnectHandler
import yaml

with open ("device.yaml","r") as target_file:
    device = yaml.safe_load(target_file)

    dev = device["device"]

    with ConnectHandler(**dev) as net_connect:
        output = net_connect.send_command("show running-config | include hostname")

