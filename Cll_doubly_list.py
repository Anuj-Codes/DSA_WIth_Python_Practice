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
            if self.start.next==self.start.prev: #checcking if only single node existing in linked list
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
    
    def insert_after_node(self,new_data,data):
        n=Node(data)

    def printlist(self):
        temp=self.start
        while temp.next!=self.start:
            print(temp.item,end=' ')
            temp=temp.next
        print(temp.item,end=' ')



mylist=CDLL()
mylist.insert_at_start(10)
# mylist.insert_at_start(20)
#mylist.insert_at_start(30)
mylist.printlist()
print()
mylist.insert_at_last(30)
mylist.printlist()
# mylist.insert_at_last(60)
# print()
# mylist.printlist()
print()
print(mylist.serach(40))
            