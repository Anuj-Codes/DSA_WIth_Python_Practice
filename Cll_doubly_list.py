class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next


class CDLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        n=Node(data)
        if  not self.is_empty():
            # if self.start.next==self.start.prev: #checcking if only single node existing in linked list
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
            self.start=n
        else:
            n.prev=n
            n.next=n
            self.start=n

    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
        else:
            n.prev=n
            n.next=n
            self.start=n

    def serach(self,data):
        if not self.is_empty():
            temp=self.start
            while temp.next!=self.start:
                if temp.item==data:
                    return temp
                else:
                    temp=temp.next

            if temp.item==data:
                return temp
    
    def insert_after_node(self,temp,data):
        if temp is not None:
            n=Node(data)
            n.prev=temp
            n.next=temp.next
            temp.next.prev=n
            temp.next=n
        else:
            return "item not found in the list"


    def delete_first(self):
        if not self.is_empty():
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.next.prev=self.start.prev
                self.start.prev.next=self.start.next
                self.start=self.start.next
    
    def delete_last(self):
        if not self.is_empty():
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev
    
    def delete_item(self,data):
        if not self.is_empty():
            temp=self.serach(data)
            if temp is not None:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
                return None
            return "item not found"
        return "linked list is empty"
        
    def printlist(self):
        temp=self.start
        while temp.next!=self.start:
            print(temp.item,end=' ')
            temp=temp.next
        print(temp.item,end=' ')
    
    def __iter__(self):
        return CDLLiterator(self.start)

class CDLLiterator:
    def __init__(self,start):
        self.current=start
        self.first=start
        self.count=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        
        if self.current==self.first and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data

mylist=CDLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.printlist()
print()
mylist.insert_at_last(40)
mylist.printlist()
mylist.insert_at_last(80)
print()
mylist.printlist()
print()
# print(mylist.serach(30))
print(mylist.insert_after_node(mylist.serach(80),60))
mylist.printlist()
# mylist.delete_first()
# print()
# print('-----')
# mylist.printlist()
# mylist.delete_first()
# print()
# print('-----')
# mylist.printlist()
# mylist.delete_first()
# print()
# print('-----')
# mylist.printlist()
# mylist.delete_first()
# print()
# print('-----')
# mylist.printlist()
print(mylist.delete_item(20))
print()
print("--------")
mylist.printlist()
print()
print("==========")
for x in mylist:
    print(x,end=' ')


            