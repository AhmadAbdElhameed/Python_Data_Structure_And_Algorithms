class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = value
            self.tail = value
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def pop(self):
        if self.length == 0:
            return None
    
        temp = self.head
        pre = self.head
    
        while (temp.next):
            pre = temp
            temp = temp.next
    
        self.tail = pre
        self.tail.next = None
    
    
    
        
my_linked_list = LinkedList(5);

my_linked_list.append(11)
my_linked_list.append(21)
my_linked_list.append(31)
my_linked_list.append(41)


my_linked_list.print_list()

my_linked_list.pop()

my_linked_list.print_list()
