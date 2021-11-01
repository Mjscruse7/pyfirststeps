aclNum =  int(input("Cuál es el número IPV4 ACL? "))

if aclNum >= 1 and aclNum <= 99:
    print("Este es un ACL IPV4 estándar. ")
elif aclNum >= 100 and aclNum <= 199:
    print("Este es una ACL IPV4 extendida. ")
else:
    print("Esta ACL IPV4 no es extendida o estandar. ")

 