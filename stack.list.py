#inheriting lis class to impliment stack data structure
class stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,data):
        self.append(data)
        
    def pop(self):
        if not self.is_empty():
            return f"popped element is {super().pop()}"
        else:
            raise IndexError("stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
    
    def insert(self,index,data):
        raise AttributeError("atrribute error 'insert' ")
    

s1=stack()
s1.push(10)
s1.push(20)
print(s1.pop())
print(s1.peek())
s1.insert(1,60)
        
        