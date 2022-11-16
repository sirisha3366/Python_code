import os, ipaddress
#os.system will clear the console at the start of the execution
os.system('cls') 
while True:
    ip = input('Enter IP address: ')
    try:
        print(ipaddress.ip_address(ip))
        print('IP Valid')
    except:
        print('_' *50)
        print('IP is not valid')
    finally:
        if ip == 'mango':
            print('Script Finished')
            break