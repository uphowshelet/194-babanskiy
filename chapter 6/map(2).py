class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def map_linked_list(head, mapping_function):
    new_head = None
    current_new = None
    current_old = head
    while current_old is not None:
        new_node = Node(mapping_function(current_old.data))
        if new_head is None:
            new_head = new_node
            current_new = new_node
        else:
            current_new.next = new_node
            current_new = new_node
        current_old = current_old.next
    return new_head

original_list = Node(1, Node(2, Node(3)))

def mapping_function(x):
    return x * 2

mapped_list = map_linked_list(original_list, mapping_function)

current = mapped_list
while current:
    print(current.data, end=" -> ")
    current = current.next