class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Cll:
    def __init__(self,last):
        self.last=last

    def is_empty(self):
        return self.last==None
    
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    
    def search(self,data):
        if self.is_empty():
            return None
        else:
            temp=self.last.next
            while temp!=self.last:
                if temp.item==data:
                    return temp
                else:
                    temp=temp.next
            if temp.item==data:
                return temp
            return None
        
    def insert_after(self,data,temp):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if self.last==temp:
                self.last=n
    
    def printlist(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=' ')
                temp=temp.next
            print(temp.item)

    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next

                temp.next=self.last.next
                self.last=temp
        return "list is empty"
    
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
        else:
            if self.last.next.item==data:
                self.delete_first()
            else:
                temp=self.last.next
                while temp!=self.last:
                    if temp.next==self.last:
                        if self.last.item==data:
                            self.delete_last()
                            break
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
                return "data not found"
    
    def __iter__(self):
        if self.last is None:
            return CLLiterator(None)
        else:
            return CLLiterator(self.last.next)

class CLLiterator:
    def __init(self,start):
        self.current=start
        self.start=start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
           data=self.current.item
           self.current=self.current.next
           if self.current==self.start:
               raise StopIteration
               
           
           return data



            

        

        

