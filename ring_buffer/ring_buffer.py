class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0 

    def append(self, item):
        # when the storage equals desired length...
        if (len(self.storage) == self.capacity):
            self.storage[self.index] = item
            self.index += 1
            if (self.index >= self.capacity):
                self.index = 0
        # #otherwise
        else:
            self.storage.append(item)

        #missing one case

    def get(self):
        if len(self.storage) != self.capacity:
            new_storage = [i for i in self.storage if i is not None]
        else: 
            return self.storage