my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
def Dir_cyclic_or_acyclic(Graph):
    if Graph.gtype!="d":
        return None
    elif Graph.gtype=="d":
        adj_list=Graph.adj
        for i in adj_list:
            if adj_list[i] == None:
                adj_list[i]=[]
        color = {}
        parent = {}

        for u in adj_list.keys():
            color[u] = 'W'
            parent[u] = None
                      
        def dfs(u, color):
            color[u] = 'G'
            for v in adj_list[u]:
                if color[v]=='W':
                    cycle = dfs(v, color)
                    if cycle:
                        return True
                elif color[v]=='G': 
                    return True
            color[u] = 'B'
            return False

        is_cyclic = False
        for u in adj_list.keys():
            if color[u] == 'W':
                is_cyclic = dfs(u, color)
                if is_cyclic:
                    break
        return is_cyclic
def UnDir_cyclic_or_acyclic(Graph):
    if Graph.gtype!="u":
        return None
    elif Graph.gtype=="u":
        adj_list=Graph.adj
        color = {}
        parent = {}
        
        for u in adj_list.keys():
            color[u] = 'W'
            parent[u] = None
        
        def dfs(u, color, parent):
            color[u] = 'G'
            for v in adj_list[u]:
                if color[v] == 'W':
                    parent[v] = u
                    cycle = dfs(v, color, parent)
                    if cycle == True:
                        return True
                elif color[v] == "G" and parent[u]!=v:
                    return True
            color[u] = "B"
            return False
        
        is_cyclic = False
        for u in adj_list.keys():
            if color[u] == 'W':
                is_cyclic = dfs(u, color, parent)
                if is_cyclic == True:
                    return is_cyclic
                else:
                    return False
def T_sort(Graph):
    if Graph.gtype=="d":
        deger=Dir_cyclic_or_acyclic(Graph)
        if deger==False:
            def topologicalSortUtil(Graph,v,visited,stack):
                visited[v] = True
                 
                if Graph.adj[v]==None:
                    kl=[]
                else:
                    kl=Graph.adj[v]
                for i in kl:
                    if visited[i] == False:
                        topologicalSortUtil(Graph,i,visited,stack)
                stack.insert(0,v)
            def topologicalSort(Graph):
                visited = [False]*len(Graph.vertices)
                stack =[]
                for i in range(len(Graph.vertices)):
                    if visited[i] == False:
                        topologicalSortUtil(Graph,i,visited,stack)
                return(stack)
            return topologicalSort(Graph)
        else:
            return None
    else:
        return None