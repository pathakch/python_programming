class HashTable:
    def __init__(self, size = 7):
        self. data_map = [None] * size

    def hash(self, key):
        hash_val = 0
        for letter in key:
            hash_val = (hash_val + ord(letter) * 23) % len(self.data_map)
        return hash_val
    
    def print_hash_table(self):
        for key, value in enumerate(self.data_map):
            print(f"{key} : {value}")

    def set_item(self, key, value):
        index = self.hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.hash(key)
        if self.data_map[index] != None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                 return self.data_map[index][i][1]
        else:
            return f"key '{key}' does not exist in the table"
        
    def keys(self):
        keys = []
        for i in range (len(self.data_map)):
            if self.data_map[i] != None:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        return keys
            






    # def set_item(self, )


a = HashTable()
# print(a.hash('A'))
# a.set_item('bolts',20)
# a.set_item('B',30)
# a.set_item('washers',40)
# a.set_item("lumber",100)
# a.print_hash_table()
# print(a.get_item('bolts'))
# print(a.keys())
print(type(a))






