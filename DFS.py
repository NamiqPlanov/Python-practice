class Node:
    def __init__(self,val,left:Node=None,right:Node=None):
        self.val = val
        self.left = left
        self.right = right
    def dfsinorder(root:Node):
        if root is None:
            return 
        else:
            dfsinorder(root.left)
            print(root.val)
            dfsinorder(root.right)
    def dfssemiorder(root:Node):
        print(root.val)
        dfssemiorder(root.left)
        dfssemiorder(root.right)
    def dfsorder(root:Node):
        dfsorder(root.left)
        dfsorder(root.right)
        print(root.val)
        



 

