import random
import time

def random_MAC():
    return [ random.randint(0x00, 0xff),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff) ]
def random_PORT() :
    return random.randint(1, 4);

def MACprettyprint(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))

if __name__ == '__main__':
    file = open("mac_to_port.txt", "w")
    time1 = time.time()
    count=0
    for i in range (0,1000):
        file = open("mac_to_port.txt", "a")
        file.write(MACprettyprint(random_MAC()))
        file.write("   port")
        file.write(str(random_PORT()))
        file.write("\n")
        file.close()
        count=count+1
    time2 = time.time()
    print("time taken to generate ", count, " MAC address is ", time2-time1)