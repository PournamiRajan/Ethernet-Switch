import hashlib


class cuckoo:
    TABLE_SIZE = 16000
    table1 = [[None for i in range(2)] for j in range(TABLE_SIZE)]
    table2 = [[None for i in range(2)] for j in range(TABLE_SIZE)]
    MAX_ITERATION = 100
    Number_of_entries = 0
    count = 0
    success = False
    second = False

    def debug_stdout(self, sfunc):
        '''print(sfunc)'''

    debug = debug_stdout

    def hashfunction1(self, key):
        h = hashlib.md5(str.encode(key))
        self.debug("hash key 1 = " + str(int(h.hexdigest(), 16) % self.TABLE_SIZE))
        return int(h.hexdigest(), 16) % self.TABLE_SIZE

    def hashfunction2(self, key):
        h = hashlib.sha256(str.encode(key))
        self.debug("hash key 2 = " + str(int(h.hexdigest(), 16) % self.TABLE_SIZE))
        return int(h.hexdigest(), 16) % self.TABLE_SIZE

    def insert(self, key_value_pair, table_no, n):
        if n == self.MAX_ITERATION:
            self.count += 1
            if self.count <= 10:
                print("Reached MAX_ITERATION at", self.Number_of_entries)
                print("Percentage load = ", self.Number_of_entries*100/(self.TABLE_SIZE*4))
                #print(self.table1)
                #print(self.table2)
            return



        """if n == self.MAX_ITERATION:
            if self.second is True:
                self.count += 1
                if self.count <= 10:
                    print("Reached MAX_ITERATION at", self.Number_of_entries)
                    print("Percentage load = ", self.Number_of_entries*100/(self.TABLE_SIZE*4))
                #print(self.table1)
                #print(self.table2)
            return
        """
        n = n + 1
        hash_value1 = self.hashfunction1(key_value_pair.getKey())
        hash_value2 = self.hashfunction2(key_value_pair.getKey())
        if table_no == 1:
            if self.table1[hash_value1][0] is None:
                self.table1[hash_value1][0] = key_value_pair
                self.debug("inserted key : " + str(key_value_pair.getKey()))
                #self.Number_of_entries += 1
                self.success = True
                #print("1", self.table1)
            elif self.table1[hash_value1][1] is None:
                self.table1[hash_value1][1] = key_value_pair
                self.debug("inserted key : " + str(key_value_pair.getKey()))
                #self.Number_of_entries += 1
                self.success = True
                #print("1", self.table1)
            else:
                pair1 = self.table1[hash_value1][1]
                self.table1[hash_value1][1] = key_value_pair
                self.debug("inserted key : " + str(key_value_pair.getKey()))
                self.insert(pair1, 2, n)
                if self.table1[hash_value1][0] is not None:
                    pair1 = self.table1[hash_value1][0]
                    self.table1[hash_value1][0] = None
                    self.debug("inserted key : " + str(key_value_pair.getKey()))
                    self.insert(pair1, 2, n)

                """if self.success is False and self.second is False:
                    #print(" inside if 1")
                    self.second = True
                    self.table1[hash_value1][1] = pair1
                    pair1 = self.table1[hash_value1][0]
                    self.table1[hash_value1][0] = key_value_pair
                    self.debug("inserted key : " + str(key_value_pair.getKey()))
                    self.insert(pair1, 2, 1)
                """
        elif table_no == 2:
            if self.table2[hash_value2][0] is None:
                self.table2[hash_value2][0] = key_value_pair
                #self.Number_of_entries += 1
                self.success = True
                #print("2", self.table2)
            elif self.table2[hash_value2][1] is None:
                self.table2[hash_value2][1] = key_value_pair
                #self.Number_of_entries += 1
                self.success = True
                #print("2",self.table2)
            else:
                pair2 = self.table2[hash_value2][1]
                self.table2[hash_value2][1] = key_value_pair
                self.insert(pair2, 1, n)
                if self.table2[hash_value2][0] is not None:
                    pair2 = self.table2[hash_value2][0]
                    self.table2[hash_value2][0] = None
                    self.insert(pair2, 1, n)
                """if self.success is False and self.second is False:
                    #print(" inside if 2")
                    self.second = True
                    self.table2[hash_value2][1] = pair2
                    pair2 = self.table2[hash_value2][0]
                    self.table2[hash_value2][0] = key_value_pair
                    self.insert(pair2, 1, 1)
                """

    def find_port(self, key):
        hash_value1 = self.hashfunction1(key)
        hash_value2 = self.hashfunction2(key)

        if (self.table1[hash_value1][0] is not None) and (self.table1[hash_value1][0].getKey() == key):
            return self.table1[hash_value1][0].getValue()
        elif (self.table1[hash_value1][1] is not None) and (self.table1[hash_value1][1].getKey() == key):
            return self.table1[hash_value1][1].getValue()
        elif (self.table2[hash_value2][0] is not None) and (self.table2[hash_value2][0].getKey() == key):
            return self.table2[hash_value2][0].getValue()
        elif (self.table2[hash_value2][1] is not None) and (self.table2[hash_value2][1].getKey() == key):
            return self.table2[hash_value2][1].getValue()
        else:
            return None

    def search(self, key):
        hash_value1 = self.hashfunction1(key)
        hash_value2 = self.hashfunction2(key)

        if self.table1[hash_value1][0].getKey() == key:
            self.debug("incoming key =" + str(key) + ", found key = " + str(self.table1[hash_value1][0].getKey()))
            return True
        elif self.table1[hash_value1][1].getKey() == key:
            self.debug("incoming key =" + str(key) + ", found key = " + str(self.table1[hash_value1][1].getKey()))
            return True
        elif self.table2[hash_value2][0].getKey() == key:
            self.debug("incoming key =" + str(key) + ", found key = " + str(self.table1[hash_value1][0].getKey()))
            return True
        elif self.table2[hash_value2][1].getKey() == key:
            self.debug("incoming key =" + str(key) + ", found key = " + str(self.table1[hash_value1][1].getKey()))
            return True
        self.debug("incoming key =" + str(key) + ",  key not found ")
        return False

    def delete(self, key):
        hash_value1 = self.hashfunction1(key)
        hash_value2 = self.hashfunction2(key)

        if (self.table1[hash_value1][0] is not None) and (self.table1[hash_value1][0].getKey() == key):
            self.table1[hash_value1][0] = None
        elif (self.table1[hash_value1][1] is not None) and (self.table1[hash_value1][1].getKey() == key):
            self.table1[hash_value1][1] = None
        elif (self.table2[hash_value2][0] is not None) and (self.table2[hash_value2][0].getKey() == key):
            self.table2[hash_value2][0] = None
        elif (self.table2[hash_value2][1] is not None) and (self.table2[hash_value2][1].getKey() == key):
            self.table2[hash_value2][1] = None
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




