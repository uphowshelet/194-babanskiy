class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def filter_linked_list(head, predicate_function):
    new_head = None
    current_new = None
    current_old = head
    while current_old is not None:
        if predicate_function(current_old.data):
            new_node = Node(current_old.data)
            if new_head is None:
                new_head = new_node
                current_new = new_node
            else:
                current_new.next = new_node
                current_new = new_node
        current_old = current_old.next
    return new_head

original_list = Node(1, Node(2, Node(3)))

def predicate_function(x):
    return x >= 2

filtered_list = filter_linked_list(original_list, predicate_function)

current = filtered_list
while current:
    print(current.data, end=" -> ")
    current = current.next