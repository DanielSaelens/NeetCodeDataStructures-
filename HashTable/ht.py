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

        if first_tombstone_index is not None:
            current_index = first_tombstone_index

        elif self.table[current_index] is None:
            pass

        elif self.tombstone is None and self.table[current_index] is not None:
            self.resize()
            self.insert(key, value)
            return

        self.table[current_index] = [key, value]
        self.size += 1
        load_factor = self.size / self.capacity

        if load_factor >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        current_index = key % self.capacity
        starting_index = current_index

        while True:

            if self.table[current_index] is None:
                return -1
            elif self.table[current_index] is self.tombstone:
                pass

            elif self.table[current_index][0] == key:
                return self.table[current_index][1]

            current_index = (current_index + 1) % self.capacity

            if current_index == starting_index:
                return -1

    def remove(self, key: int) -> bool:
        current_index = key % self.capacity
        starting_index = current_index

        while True:
            if self.table[current_index] is None:
                return False

            elif self.table[current_index] is self.tombstone:
                return False

            elif self.table[current_index][0] == key:
                self.table[current_index] = self.tombstone
                self.size -= 1
                return True

            current_index = (current_index + 1) % self.capacity

            if current_index == starting_index:
                return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        double_cap = self.capacity * 2
        new_table = [None] * double_cap

        for slot in self.table:
            if slot is None:
                pass
            elif slot is self.tombstone:
                pass
       
            else:
                key, value = slot
                current_index = key % double_cap
                starting_index = current_index

        while True:
            if new_table[current_index] is None:
                break

            current_index = (current_index + 1) % double_cap

            if current_index == starting_index:
                break
        new_table[current_index] = key, value

        self.table = new_table
        self.capacity = double_cap

    def displayHT(self) -> None:
        display = []
        for slot in self.table:
            if slot is self.tombstone:
                display.append("TOMBSTONE")
            else:
                display.append(slot)

        print(display)


if __name__ == "__main__":

    ht = HashTable(5)
    ht.insert(3, 100)
    ht.insert(4, 100)
    ht.displayHT()
   
