class Node:
    self.root
    self.children = []

    def bfs(node):
        stack = [node]
        seen = set(node.val)
        while stack:
            n = stack.pop(0)
            print(n.val)
            for child in n .children:
                stack.append(child)
                seen.add(child.val)   