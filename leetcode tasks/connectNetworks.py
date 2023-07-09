def makeConnection(n,connections):
    l = len(connections)
    if l < n-1:
        return -1

    graph = [set() for i in range(n)]
    for src,dest in connections:
        graph[src].add(dest)
        graph[dest].add(src)
        

    visited = [0]*n
    def dfs(node):
        if visited[node]:
            return 0

        visited[node]=1
        for neighbour in graph[node]:
            dfs(neighbour)
        return 1

    return sum(dfs(node) for node in range(n))-1

print(makeConnection(2, [[0,1],[0,2],[1,2]]))