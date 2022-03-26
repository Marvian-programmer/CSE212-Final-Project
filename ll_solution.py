
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next # You needed to set self.head to self.head.next to get the next value.
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node  # The tail must become the new Node
        self.length += 1



my_linked_list = LinkedList(1)

my_linked_list.append(2) # You needed to to add just the three append methods with the values 234
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.print_list()                               
