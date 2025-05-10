class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 在头部插入节点
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 在尾部插入节点
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # 在指定位置插入节点
    def insert_at_position(self, position, data):
        if position < 0:
            raise ValueError("Position must be non-negative")
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                break
            current = current.next
        if current is None:
            raise IndexError("Position out of bounds")
        new_node.next = current.next
        current.next = new_node

    # 按值删除节点
    def delete_by_value(self, value):
        current = self.head
        prev = None
        while current is not None:
            if current.data == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return  # 仅删除第一个匹配的节点
            prev = current
            current = current.next
        raise ValueError("Value not found in the list")

    # 按位置删除节点
    def delete_by_position(self, position):
        if position < 0:
            raise ValueError("Position must be non-negative")
        if self.head is None:
            raise IndexError("List is empty")
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        current_pos = 0
        while current is not None and current_pos < position:
            prev = current
            current = current.next
            current_pos += 1
        if current is None:
            raise IndexError("Position out of bounds")
        prev.next = current.next

    # 查找值是否存在
    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    # 获取链表长度
    def get_length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # 转换为列表（用于测试）
    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    # 反转链表
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 字符串表示
    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) + " -> None"


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(1)
    ll.insert_at_head(2)
    print("After inserting 1 and 2 at head:", ll.to_list())  # [2, 1]

    ll.insert_at_tail(3)
    print("After inserting 3 at tail:", ll.to_list())        # [2, 1, 3]

    ll.insert_at_position(1, 4)
    print("After inserting 4 at position 1:", ll.to_list()) # [2, 4, 1, 3]

    ll.delete_by_value(4)
    print("After deleting value 4:", ll.to_list())           # [2, 1, 3]

    ll.delete_by_position(0)
    print("After deleting position 0:", ll.to_list())        # [1, 3]

    ll.reverse()
    print("After reversing:", ll.to_list())                  # [3, 1]

    print("Search for 3:", ll.search(3))                     # True
    print("Length of list:", ll.get_length())               # 2
