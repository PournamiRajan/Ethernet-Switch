from switch import switch
import time

text_file= open("write it.text","w")
text_file.write("\n")
text_file.write("SRC_MAC\t\t\t\t\t")
text_file.write("DST_MAC\t\t\t\t\t")
text_file.write("\t\t\t  ")
text_file.write("Action\t\n")
text_file.close()

perf_file= open("performance_summary.text", "w")
perf_file.write("\n")
perf_file.write("# of entries in FWD TABLE\t\t\t")
perf_file.write("Time taken\t\t\t\t\t\n")
perf_file.close()

s = switch()
while True:


    text_file = open("write it.text", "a")
    text_file.write("\n")
    text_file.close()
    in_port = input("Enter input port :").strip()
    SRC_MAC = input("Enter the Source MAC Address :").strip()
    DST_MAC = input("Enter the Destination MAC Address :").strip()
    vlan_id = input("Enter the VLAN ID of incoming packet :").strip()
    time1 = time.time()
    packet = [DST_MAC, SRC_MAC, vlan_id]
    s.validate(packet, in_port)
    s.forward(packet, in_port)
    time2 = time.time()
    perf_file= open("performance_summary.text", "a")
    perf_file.write("\t\t")
    perf_file.write(str(len(s.FWD_TABLE)))
    perf_file.write("\t\t\t\t\t\t")
    perf_file.write(str((time2-time1)*1000))
    perf_file.write("\n")
    perf_file.close()

    #print(s.FWD_TABLE)




