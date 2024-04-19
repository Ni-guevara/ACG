ACLnum=int (input("¿Cual es tu numero de ACL IPv4?"))
if ACLnum >= 1 and ACLnum <= 99:
    print("Corresponde a un ACL Ipv4 standard")
elif ACLnum >= 100 and ACLnum <= 199:
    print ("Corresponde a una ACL IPv4 extended")
else:
    print ("Este no corresponde a un acl ipv4 standard o extended")