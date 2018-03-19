import sys
class switch:

    FWD_TABLE = {}
    data_input1={}
    ports = ['1','2','3','4']
    file = open("mac_to_port.txt", "r")
    for line in file:
        a = line.split("port")
        data_input1[a[0].strip()]=a[1][0]
    file.close()

    def learn(self, SRC_MAC):
        if not SRC_MAC in self.FWD_TABLE:
            self.FWD_TABLE[SRC_MAC] = self.data_input1[SRC_MAC]

    def forward(self, packet):
        SRC_MAC = packet[1]
        DST_MAC = packet[0]
        self.learn(SRC_MAC)
        if DST_MAC in self.FWD_TABLE:
            port = self.FWD_TABLE[DST_MAC]
            input_port = self.data_input1[SRC_MAC]
            if port == input_port:
                text_file = open("write it.text", "a")
                text_file.write("\n")
                text_file.write(packet[1])
                text_file.write("\t\t")
                text_file.write(packet[0])
                text_file.write("\t\t\t\t\t ")
                text_file.write(" Suppressed : Same port number")
                text_file.close()
                return
            self.sendpacket(port, packet)
        else:
            port = self.data_input1[DST_MAC]
            input_port = self.data_input1[SRC_MAC]
            if port == input_port:
                text_file = open("write it.text", "a")
                text_file.write("\n")
                text_file.write(packet[1])
                text_file.write("\t\t")
                text_file.write(packet[0])
                text_file.write("\t\t\t\t\t")
                text_file.write("Suppressed : Same port number")
                text_file.close()
                return
            self.broadcast(input_port, packet)

    def sendpacket(self, port, packet):
        DST_MAC = packet[0]
        #print("inside fn")
        if port == self.data_input1[DST_MAC]:
            Action = "Accepted"
            #print("acc")
        else:
            Action = "Rejected(Broadcast packet)"
            #print("rej")
        text_file = open("write it.text", "a")
        text_file.write("\n")
        text_file.write(packet[1])
        text_file.write("\t\t")
        text_file.write(packet[0])
        text_file.write("\t\t")
        text_file.write(port)
        text_file.write("\t\t\t")
        text_file.write(Action)
        text_file.close()


    def broadcast(self, input_port, packet):
        for p in self.ports:
            if p != input_port:
                self.sendpacket(p, packet)


    def validate(self, packet):
        SRC_MAC = packet[1]
        DST_MAC = packet[0]
        if SRC_MAC not in self.data_input1:
            text_file = open("write it.text", "a")
            text_file.write("\n")
            text_file.write(SRC_MAC)
            text_file.write("\t\t\t\t\t")
            text_file.write("\t\t\t\t\t\t")
            text_file.write("Invalid Source MAC entry found")
            text_file.close()
            sys.exit()
        if DST_MAC not in self.data_input1:
            text_file = open("write it.text", "a")
            text_file.write("\n")
            text_file.write("\t\t\t\t\t\t")
            text_file.write(DST_MAC)
            text_file.write("\t\t\t\t\t")
            text_file.write("Invalid Destination MAC entry found")
            text_file.close()
            sys.exit()
