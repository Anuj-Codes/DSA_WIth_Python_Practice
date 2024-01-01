class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None
        self.item_count=0
    
    def is_empty(self):
        return self.rear==None
    
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1   
    
    def dequeue(self):
        if not self.is_empty():
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
            self.item_count-=1
        else:
            return IndexError("queue is underflow(empty)")
        
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            return IndexError("queue is underflow(empty)")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            return IndexError("queue is underflow(empty)")
        
    def size(self):
        if not self.is_empty():
            return self.item_count
        else:
            return IndexError("queue is underflow(empty)")
        

q1=Queue()
print(q1.is_empty() )
print()
q1.enqueue(10)
q1.enqueue(20)
print(q1.get_front())
print(q1.get_rear())
print(q1.size())
print()
q1.dequeue()
print(q1.get_front())
print(q1.get_rear())
print(q1.size())
         
            
            
            
            