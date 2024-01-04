''''Binary search tree python implimentation'''
class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
        
class BST:
    def __init__(self):
        self.root=None
    
    def is_empty(self):
        return self.root==None
    
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
        
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.item:
            root.left=self.rinsert(root.left,data)
        elif data>root.item:
            root.right=self.rinsert(root.right,data)
        return  root
    
    def search(self,data):
        if not self.is_empty():
            return self.rsearch(self,self.root,data)
        else:
            raise IndexError("Binary search tree is empty")
    
    def rsearch(self,root,data):
        if data==root.item:
            return root   
        elif data<root.item:
            return self.rinsert(root.left,data)
        else:
            return self.rsearch(root.right,data)
            
    def inroder(self):
        
        

            
                
                    
        

        