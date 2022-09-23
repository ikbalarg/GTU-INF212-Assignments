my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
#import avlgtu as avl
#import bstgtu as bst
from collections import deque
#problem1
def problem1(string):
    pass
    """oku=open(string,"r")
    l1=oku.readlines()
    l2=[]
    for i in l1:
        str1=i[:-1]
        lstr1=str1.split()
        stringİc=lstr1[0]+lstr1[1]+lstr1[2]
        l2.append([stringİc,lstr1[3],lstr1[4],lstr1[5]])
    print(len(l2))"""
    
#problem2
def problem2(u,v):
    class Graph:
        def __init__(self,Nodes):
            self.nodes=Nodes
            self.adj={}
            self.l1=[]
            for node in self.nodes:
                self.adj[node]=[]
        def add_edge(self,u,v):
            self.adj[u].append(v)
            self.adj[v].append(u)
        def adj(self):
            for node in self.nodes:
                self.l1.append([node,self.adj_list[node]])
            return self.l1
            
    nodes=u
    graph=Graph(nodes)
    for i in v:
        graph.add_edge(i[0],i[1])
    return graph
#problem3
def problem3(u,v):
    class Graph:
        def __init__(self,Nodes,is_directed=True):
            self.nodes=Nodes
            self.adj={}
            self.l1=[]
            self.is_directed=is_directed
            for node in self.nodes:
                self.adj[node]=[]
        def add_edge(self,u,v):
            self.adj[u].append(v)
            if not self.is_directed:
                self.adj[v].append(u)
            
        def adj1(self):
            for node in self.nodes:
                self.l1.append([node,self.adj_list[node]])
            return self.l1
            
    nodes=u
    graph=Graph(nodes,is_directed=(True))
    for i in v:
        graph.add_edge(i[0],i[1])
    for i in graph.adj:
        if graph.adj[i]==[]:
            graph.adj[i]=None
    return graph
#Problem4
def problem4(x,y):
    class BFSResult:
        def __init__(self):
            self.level = {}
            self.parent = {}
    class Graph:
        def __init__(self):
            self.adj = {}
        def add_edge(self, u, v): 
            if self.adj[u] is None:
                self.adj[u] = []
            self.adj[u].append(v)
    def bfs(g, s):
        r= BFSResult()
        r.parent = {s: None}
        r.level = {s: 0}
        queue = deque()
        queue.append(s)
        while queue:
            u = queue.popleft() 
            try:
                for n in g.adj[u]:
                    if n not in r.level:
                        r.parent[n] = u
                        r.level[n] = r.level[u] + 1
                        queue.append(n)
            except:
                continue
        return r
    return bfs(x,y)
#problem5
def problem5(Vertices,Edges,x,y,z="u"):
    if z=="u":
        deger=problem2(Vertices,Edges).adj
    elif z=="d":
        deger=problem3(Vertices,Edges).adj
    else:
        return None
    def BFS_SP(graph,start,goal):
        explored=[]
        queue=[[start]]
        if start==goal:
            return None
        while queue:
            path=queue.pop(0)
            node=path[-1]
            if node not in explored:
                neighbours=graph[node]
                try:
                    for neighbour in neighbours:
                        new_path=list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)
                        if neighbour==goal:
                            return new_path
                except:
                    continue
                explored.append(node)
        
        return "INF212"
    return BFS_SP(deger,x,y)
    
        