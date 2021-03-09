import socket

def print_machine_info():
    host_name = socket.gethostname()
    fqdn_name = socket.getfqdn()
    ip_address = socket.gethostbyname(fqdn_name)
    so = socket.gethostbyaddr(ip_address)
    print ("Host name: %s" % host_name)
    print("FQDN name: %s" % fqdn_name)
    print ("IP address: %s" % ip_address)
    print(so)


if __name__ == '__main__':
    print_machine_info()