import sys
class switch:
    FWD_TABLE = {}
    # data_input1 --> Mac address to port mapping
    data_input1 = {'20-55-24-BD-4D-4C': 1, '10-75-D3-79-22-CF': 2, '5F-CA-A5-88-BC-38': 3, '6B-26-7B-C4-51-C7': 4}

    # FWD_TABLE={}

    def learn(self, SRC_MAC):
        if not SRC_MAC in self.FWD_TABLE:
            self.FWD_TABLE[SRC_MAC] = self.data_input1[SRC_MAC]

    def forward(self, packet):
        SRC_MAC = packet[1]
        DST_MAC = packet[0]
        self.learn(SRC_MAC)
        if DST_MAC in self.FWD_TABLE:
            port = self.FWD_TABLE[DST_MAC]
            self.sendpacket(port, packet)
        else:
            input_port = self.data_input1[SRC_MAC]
            self.broadcast(input_port, packet)

    def sendpacket(self, port, packet):
        DST_MAC = packet[0]
        if port == self.data_input1[DST_MAC]:
            Action = "Accepted"
        else:
            Action = "Rejected"
        print("Packet received")
        print("Details of the packet")
        print("----------------------")
        print("SRC_MAC : ", packet[1])
        print("DST_MAC : ", packet[0])
        print("Port No : ", port)
        print("Action  : ", Action)

    def broadcast(self, input_port, packet):
        for key in self.data_input1:
            current_port = self.data_input1[key]
            if current_port != input_port:
                self.sendpacket(current_port, packet)

    def check_(self, mac_int):
        if mac_int <= 255:
            return "The MAC address has the proper format"
        else:
            return "the MAC address does not have the proper format"


    def validate(self,packet):
        a = []
        for i in packet:
            if not (len(i) == 17):
                print("{} - does not have the proper length".format(i))
            else:
                print("{} - has the proper length".format(i))
            a = i.split("-")
            for f in a:
                try:
                    p = int(f, 16)
                    k = self.check_(p)
                except ValueError:
                    k = "Not a hex number. Improper MAC address format"
                    sys.exit()
            print(k)

