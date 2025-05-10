class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None

        
class LinkedListStack:
    def __init__(self):
        self._peek: ListNode | None = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def push(self, val: int) -> None:
        node = ListNode(val)
        node.next = self._peek
        self._peek = node
        self._size += 1

    def pop(self) -> int:

        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peek.val

    def is_empty(self) -> bool:
        return self._size == 0

    def to_list(self) -> list[int]:
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next

        arr.reverse()
        return arr
        



if __name__ == '__main__':
    stack = LinkedListStack()
    stack.push(1)
    stack.push(2)
    stack.push(4)
    stack.push(3)
    print(stack.to_list())
    assert stack.pop() == 3
    assert stack.pop() == 4
    assert stack.peek() == 2

    print(stack.to_list())
