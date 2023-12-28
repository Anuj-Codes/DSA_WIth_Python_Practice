class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next


class Dll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        if self.start is None:
            return "DLL is empty"
        else:
            return "DLL is not empty"
        
    def insert_at_start(self,data):
        if self.start is not None:
            n=Node(data,self.start.prev,self.start)
            self.start.prev=n
            self.start=n
        else:
            n=Node(data)
            self.start=n

    def insert_at_last(self,data):
        if self.start is not None:
            temp=self.start
            n=Node(data)
            while temp.next is not None:
                temp=temp.next
            n.prev=temp
            temp.next=n
        else:
            n=Node(data)
            self.start=n

   
    def search(self,data):
        if self.start.next is None:
            if self.start.item==data:
                return f"data {data} is present at {self.start} address/reference"
            else:
                return f"data {data} is not present in DLL"
        
        elif self.start is None:
            return "DLL is empty"
        elif self.start is not None:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    return f"data {data} is present at {temp} address/reference"
                else:
                    temp=temp.next
            return f"data {data} is not present in DLL"
   
    def insert_after(self,data,new_data):
        if self.start.next is None:
            if self.start.item==data:
                n=Node(new_data)
                n.prev=self.start
                self.start.next=n
            else:
                return "data is not found" 
        elif self.start is not None:
            temp=self.start

            n=Node(new_data)
            while temp is not None:
                if temp.item==data:
                    n.prev=temp
                    n.next=temp.next
                    temp.next.prev=n
                    temp.next=n
                   
                    break
                else:
                    temp=temp.next


    def print_Dlist(self):
        temp=self.start
        while temp is not None:
            # print(temp.prev)
            # print(temp.item)
            # print(temp.next)
            # print()
            print(temp.item,end=' ')
            temp=temp.next      
    
    def delete_first(self):
        if self.start is not None:
            self.start.next.prev=None
            self.start=self.start.next
            
        elif self.start.next is None:
            self.start=None
        
        else: 
            return "DLL is empty"
    
    def delete_last(self):
        if self.start is None:
            return "DLL is empty"
        elif self.start is not None:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
        else:
            self.start=None
    
    def delete_specific_element(self,data):
        if self.start is None:
            return "DLL is empty"
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
            else:
                return "data is not found in DLL" 
        else:
            # print("inside here123")
            temp=self.start
            # print("first item of DLL ",temp.item)
            while temp is not None:
                # print(temp.prev)
                # print(temp.item)
                # print(temp.next)
                if temp.item==data and temp.next is not None:
                    temp.prev.next=temp.next.prev
                    temp.next.prev=temp.prev.next
                    break
                elif temp.item==data and temp.next is None:
                    # print("inside this if")
                    # print(temp.item)
                    # print("next ",temp.next)
                    # print("prev " ,temp.prev)
                    temp.prev.next=None
                    break
                
                else:
                    # print("inside here")
                    temp=temp.next
            
myDlist=Dll()
# print(myDlist.is_empty())
myDlist.insert_at_start(10)
# myDlist.print_Dlist()
# print()
print("-------")
myDlist.insert_at_start(20)
myDlist.insert_at_start(30)
myDlist.insert_at_start(40)
myDlist.print_Dlist()
print()
# print(myDlist.is_empty())
print("-----------")
myDlist.insert_at_last(90)
myDlist.print_Dlist()
# myDlist.insert_at_last(80)
# myDlist.print_Dlist()
# print()
# print(myDlist.search(30))
# print(myDlist.search(60))
# print(myDlist.search(90))
print(myDlist.insert_after(10,120))
myDlist.print_Dlist()
print()
print("deleting the items")
myDlist.delete_first()
myDlist.print_Dlist()
print()
myDlist.delete_first()
myDlist.print_Dlist()
print()
myDlist.delete_last()
myDlist.print_Dlist()
print()
myDlist.delete_last()
myDlist.print_Dlist()
print()
myDlist.delete_last()
myDlist.print_Dlist()
# print()
print("final check---------")
# myDlist.print_Dlist()
myDlist.delete_specific_element(20)
myDlist.print_Dlist()



    