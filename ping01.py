import os
with open("ip_list.txt") as file:
    park = file.read()
    park = park.splitlines()
    print("{park} \n")
for ip in park:
    response = os.popen(f"ping {ip} ").read()
    if("Request timed out." or "unreachable") in response:
        print(response)
        f = open("info_output.txt","a")
        f.write(str(ip) + 'link is down '+'\n')
        f.close()
    else:
        print(response)
        f = open("info_output.txt","a")
        f.write(str(ip) +' is up '+'\n')
        f.close()
with open("info_output.txt") as file:
    output = file.read()
    f.close()
    print(output)
with open("info_output.txt","w") as file:
    pass
    