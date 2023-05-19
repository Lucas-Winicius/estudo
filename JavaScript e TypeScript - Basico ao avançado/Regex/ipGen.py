ip = [ 0, 0, 0, 0 ]

while ip[0] <= 255:
    ip[3] += 1
    ipString = f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}"

    with open('ips.txt', 'a') as arquivo:
        arquivo.write(f"{ipString}\n")

    print(ipString)
    
    if ip[3] == 255:
        ip[3] = 0
        ip[2] += 1

    if ip[2] == 255:
        ip[2] = 0
        ip[1] += 1

    if ip[1] == 255:
        ip[1] = 0
        ip[0] += 1
