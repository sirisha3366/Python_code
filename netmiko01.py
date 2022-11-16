from netmiko import ConnectHandler
#First create the device object using a dictionary
CSR = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345"
}
# Next establish the SSH connection
net_connect = ConnectHandler(**CSR)
# Then send the command and print the output

output = net_connect.send_command('show ip ro')

print (output)
# Finally close the connection
net_connect.disconnect()


