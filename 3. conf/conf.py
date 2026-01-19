from netmiko import ConnectHandler
import yaml

with open ("device.yaml","r") as target_file:
    device = yaml.safe_load(target_file)


    #Access to the device dictionary inside the yaml file
    dev = device["device"]

    # Establishing connection to the device
    with ConnectHandler(**dev) as net_connect:
        output = net_connect.send_command("show running-config ")
        print(output)

