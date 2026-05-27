class HashTable:
    def __init__(self, size):
        self.data_map = [None] * size

    def _hash(self, key):
        hash = 0
        for letter in key:
            hash = (hash + (ord(letter)*23))% len(self.data_map)
        return hash

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i} : {val}")

    def get_item(self, key):
        index = self._hash(key)
        for i in range(len(self.data_map[index])):
            if (self.data_map[index])[i][0] == key:
                return self.data_map[index][i][1]
        return False
    
    def keys(self):
        keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        return keys
            

ht = HashTable(7)
ht.set_item('Hammer', 20)
ht.set_item('AbC', 30)
ht.set_item('nails', 40)
ht.set_item('bolts', 50)
ht.set_item('washers', 60)

ht.print_table()
print("get Item : ",ht.get_item('Hammer'))
print("Keys : ", ht.keys())


# print(ht._hash('washers'))