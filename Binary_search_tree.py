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
            return self.rsearch(self.root,data)
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
        result=[]
        self.rinorder(self.root,result)
        return result
    
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
            
    def preroder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
                
    def postroder(self):
        result=[]
        self.rpostroder(self.root,result)
        return result
    
    
    def rpostroder(self,root,result):
        if root:
            self.rpostroder(root.left,result)
            self.rpostroder(root.right,result)
            result.append(root.item)
    
    def find_min(self):
        if not self.is_empty(): 
            return self.inroder()[0]
        else:
            raise IndexError("binary search tree is empty")
    
    def find_max(self):
        if not self.is_empty(): 
            return self.inroder()[-1]
        else:
            raise IndexError("binary search tree is empty")
    
    def size(self):
        if not self.is_empty():
            return len(self.inroder())
        else:
            raise IndexError("binary search tree is empty")
            
    
    def delete_node(self,data):
        
        
                      

bst=BST()
print(bst.is_empty())
bst.insert(50) 
bst.insert(30)
bst.insert(40)
bst.insert(10)
bst.insert(80)
bst.insert(70)
bst.insert(90)
print("inorder traversal of binary search tree: ",bst.inroder())
print("preorder traversal of binary search tree: ",bst.preroder())
print("postorder traversal of binary search tree: ",bst.postroder())
print(bst.is_empty())
print(bst.search(90))
print(bst.find_min())
print(bst.find_max())
print(bst.size())
                 
        
        

            
                
                    
        

        