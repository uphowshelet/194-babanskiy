class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def get_nth(head, index):
    if head is None:
        raise ValueError("Неверный индекс или пустой список")

    current = head
    current_index = 0

    while current is not None:
        if current_index == index:
            return current
        current = current.next
        current_index += 1

    raise ValueError("Индекс вне диапазона")

list1 = Node(1, Node(2, Node(3)))
result1 = get_nth(list1, 0)
print(result1.data)
list2 = Node(1, Node(2, Node(3, None)))
result2 = get_nth(list2, 2)
print(result2.data)
try:
    get_nth(list2, 5)
except ValueError as e:
    print(e)
try:
    get_nth(None, 0)
except ValueError as e:
    print(e)