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
    
    def insert_after_node(self,temp,data):
        if temp is not None:
            n=Node(data)
            if temp.next==self.start.prev:
                # print("inside if this")
                n.prev=temp
                n.next=temp.next
                temp.next=n
                self.start.prev=n
            else:
                # print("inside this now")
                n.prev=temp
                n.next=temp.next
                temp.next.prev=n
                temp.next=n
        else:
            return "item not found in the list"


    def delete_first(self):
        if not self.is_empty():
            self.start.next.prev=self.start.prev
            self.start.prev.next=self.start.next
            self.start=self.start.next


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
# print()
# mylist.insert_at_last(30)
# mylist.printlist()
# mylist.insert_at_last(60)
# print()
# mylist.printlist()
print()
# # print(mylist.serach(30))
print(mylist.insert_after_node(mylist.serach(20),60))
mylist.printlist()
mylist.delete_first()
print()
print('-----')
mylist.printlist()

            