class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def length(head):
    current = head
    count = 0
    while current is not None:
        count += 1
        current = current.next
    return count

def count(head, value):
    current = head
    occurrences = 0
    while current is not None:
        if current.data == value:
            occurrences += 1
        current = current.next
    return occurrences

list1 = Node(1, Node(2, Node(3)))
result_length = length(list1)
print(result_length)

result_count = count(list1, 1)
print(result_count)

list2 = Node(1, Node(1, Node(1, Node(2, Node(2, Node(2, Node(2, Node(3, Node(3)))))))))
result_count_2 = count(list2, 2)
print(result_count_2)