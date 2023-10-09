def tree():
    dp = {0:[],1:[TreeNode()]}
    def backtrack(n):
        if n in dp:
            return dp[n]
        res = []
        for l in range(n):
            r = n-1-l
            lefttree,righttree = backtrack(l),backtrack(r)
            for t1 in lefttree:
                for t2 in righttree:
                    res.append(TreeNode(0,t1,t2))
        dp[n] = res
        return res
    return backtrack[n]

print(tree(4))