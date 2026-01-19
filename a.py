from netmiko import ConnectHandler
import yaml

with open ("info.yaml") as target_file:
    devices =yaml.safe_load(target_file)

    device = devices["device"]

for dev in device: 
    with ConnectHandler(**dev) as net_connect: 
        output = net_connect.send_command("show ip int brief")
        print (output)