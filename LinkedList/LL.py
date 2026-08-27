from typing import List


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                # print(current.value)
                return current.value
            count += 1
            current = current.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        current = self.head
        if self.head is None:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove(self, index) -> bool:
        counter = 0
        current = self.head
        if self.head is None:
            return False
        elif index == 0:
            self.head = self.head.next
            return True
        else:
            while counter < index - 1 and current.next is not None:
                current = current.next
                counter += 1
            if current.next is not None:
                current.next = current.next.next
                return True
            else:
                return False

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        # print(values)
        return values

    def print_LL(self) -> None:
        current = self.head
        while current is not None:
            print(current.value,  end=" -> ",)
            current = current.next
        print(None)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertHead(7)
    ll.insertHead(6)
    ll.insertHead(5)
    ll.insertTail("SuperMan")
    ll.print_LL()
    ll.getValues()
    print(ll.remove(0))
    ll.getValues()
    ll.print_LL()

    assert ll.get(0) == 6
    assert ll.get(1) == 7
    assert ll.get(2) == "SuperMan"
    assert ll.get(3) is -1
    assert ll.getValues() == [6, 7, "SuperMan"]
    assert ll.remove(0) is True
