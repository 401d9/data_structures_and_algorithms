from node import Node
from typing import Any


class LinkedList(object):
    def __init__(self):
        self.head = None
        self._length = 0

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length : {self._length}'

    def __len__(self):
        return self._length

    # def __iter__(self):
    #     pass
    #
    # def __next__(self):
    #     pass

    def append(self, val: Any) -> Node:

        if self.head is None:
            self.head = Node(val)
            self._length += 1
        else:
            current = self.head

            while current._next is not None:
                print('made it here')
                current = current._next

            new_node = Node(val)

            current._next = new_node
            self._length += 1

    # def includes(self, val: str, data: int) -> bool:
    def includes(self, val: Any) -> bool:
        pass

if __name__ == '__main__':

    ll = LinkedList()
    ll.append(23)
    ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # return ll

    print(ll.head._next.val )
