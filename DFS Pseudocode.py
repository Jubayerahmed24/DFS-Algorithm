def DFS(G, u):
    u.visited = True
    for v in G.Adj[u]:
        if not v.visited:
            DFS(G, v)

def init(G):
    for u in G:
        u.visited = False
    for u in G:
        if not u.visited:
            DFS(G, u)