class Dequeue:
    def __init__(self):
        self.mydequeue=[]
        
    def is_empty(self):
        return len(self.mydequeue)==0
    
    def insert_front(self,data):
        self.mydequeue.insert(0,data)
        
    def insert_rear(self,data):
        self.mydequeue.append(data)

    def delete_front(self):
        if not self.is_empty():
            self.mydequeue.pop(0)
        else:
            raise IndexError("dequeue is empty")
        
    def delete_rear(self):
        if not self.is_empty():
            self.mydequeue.pop()
        else:
            raise IndexError("dequeue is empty")
    
    def get_front(self):
        if not self.is_empty():
            return self.mydequeue[0]
        else:
            raise IndexError("dequeue is empty")
    
    def get_rear(self):
        if not self.is_empty():
            return self.mydequeue[-1]
        else:
            raise IndexError("dequeue is empty")
        
    def size(self):
        if not self.is_empty():
            return len(self.mydequeue)
        else:
            raise IndexError("dequeue is empty")
    
dq=Dequeue()
dq.insert_front(10)
dq.insert_front(20)
dq.insert_rear(30)
dq.insert_rear(40)
print(dq.get_front())
print(dq.get_rear())
print("===========")   
dq.delete_front()
dq.delete_rear()
print(dq.get_front())
print(dq.get_rear())  
   
