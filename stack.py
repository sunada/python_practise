#!/bin/python

class Stack(object):
    def __init__(self, size = 8):
        self.stack = []
        self.size = size
        self.top = -1

    def set_size(self, size):
        if self.top >= size:
            raise Exception("StackWillOverFlow")
        self.size = size
    
    def isFull(self):
        return True if self.size == self.top + 1 else False

    def isEmpty(self):
        return True if self.top == -1 else False

    def push(self, data):
        if self.isFull():
            raise Exception("StackOverFlow")
            return
        self.stack.append(data)
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("StackIsEmpty")
            return
        self.top -= 1
        return self.stack.pop()
    
    def top(self):
        if self.isEmpty():
            raise Exception("StackIsEmpty")
            return -1
        return self.stack[self.top]

    def show(self):
        print self.stack

def test_stack(data):
    stack = Stack(data)
    stack.show()

    for i in range(data):
        stack.push(i)
    stack.show()

    try:
        stack.push(data)
    except Exception, e:
        print e
    else:
        stack.show()

    try:
        stack.set_size(data/2)
    except Exception, e:
        print e
    else:
        stack.show()

    while not stack.isEmpty():
        stack.pop()
    stack.show()

    for i in range(data/2):
        stack.push(i)
    stack.show()

    try:
        stack.push(data)
    except Exception, e:
        print e
    else:
        stack.show()

    try:
        stack.set_size(data -1)
    except Exception, e:
        print e
    else:
        stack.show()


if __name__ == '__main__':
    test_stack(8)

    



            

