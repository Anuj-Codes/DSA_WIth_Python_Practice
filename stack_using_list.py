class Queue:
    def __init__(self):
        self.mylist=[]
        self.rear=None
        self.front=None
        
    def is_empty(self):
        return len(self.mylist)==0
    
    def enqueue(self,data):
        if len(self.mylist)>1:
            self.front=self.mylist[0]
            self.mylist.append(data)
            self.rear=self.mylist[-1]
        else:
            self.mylist.append(data)
            self.front=self.mylist[0]
            self.rear=self.mylist[-1]       

            
        
    def dequeue(self):
        if not self.is_empty():
            self.mylist.pop()
            self.rear=self.mylist[-1]
        else:
            raise IndexError("Queue is empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.front
        else:
            raise IndexError("Queue is empty")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear
        else:
            raise IndexError("Queue is empty")
        

q1=Queue()
print(q1.is_empty())
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(f"front is : {q1.get_front()}")
print(f"rear is : {q1.get_rear()}")
q1.dequeue()
print(f"front is : {q1.get_front()}")
print(f"rear is : {q1.get_rear()}")
