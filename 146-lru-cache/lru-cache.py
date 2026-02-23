class Node:
    def __init__(self, value , key):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nm = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head



    def get(self, key: int) -> int:
        if key not in self.nm:
            return -1
        node = self.nm[key]
        self._remove(node)
        self._add(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.nm:
            old = self.nm[key]
            self._remove(old)
        node  = Node(value, key)
        self.nm[key] = node
        self._add(node)
        if len(self.nm) > self.capacity:
            nodetodel = self.head.next
            self._remove(nodetodel)
            del self.nm[nodetodel.key]
    

    def _add(self, node):
        end = self.tail.prev
        end.next = node
        node.prev = end
        node.next = self.tail
        self.tail.prev = node

    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)