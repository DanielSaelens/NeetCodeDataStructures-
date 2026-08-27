class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity

    def get(self, i: int):
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            new_capacity = self.capacity * 2
            new_array = [None] * new_capacity

            for i in range(self.size):
                new_array[i] = self.arr[i]

            self.arr = new_array
            self.capacity = new_capacity

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        last_pos = self.size - 1
        value = self.arr[last_pos]
        self.arr[last_pos] = None
        self.size -= 1
        return value

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.arr[i]

        self.arr = new_array
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

# Thought bubble, is there a way to make a separate class that can inherit from here.


if __name__ == "__main__":

    da1 = DynamicArray(2)

    assert da1.capacity == 2
    assert da1.getSize() == 0

    da1.pushback(10)

    assert da1.capacity == 2
    assert da1.getSize() == 1
    assert da1.get(0) == 10

    da1.pushback(20)
    assert da1.getSize() == 2
    assert da1.capacity == 2
    assert da1.get(1) == 20

    da1.resize()

    da1.pushback(30)
    assert da1.getSize() == 3
    assert da1.capacity == 4
    assert da1.get(2) == 30
    da1.set(1, 99)
    assert da1.get(1) == 99
    assert da1.getSize() == 3
    assert da1.capacity == 4

    da1.popback()

    assert da1.getSize() == 2
    assert da1.capacity == 4
    assert da1.get(0) == 10
    assert da1.get(1) == 99

    assert da1.get(0) == 10
    assert da1.get(1) == 99

    assert da1.popback() == 99
    assert da1.getSize() == 1
    assert da1.popback() == 10
    assert da1.getSize() == 0
