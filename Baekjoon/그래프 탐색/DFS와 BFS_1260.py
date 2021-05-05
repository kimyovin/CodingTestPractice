def DFS(graph, root):
    visited=[]
    stack=[root]    # start node를 먼저 넣어 놓음

    while stack:    # 스택이 비어질 때까지 !!
        n = stack.pop() # n을 방문한다.
        if n not in visited:
            visited.append(n)
            if n in graph:  # 인접한 노드가 있으면
                # n과 이어져있는 node를 stack에 넣음
                # set() - set()
                stack += sorted(list(set(graph.get(n)) - set(visited)), reverse=True)
    
    return " ".join(str(i) for i in visited)  # 방문한 순서를 return 함

from collections import deque
def BFS(graph, root):
    visited=[]
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                queue += sorted(list(set(graph.get(n)) - set(visited)))
    
    return " ".join(str(i) for i in visited)

graph = {}  # dict{ node: [연결된 노드 list]}
info = input().split(' ')
n, m, v = [int(i) for i in info]
# input 처리
for _ in range(m):
    edge = input().split(' ')
    n1, n2 = [int(i) for i in edge]

    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)
    
print(graph)
print(DFS(graph, v))
print(BFS(graph, v))

'''
https://www.acmicpc.net/problem/1260
'''
