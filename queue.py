class Queue(object):
    def __init__(self, size = 8):
        self.queue = []
        self.size = size
        self.front = 0 
        self.rear = -1

    def is_full(self):
        return True if self.rear == self.size - 1 else False

    def is_empty(self):
        return True if self.rear == -1 else False

    def push(self, data):
        if self.is_full():
            raise Exception("QueueOverFlow")
        self.queue.append(data)
        self.rear += 1

    def pop(self):
        if self.is_empty():
            raise Exception("QueueIsEmpty")
        self.rear -= 1
        return self.queue.pop(self.front)
    
    def first(self):
        return self.queue[self.front]

    def last(self):
        return self.queue[self.rear]

    def show(self):
        print self.queue

def test_queue(data):
    queue = Queue(data)
    queue.show()

    for i in range(data):
        queue.push(i)
    queue.show()

    try:
        queue.push(data)
    except Exception, e:
        print e
    else:
        queue.show()

    while not queue.is_empty():
        queue.pop()
    queue.show()

    try:
        queue.pop()
    except Exception, e:
        print e
    else:
        queue.show()

if __name__ == '__main__':
    test_queue(8)


