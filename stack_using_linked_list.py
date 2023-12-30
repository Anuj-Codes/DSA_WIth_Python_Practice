class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    
class Stack:
    def __init__(self,start=None):
        self.start=start
        self.item_count=0
    
    def is_empty(self):
        return self.start is None
    
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1
    
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
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
print(f"popped item is {s1.pop()}")
print()
print(f"popped item is {s1.pop()}")
print()
print(s1.peek())
print()
print(s1.size())
      

        