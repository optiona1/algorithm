class ArrayStack:
    def __init__(self):
        self._val = []

    def size(self) -> int:
        return len(self._val)

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, val: int):
        self._val.append(val)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._val.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._val[-1]

    def to_list(self):
        return self._val


if __name__ == '__main__':
    stack = ArrayStack()
    stack.push(5)
    stack.push(5)
    stack.push(4)
    stack.push(5)
    print(stack.to_list())
    assert stack.pop() == 5
    assert stack.pop() == 4
    print(stack.to_list())
