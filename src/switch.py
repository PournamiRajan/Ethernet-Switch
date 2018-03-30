import sys
class switch:

    FWD_TABLE = {}
    vlan_to_ports = {'100': ['0', '1', '2'], '200': ['3', '4', '5', '6'], '300': ['7', '8', '9']}

    file = open("mac_to_port.txt", "r")
    for line in file:
        a = line.split("port")
        vlanid = a[1][8:11]
        key = vlanid+a[0].strip()
        FWD_TABLE[key] = a[1][0]
    file.close()

    def learn(self, packet, in_port):
        SRC_MAC = packet[1]
        vlan_id = packet[2]
        key = vlan_id + SRC_MAC
        if key not in self.FWD_TABLE:
            self.add_to_FWD_TABLE(key, str(in_port))


    def forward(self, packet, in_port):
        DST_MAC = packet[0]
        vlan_id = packet[2]
        self.learn(packet, in_port)
        key = vlan_id + DST_MAC
        if self.if_present_in_FWD_TABLE(key):
            out_port = self.get_port_from_FWD_TABLE(key)
            self.sendpacket(out_port, in_port, packet)
        else:
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
            print("Invalid entry : VLAN source mapping not found")
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

    def check_(self, mac_int):
        if mac_int <= 255:
            return "The MAC address has the proper format"
        else:
            return "the MAC address does not have the proper format"

    def add_to_FWD_TABLE(self, key, in_port):
        self.FWD_TABLE[key] = in_port

    def if_present_in_FWD_TABLE(self, key):
        if key in self.FWD_TABLE:
            return True
        else:
            return False

    def get_port_from_FWD_TABLE(self, key):
        port = self.FWD_TABLE[key]
        return port






