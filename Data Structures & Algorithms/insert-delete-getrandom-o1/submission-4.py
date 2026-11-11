import random

class RandomizedSet:

    def __init__(self):
        self.values = {}
        self.indices = {}
        self.index = 0


        

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        else:
            self.values[val] = self.index
            self.indices[self.index] = val
            
            self.index += 1
            return True

        

    def remove(self, val: int) -> bool:
        if val in self.values:
            #get index
            i = self.values[val]

            # Get last element
            last_index = self.index - 1
            last_val = self.indices[last_index]

            # Move last element into removed element's position
            self.indices[i] = last_val
            self.values[last_val] = i

            self.indices.pop(last_index) # remove from indices
            self.values.pop(val) # remove from values

            self.index -= 1
            return True
        else:
            return False

        

    def getRandom(self) -> int:
        r = random.randint(0, self.index-1)


        return self.indices[r]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()