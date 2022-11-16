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
# discover the hostname from the prompt
hostname = net_connect.send_command('show run | i host')
hostname.split(" ")
#hostname, device = hostname.split(" ")
hostname, device, *rest = hostname.split(" ")
print(hostname)
print(device)
print("Backing up " + device)
filename = "C:/pythoncode/devices01.txt"
#save back up in samefolder as script use below line and comment out above line
#filename = device + '.txt'
showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a") # in append mode
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")
# finally close the connection
net_connect.disconnect()
