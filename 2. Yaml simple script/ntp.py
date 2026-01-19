from netmiko import ConnectHandler
import yaml 

# loading the Global configurations from a text file
with open ("Global_configs.txt", "r") as target_file:
    my_config = target_file.readlines()

# loading the device information from a yaml file
with open("devices.yaml") as target_devices:
    my_devices = yaml.safe_load(target_devices)

# connecting to the device and sending commands
    dev = my_devices["device"]


# Show IP Interface Brief (send command)
    with ConnectHandler(**dev) as net_connect:
        output = net_connect.send_command("show ip interface brief")
        print(output)

# Send Global Configurations (send config set)
    with ConnectHandler(**dev) as conf:
        exec = conf.send_config_set(my_config)
        output2 = conf.send_command ("show run | include banner")
        print (output2)