# String Hashes
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t['jide'] = 1000
print(t['qudus'])
print(t.arr)
print(t['jide'])


# Hashing Involving nums
class Hashing:
    def __init__(self):
        self.arr = [None] * 10

    def hash_funct(self, key):
        return key % len(self.arr)

    def insert(self, key, value):
        hash_key = self.hash_funct(key)
        self.arr[hash_key] = value


h = Hashing()
h.insert(4, 9)
print(h.arr)


# Dictionary

dico = {}
dico["yes"] ="as"
try:
    print(dico[5])
except KeyError:
    print(dico["yes"])