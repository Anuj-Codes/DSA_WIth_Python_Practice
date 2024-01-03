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
    
    def insert_node(self,data):
        n=Node(data) #setting left and right as None default
        if not self.is_empty():
            temp=self.root
            prev=None
            while temp is not None:
                if n.item<temp.item:
                    prev=temp
                    temp=temp.left
                    #self.root.left=n
                else:
                    prev=temp
                    temp=temp.right
                    #self.root.right=n
            if n.item<prev.item:
                prev.left=n
            else:
                prev.right=n
    def print_bst(self):
        '''printing the binary search tree using inorder traversal method'''
        if not self.is_empty():
            temp=self.root
            while 
        

        