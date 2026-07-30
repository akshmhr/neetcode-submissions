from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.dq = deque(maxlen = capacity)

    def get(self, key: int) -> int:
        if key in self.dq:
            self.dq.remove(key)
            self.dq.append(key)
        return self.hashMap.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap[key] = value
            self.dq.remove(key)
            self.dq.append(key)
            return

        elif len(self.hashMap) < self.capacity:
            self.hashMap[key] = value
            self.dq.append(key)
    
        else:
            removeKey = self.dq.popleft()
            self.hashMap.pop(removeKey, -1)
            self.hashMap[key] = value
            self.dq.append(key)