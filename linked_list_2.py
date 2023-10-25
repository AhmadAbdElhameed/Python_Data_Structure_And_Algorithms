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
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        
        if(self.length == 0):
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None    
        return temp
            
            
    def get(self,index):
        if(index < 0 or index >= self.length):
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
            
            
    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if (index < 0 or index > self.length):
            return False
        if index == 0:
            return self.prepend(value);
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self,index):
        if (index < 0 or index > self.length):
            return None
        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    
my_linked_list = LinkedList(5);
my_linked_list.append(9)
my_linked_list.append(20)
my_linked_list.append(30)

my_linked_list.insert(2,1500)


my_linked_list.print_list()

my_linked_list.remove(2)
my_linked_list.print_list()





