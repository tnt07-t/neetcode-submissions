#doubly linked list + hash map -> track recency + value

class Node:
    def __init__(self, key, val):
        self.key, self.val = key,val
        self.prev = self.next = None

class LRUCache:


    def __init__(self, capacity: int):
        self.cache = {} #hash key to node
        self.capacity = capacity
        #set up node
        self.left, self.right = Node(0,0), Node(0,0)# LRU, MRU
        self.left.next, self.right.prev = self.right, self.left
        self.curr = 0

    def insert(self,node):
        node.prev, node.next = self.right.prev, self.right

        self.right.prev.next = node
        self.right.prev = node

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            self.remove(node)#remove LRU
            self.insert(node)#update MRU
        
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        new_node = Node(key,value)
        if key in self.cache: #update val
            node = self.cache[key]
            self.remove(node)
            self.insert(new_node)

            #update cache
            self.cache[key] = new_node

        else:
            #update curr
            if self.curr < self.capacity:
                self.curr += 1

            #remove LRU
            else:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]   #clean up evicted key

            #update MRU + add key-value
            self.insert(new_node)
            self.cache[key] = new_node
