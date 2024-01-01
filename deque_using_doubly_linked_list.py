class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
        
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    
    def is_empty(self):
        return self.front==None
    
    
    def insert_front(self,data):
        n=Node(data) #created node with prev and next with default None value
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            n.next=self.front
            self.front.prev=n
            self.front=n
        self.item_count+=1
          
    def insert_rear(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            self.rear.next=n
            n.prev=self.rear
            self.rear=n
        self.item_count+=1
        
    def delete_front(self):
        if not self.is_empty():
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.front.next.prev=None
                self.front=self.front.next
            self.item_count-=1
        else:
            return IndexError("Deque is empty")
    
                
    def delete_rear(self):
        if not self.is_empty():
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.rear.prev.next=None
                self.rear=self.rear.prev
            self.item_count-=1
        else:
            return IndexError("Deque is empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            return IndexError("Deque is empty")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            return IndexError("Deque is empty")
            
    def size(self):
        if not self.is_empty():
            return self.item_count
        else:
            return IndexError("Deque is empty")
            
        
dq=Deque()
dq.insert_front(10)
dq.insert_front(20)
dq.insert_rear(30)
dq.insert_rear(40)
print(dq.size()) 
print(dq.get_front())
print(dq.get_rear()) 
print("-----------------")   
dq.delete_front()
dq.delete_rear()
print(dq.get_front())
print(dq.get_rear()) 
print('---------')
dq.insert_front(50)
dq.insert_front(60)
dq.insert_rear(70)
dq.insert_rear(80)
print(dq.get_front())
print(dq.get_rear()) 
print(dq.size())      
               
            
            