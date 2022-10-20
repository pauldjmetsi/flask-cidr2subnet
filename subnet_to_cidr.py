## Convert subnet mask to cidr ##
def netmask_to_cidr(netmask):
    cidr = sum(bin(int(x)).count('1') for x in netmask.split('.'))
    #print(cidr)
    return cidr 

netmask_to_cidr('255.255.255.0')