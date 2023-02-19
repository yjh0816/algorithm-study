from collections import deque

# stack
'''
stack = []

stack.append(0)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack[::-1])

stack.pop()
print(stack)
stack.pop()
print(stack)
'''

# queue
'''
queue = deque()

queue.append(0)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)
queue.reverse()
print(queue)
'''

# recursive
# gcd

'''
def gcd(n1, n2):
    if n1 % n2 == 0:
        return n2
    else:
        return gcd(n2, n1 % n2)


print(gcd(192, 162))
'''

# DFS
'''
def dfs(graph, v, visited):
    visited[v] = True
    print(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)
'''

# BFS
'''
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v)

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True        

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)
'''

# problem 1
def icing(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v)
        for i in box:
            for j in i:
                if not visited[j]:
                    queue.append(j)
                    visited[j] = True

box = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0],
]

visited = [[False for _ in range(len(box[0]))] for _ in range(len(box))]