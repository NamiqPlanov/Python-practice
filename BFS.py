class Node:
    def __init__(self,val,right:Node,left:Node):
        self.val = val
        self.right = right
        self.left = left
    def bfs(root):
        stack = [root]
        while stack:
            node = stack.pop(0)
            print(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)