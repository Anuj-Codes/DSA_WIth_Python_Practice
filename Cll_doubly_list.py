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
        if not self.is_empty():
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
        # elif self.start==self.start.next:
        #     n.prev=self.start
        #     n.next=self.start
        #     self.start.prev=self.start
        #     self.start.next=n
    
    def printlist(self):
        temp=self.start
        while temp.next!=self.start:
            print(temp.item,end=' ')
            temp=temp.next
        print(temp.item,end=' ')



mylist=CDLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.printlist()
            