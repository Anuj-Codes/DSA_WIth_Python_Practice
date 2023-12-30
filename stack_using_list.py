class Queue:
    def __init__(self):
        self.mylist=[]
        # self.rear=None
        # self.front=None
        
    def is_empty(self):
        return len(self.mylist)==0
    
    def enqueue(self,data):
        self.mylist.append(data)
               
    def dequeue(self):
        if not self.is_empty():
            self.mylist.pop(0)
        else:
            raise IndexError("Queue is empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError("Queue is empty")
    
    def get_rear(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            raise IndexError("Queue is empty")
    
    def size(self):
        if not self.is_empty():
            return len(self.mylist) 
        else:
            raise IndexError("Queue is empty")

q1=Queue()
print(q1.is_empty())
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print(f"size of queue is :{q1.size()}")
print(f"front is : {q1.get_front()}")
print(f"rear is : {q1.get_rear()}")
q1.dequeue()
print(f"front is : {q1.get_front()}")
print(f"rear is : {q1.get_rear()}")
print(f"size of queue is :{q1.size()}")
