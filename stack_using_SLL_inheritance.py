from linked_list import *
class Stack(Sll):
    def __init__(self):
        super().__init__()
        self.item_count=0
    
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1
    
    def pop(self):
        if not self.is_empty():
            self.item_count-=1
            self.delete_first()
            
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty")
    
    def size(self):
        if not self.is_empty():
            return self.item_count
        else:
            raise IndexError("Stack is empty")
        


s1=Stack()
print(s1.is_empty())
s1.push(10)
s1.push(20)
s1.push(30)
print()
print(s1.size())
print()
s1.pop()
s1.pop()
print(s1.peek())
print()
print(s1.size())
        