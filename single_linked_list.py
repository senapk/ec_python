from __future__ import annotations

class Node:
    def __init__(self, data: int, next: Node | None = None) -> None:
        self.data = data
        self.next = next


class SimpleLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
    
    def append(self, data: int) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current: Node | None = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self) -> None:
        current: Node | None = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def remove(self, data: int) -> bool:
        current: Node | None = self.head
        previous: Node | None = None
        
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def search(self, data: int) -> bool:
        current: Node | None = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


my_list = SimpleLinkedList()
for i in range(10):
    my_list.append(i)
my_list.display()



