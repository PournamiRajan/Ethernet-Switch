import sys
from cuckoo_hash import cuckoo
import random
class switch:

    cuck = cuckoo()
    vlan_to_ports = {'100': ['0', '1', '2'], '200': ['3', '4', '5', '6'], '300': ['7', '8', '9']}

    def debug_stdout(self, sfunc):
         '''print(sfunc)'''

    def debug_stdout2(sfunc):
         '''print(sfunc)'''

    debug = debug_stdout
    debug2 = debug_stdout2


    file = open("mac_to_port.txt", "r")
    for line in file:
        a = line.split("port")
        vlanid = a[1][8:11].strip()
        key = vlanid + a[0].strip()
        key_value_pair = cuck.Pair(key, str(a[1][0]))
        cuck.success = False
        cuck.second = False
        cuck.insert(key_value_pair, 1, random.randint(1, 2))
        cuck.Number_of_entries += 1
        debug2("inserted mac : " + str(a[0].strip()) + ", key = " + str(key_value_pair.getKey()))

    file.close()

    def learn(self, packet, in_port):
        SRC_MAC = packet[1]
        vlan_id = packet[2]
        key = vlan_id + SRC_MAC
        if self.if_present_in_cuckoo_hash_table(key):
            return
        self.insert_into_cuckoo_hash_table(key, str(in_port))
        #self.debug("learning mac :" + SRC_MAC + ", key = " + str(self.cuck.split_add(key)))


    def forward(self, packet, in_port):
        DST_MAC = packet[0]
        vlan_id = packet[2]
        self.learn(packet, in_port)
        key = vlan_id + DST_MAC
        if self.if_present_in_cuckoo_hash_table(key):
            out_port = self.get_port_from_cuckoo_hash_table(key)
            #self.debug("found dst mac entry:" + DST_MAC + ", key = " + str(self.cuck.split_add(key)))
            self.sendpacket(out_port, in_port, packet)
        else:
            #self.debug("could not find dst mac entry:" + DST_MAC + ", key = " + str(self.cuck.split_add(key)))
            self.broadcast(in_port, packet)

    def sendpacket(self, out_port, in_port, packet):
        text_file = open("write it.text", "a")
        text_file.write("\n")
        text_file.write(packet[1])
        text_file.write("\t\t")
        text_file.write(packet[0])
        text_file.write("\t\t\t\t\t")
        if str(out_port) == str(in_port):
            text_file.write("Packet sent on port : " + str(out_port) + "(Suppress)")
        else:
            text_file.write("Packet sent on port : " + str(out_port))
        text_file.close()

    def broadcast(self, in_port, packet):
        vlan = packet[2]
        for port in self.vlan_to_ports[vlan]:
            self.sendpacket(port, in_port, packet)

    def validate(self, packet, in_port):
        SRC_MAC = packet[1]
        DST_MAC = packet[0]
        vlan_id = packet[2]
        if not self.validate_mac_format(SRC_MAC):
            print("Invalid entry : " + SRC_MAC + " not in proper format")
            sys.exit()
        if not self.validate_mac_format(DST_MAC):
            print("Invalid entry : " + DST_MAC + " not in proper format")
            sys.exit()
        if DST_MAC == SRC_MAC:
            print("Invalid entry : Destination and source cannot be same. Try Again !! ")
            sys.exit()
        if vlan_id not in self.vlan_to_ports:
            print("Invalid entry : VLAN_ID not found/configured")
            sys.exit()
        if in_port not in self.vlan_to_ports[vlan_id]:
            print("Invalid entry : VLAN port mapping not found")
            sys.exit()

    def validate_mac_format(self, mac):
        valid = True
        if not (len(mac) == 17):
            valid = False
        byte_list = mac.split(":")
        for each_byte in byte_list:
            try:
                mac_int = int(each_byte, 16)
                if not mac_int <= 255:
                    valid = False
            except ValueError:
                valid = False
        return valid


    def insert_into_cuckoo_hash_table(self, key, in_port):
        key_value_pair = self.cuck.Pair(key, in_port)
        self.cuck.success = False
        self.cuck.insert(key_value_pair, 1, 1)

    def if_present_in_cuckoo_hash_table(self, key):
        return self.cuck.search(key)

    def get_port_from_cuckoo_hash_table(self, key):
        return self.cuck.find_port(key)







