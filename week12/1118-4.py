class Stack:
    def __init__(selfself):
        self.items = list() # self.items = []

    def push(selfself, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

subjects = Stack()
subjects.push("웹프로그래밍")
subjects.push("자료구조")
print(subjects.pop())
print(subjects)