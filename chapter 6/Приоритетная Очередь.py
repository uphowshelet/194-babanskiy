class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item, priority):
        self.items.append((item, priority))

    def pop(self):
        if self.is_empty():
            raise IndexError("Пустая очередь")
        self.items.sort()
        return self.items.pop(0)[1]

    def peek(self):
        if self.is_empty():
            raise IndexError("Пустая очередь")
        self.items.sort()
        return self.items[0][1]

    def size(self):
        return len(self.items)


pq = PriorityQueue()

pq.push(1, priority=2)
pq.push(2, priority=5)
pq.push(3, priority=1)

print("Первый элемент с наивысшим приоритетом:", pq.peek())

while not pq.is_empty():
    print("Обработка:", pq.pop())