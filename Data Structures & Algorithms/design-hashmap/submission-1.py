class MyHashMap:

    def __init__(self):
        self.d = [[] for _ in range(10000)]

        

    def put(self, key: int, value: int) -> None:
        index = key%len(self.d)
        for  i, (k,v) in enumerate(self.d[index]):
            if key == k:
                self.d[index][i] = (key,value)
                return
        self.d[index].append((key,value))
        

    def get(self, key: int) -> int:
        index = key%len(self.d)
        for k,v in self.d[index]:
            if key == k:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        index = key%len(self.d)
        for  i, (k,v) in enumerate(self.d[index]):
            if k == key:
                self.d[index].pop(i)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)