from switch import switch
import sys

# data_input2 --> Host to Mac address mapping
data_input2 = {'A': '20-55-24-BD-4D-4C', 'B': '10-75-D3-79-22-CF', 'C': '5F-CA-A5-88-BC-38', 'D': '6B-26-7B-C4-51-C7'}
while True:

    SRC_HOST = input("Enter the sender (A/B/C/D) :")
    if SRC_HOST not in ("A", "B", "C", "D"):
        print("{} - Not a valid source port number".format(SRC_HOST))
        sys.exit()

    DST_HOST = input("Enter the receiver (A/B/C/D) :")
    if DST_HOST not in ("A", "B", "C", "D"):
        print("{} - Not a valid destination port number".format(DST_HOST))
        sys.exit()

    if DST_HOST == SRC_HOST:
        print("Destination and source cannot be same. Try Again !! ")
        sys.exit()

    SRC_MAC = data_input2[SRC_HOST]
    DST_MAC = data_input2[DST_HOST]

    # print("SRC MAC : {} \n DST MAC : {}".format(SRC_MAC,DST_MAC))

    s = switch()
    packet = [DST_MAC, SRC_MAC]
    s.validate(packet)
    s.forward(packet)