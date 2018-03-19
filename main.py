from switch import switch
import sys
import time

text_file= open("write it.text","w")
text_file.write("\n")
text_file.write("SRC_MAC\t\t\t\t\t")
text_file.write("DST_MAC\t\t\t\t\t")
text_file.write("Port No\t\t")
text_file.write("Action\t\n")
text_file.close()
s = switch()
while True:


    text_file = open("write it.text", "a")
    text_file.write("\n")
    text_file.close()
    SRC_MAC = input("Enter the Source MAC Address :")
    DST_MAC = input("Enter the Destination MAC Address :")
    time1 = time.time()
    print("time1:", time1)
    if DST_MAC == SRC_MAC:
        print("Destination and source cannot be same. Try Again !! ")
        sys.exit()
    packet = [DST_MAC, SRC_MAC]
    s.validate(packet)
    s.forward(packet)
    time2=time.time()
    print("time2:", time2)
    print(s.FWD_TABLE)
    print("Total time for forwarding ", (time2-time1)*1000, "ms")




