class MyHashSet:

    def __init__(self):
        self.d = [[] for _ in range(10000)]
        

    def add(self, key: int) -> None:
        index = key % len(self.d)
        if not self.d[index]:
            self.d[index].append(key)
        

    def remove(self, key: int) -> None:
        index = key % len(self.d)
        if self.d[index]:
            self.d[index].pop()
            

    def contains(self, key: int) -> bool:
        index = key%len(self.d)
        if self.d[index]:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)