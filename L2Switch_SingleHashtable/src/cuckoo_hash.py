import hashlib


class cuckoo:
    TABLE_SIZE = 34000
    table1 = [None] * TABLE_SIZE
    Number_of_entries = 0
    count = 0

    def debug_stdout(self, sfunc):
        '''print(sfunc)'''

    debug = debug_stdout

    def hashfunction1(self, key):
        h = hashlib.md5(str.encode(key))
        self.debug("hash key 1 = " + str(int(h.hexdigest(), 16) % self.TABLE_SIZE))
        return int(h.hexdigest(), 16) % self.TABLE_SIZE


    def insert(self, key_value_pair, table_no, n):
        hash_value1 = self.hashfunction1(key_value_pair.getKey())
        if table_no == 1:
            if self.table1[hash_value1] is None:
                self.table1[hash_value1] = key_value_pair
                self.Number_of_entries += 1
            else:
                self.count += 1
                print("Collision met ", self.count, ", first at ",self.Number_of_entries)

    def find_port(self, key):
        hash_value1 = self.hashfunction1(key)

        if (self.table1[hash_value1] is not None) and (self.table1[hash_value1].getKey() == key):
            return self.table1[hash_value1].getValue()
        else:
            return None

    def search(self, key):
        hash_value1 = self.hashfunction1(key)

        if self.table1[hash_value1].getKey() == key:
            self.debug("incoming key =" + str(key) + ", found key = " + str(self.table1[hash_value1].getKey()))
            return True
        return False

    def delete(self, key):
        hash_value1 = self.hashfunction1(key)

        if (self.table1[hash_value1] is not None) and (self.table1[hash_value1].getKey() == key):
            self.table1[hash_value1] = None
        else:
            print("Entry not found to delete")

    '''
    def display(self):
        print("Table 1: ")
        for i in range(len(self.table1)):
            if self.table1[i] != None:
                print("[", self.table1[i].getKey(), ":", self.table1[i].getValue(), "]")
            else:
                print("[None]")
        print("Table 2: ")
        for i in range(len(self.table2)):
            if self.table2[i] != None:
                print("[", self.table2[i].getKey(), ":", self.table2[i].getValue(), "]")
            else:
                print("[None]")

    def split_add(self, mac):
        a = mac.split(":")
        sum1 = 0
        for i in a:
            sum1 += int(i, 16)
        return sum1
    '''

    class Pair:
        def __init__(self, mac, port):
            self.key = mac
            self.value = port

        def getKey(self):
            return self.key

        def getValue(self):
            return self.value




