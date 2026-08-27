class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class Dequeu:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if self.head is None and self.tail is None:
            return True

        return False

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def pop(self) -> int:
        if self.tail is None:
            return -1
        
        elif self.tail is self.head:
            og_value = self.tail.value
            self.tail = None
            self.head = None
            return og_value
        else:
            og_value = self.tail.value
            self.tail = self.tail.previous
            self.tail.next = None

        return og_value

    def popleft(self) -> int:
        if self.head is None:
            return -1
        
        elif self.head is self.tail:
            og_value = self.head.value
            self.head = None
            self.tail = None
            return og_value
        else:
            og_value = self.head.value
            self.head = self.head.next
            self.head.previous = None

        return og_value

    def print_DEQ(self) -> None:
        current = self.head

        if current is None:
            print("head -> None <- tail")
            return

        print("head -> ", end="")

        while current is not None:
            print(current.value, end="")

            if current.next is not None:
                print(" <-> ", end="")

            current = current.next

        print(" <- tail")


if __name__ == "__main__":
    dq = Dequeu()
    dq.append(5)
    dq.appendleft(3)
    dq.append(4)
    
    dq.print_DEQ()

    assert dq.head.value == 3
    assert dq.head.previous is None
    assert dq.head.next.value == 5
    assert dq.tail.value == 4

    dq.popleft()
    dq.pop()

    dq.print_DEQ()

    assert dq.head.value == 5
    assert dq.head.next is None
    assert dq.head.previous is None

    dq.pop()
    dq.print_DEQ()

    assert dq.isEmpty() is True

   