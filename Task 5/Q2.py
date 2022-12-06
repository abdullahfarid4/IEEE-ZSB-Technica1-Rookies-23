class Stack:
    def __init__(self):
        self.__arr = []
        self.__top = -1

    def peek(self):
        return self.__arr[self.__top]

    def push(self, val):
        self.__top += 1
        self.__arr.append(val)

    def is_empty(self):
        return self.__top == -1

    def pop(self):
        if self.is_empty():
            return "Empty Stack"
        else:
            ele = self.__arr[self.__top]
            self.__top -= 1
            return ele


s = Stack()
st = input()
for i in range(len(st)):
    if st[i] in ['(', '[', '{']:
        s.push(st[i])
    if ord(st[i]) == (ord(s.peek()) + 1) or ord(st[i]) == (ord(s.peek()) + 2):
        s.pop()

if s.is_empty():
    print("true")
else:
    print("false")
