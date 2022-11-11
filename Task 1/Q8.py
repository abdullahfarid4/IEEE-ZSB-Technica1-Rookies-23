class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, data):
        new_n = Node(data)
        self.size += 1
        new_n.next = self.head
        self.head = new_n
        return

    def append(self, data):
        new_n = Node(data)
        self.size += 1
        if not self.head:
            self.head = new_n
            return
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_n

    def insert(self, data, prev_node):
        new_n = Node(data)
        if not prev_node:
            return "Previous Node can't be None"
        else:
            self.size += 1
            new_n.next = prev_node.next
            prev_node.next = new_n
            return f'{data} has been inserted'

    def print(self):
        node = self.head
        while node is not None:
            print(node.data, end='->')
            node = node.next
        print()

    def length(self):
        return f'size = {self.size}'

    def search(self, element):
        node = self.head
        while node is not None:
            if node.data == element:
                return "Element is found"
            node = node.next
        return "Not Found"

    def remove(self, element):
        node = self.head
        prev_node = None
        while node is not None:
            if node.data == element:
                if not prev_node:
                    self.head = node.next
                    self.size -= 1
                    return f'{element} is removed'


