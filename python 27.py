def issymetric(root:TreeNode)->bool:
    def ismirror(left:TreeNode,right:TreeNode)->bool:
        if not left and not right:return True
        if not left or not right:return False
        if left.value!=right.value:return False
        return ismirror(left.left, right.right) and ismirror(left.right, right.left)
    return ismirror(root, root)
