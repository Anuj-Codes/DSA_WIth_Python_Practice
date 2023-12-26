class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class Sll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            else:
                temp=temp.next
        return None
    def insert_at_last(self,data):
        temp=self.start
        n=Node(data)
        while temp.next is not None:
            temp=temp.next
        temp.next=n

    def insert_after(self,target_node,data):
        if target_node is not None:
            n=Node(data,target_node.next)
            target_node.next=n
    
    def delete_first(self):
        if self.start is None: #checking if linked list is empty
            pass    
        elif self.start.next is None: #checking if linked list has onely one node
            
            self.start=None
        else: #else case where linked list has more than one node
            self.start=self.start.next
            

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next

            temp.next=None

    def print_list(self):
        temp=self.start
        #print(temp.item,temp.next)
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
        #print(temp.item,end=' ')

mylist=Sll()

mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
# mylist.print_list()

mylist.insert_at_last(70)
mylist.print_list()
print("------",end='\n')
# print(mylist.is_empty())
# print(f"item is at node {mylist.search(80)} and item is not present")
# print(f"item is at node {mylist.search(70)} and item is present")
mylist.insert_after(mylist.search(70),90)
mylist.print_list()
print()
print("delete first",end='\n')
print("--------",end='\n')
mylist.delete_first()
mylist.print_list()
print()
print("delete first",end='\n')
print("--------",end='\n')
mylist.delete_first()
mylist.print_list()
print()
print("delete first",end='\n')
print("--------",end='\n')
mylist.delete_first()
mylist.print_list()
print()
print("delete last",end='\n')
print("--------",end='\n')
mylist.delete_last()
mylist.print_list()
print()
print("delete last",end='\n')
print("--------",end='\n')
mylist.delete_last()
mylist.print_list()



