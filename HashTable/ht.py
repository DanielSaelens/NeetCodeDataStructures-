class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.size = 0
        self.tombstone = object()

    # Search First
    # Decision Second
    # Insertion Last

    def insert(self, key: int, value: int) -> None:
        current_index = key % self.capacity
        starting_index = current_index
        first_tombstone_index = None

        while True:
            if self.table[current_index] is None:
                break
            elif self.table[current_index] is self.tombstone:
                if first_tombstone_index is None:
                    first_tombstone_index = current_index

            elif self.table[current_index][0] == key:
                self.table[current_index][1] = value
                return
            
            current_index = (current_index + 1) % self.capacity

            if current_index == starting_index:
                break
            
        
            
            


