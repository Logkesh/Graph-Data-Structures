from math import sqrt,inf
class Node:
    def __init__(self,id,lable,country,longitude,internal,latitude,type):
        self.id = id
        self.lable = lable
        self.country = country
        self.longitude = longitude
        self.internal = internal
        self.latitude = latitude
        self.type = type
    
    def print_node(self):
        print("Id:",self.id)
        print("Lable:",self.lable)
        print("Country:",self.country)
        print("Longitude:",self.longitude)
        print("Internal:",self.internal)
        print("Latitude:",self.latitude)
        print("type:",self.type)

class Edge:
    def __init__(self,source,target,linklable):
        self.source = source
        self.target = target
        self.linklable = linklable
    
    def print_edge(self):
        print("Source: ")
        self.source.print_node()
        print("Target: ",self.target)
        self.target.print_node()
        print("LinkLabel: ",self.linklable)

class Graph:
    def __init__(self,V,E):
        self.V=V
        self.E=E
        self.graph= [[] for i in range(self.V)] 
        self.matrix = [[0 for i in range(self.V)] for j in range(self.V)] 
        self.undirected_matrix = [[0 for i in range(self.V)] for j in range(self.V)] 
        self.edge_list= None
    
    def maketarget(self):
        self.target = []
        for i in range(self.V):
            if(self.graph[i] is not []):
                self.target.append(self.graph[i])

    def addEdge(self,source,target):
        
        self.graph[source.id].append(target)
        self.graph[source.id] = list(set(self.graph[source.id]))


    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        temp = [d]
        print(d, end=' ')
        
        for u in self.graph[d]:
            if not visited_vertex[u.id]:
                temp+=(self.dfs(u.id, visited_vertex))
        return temp

    def fill_order(self, t, visited_vertex, stack):
        visited_vertex[t] = True
        for i in self.graph[t]:
            if not visited_vertex[i.id]:
                self.fill_order(i.id, visited_vertex, stack)
        stack = stack.append(t)

    def transpose(self):
        gra = Graph(self.V,self.E)
        self.edge_list.sort(key=lambda item:item.source.id)
        for i in self.edge_list:
            gra.addEdge(i.target,i.source)
        
        return gra

    def print_scc(self):
        print("Strongly Conected Componenets: ")
        n_scc = 0
        stack = []
        visited_vertex = [False] * (self.V)
        l = []
        
        self.maketarget()

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
            


        gr = self.transpose()
        gr.maketarget()
        visited_vertex = [False] * (self.V)
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                
                l.append(gr.dfs(i, visited_vertex))
                print(" ")
                l.sort(key = lambda item: len(item),reverse=True)
                n_scc += 1
        print("Number of Strongly Conected Componenets are : ",n_scc)
        print("---------------------------------------------------")

        print("\nLargest Strongly Conected Componenets:")
        print(l[0])
        print("----------------------------------------------------")


    def topologicalSortUtil(self, vertex, visited, stack):
        visited[vertex] = True
        for i in self.graph[vertex]:
            if visited[i.id] == False:
                self.topologicalSortUtil(i.id, visited, stack)
 
        stack.append(vertex)
 
    def topologicalSort(self):

        visited = [False]*self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        print(stack[::-1])  

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def order(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


  
    def kruskal(self):
        print("\nKRUSKAL ALGORITHM")
        result = []
        i, e = 0, 0
        self.edge_list = sorted(self.edge_list, key=lambda item: self.matrix[item.source.id][item.target.id])
        sum=0
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V- 1:
            u=self.edge_list[i].source.id
            v=self.edge_list[i].target.id
            w=self.matrix[self.edge_list[i].source.id][self.edge_list[i].target.id]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.order(parent, rank, x, y)
        print("Edge : Weight")
        
        for u, v, weight in result:
            format_float = "{:.2f}".format(weight)
            print(u, v,sep='->',end =" ")
            sum+=weight
            print(":",format_float)
        fsum="{:.2f}".format(sum)
        print("Sum of weights:",fsum)
    
    def prims(self):
        print("Prims Algorithm\n")
        selected_nodes = [False for node in range(self.V)]
        sum = 0
        result = [[0 for column in range(self.V)] 
                    for row in range(self.V)]
        
        
        while(False in selected_nodes):
            min = inf
            start = 0
            end = 0

            for i in range(self.V):
                if selected_nodes[i]:
                    for j in range(self.V):
                        if (not selected_nodes[j] and self.undirected_matrix[i][j]>0):  
                            if self.undirected_matrix[i][j] < min:
                                min = self.undirected_matrix[i][j]
                                start, end = i, j
            
            selected_nodes[end] = True

            result[start][end] = min
            
            if min == inf:
                result[start][end] = 0
            
            result[end][start] = result[start][end]

        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))
                    sum += self.undirected_matrix[i][j]
        fsum="{:.2f}".format(sum)
        print("Sum of Weight: ",fsum,"\n-------------------------------------------")

    
    def DFSforcycle(self, vertex, visited, departure, time):
        visited[vertex] = True
        for u in range(self.V):
            if not visited[u]:
                time = self.DFSforcycle( u, visited, departure, time)
    
        departure[vertex] = time
        time = time + 1
    
        return time

    def isDAG(self):
        n = self.V

        discovered = [False] * self.V
    
        departure = [None] * self. V
    
        time = 0

        for i in range(n):
            if not discovered[i]:
                time = self.DFSforcycle(i, discovered, departure, time)

        for u in range(n):

            for v in self.graph[u]:
    
                if departure[u] <= departure[v.id]:
                    return False
        return True
        

    def printGraph(self):
        print("Adjacency List:")
        for i in range(self.V):
            if(self.graph[i] !=[]):
                print("ID "+str(i) + ":",end=" ")
                for j in self.graph[i]:
                    print(" -> ",j.id,end=" ")
                print()
        n=70
        print("\n---------------------------------------------------\n\n")
        print("Adjacency Matrix for first 50 elements: ")
        print(end="    ")
        for i in range(n): print(i,end=" ")
        print()
        print("\n",0," ",sep="",end=" ")
        for i in range(n):
            if i!= 0: print(i,end="  ")
            if(i<10): print(end=" ")
            for j in range(n):
                if self.matrix[i][j]>0:
                    print(1,end=" ")
                else:
                    print(0,end=' ')
                if(j>10): print(end=" ")
                if(j==10):print(end=" ")
            print()
        print("\n---------------------------------------------------\n\n")
        print("Graph Map: \nCoordinates: (source,target)\n")
        for i in self.edge_list:
            print((i.source.id,i.target.id),end="\n")

        print("\nNumber of Vertices:",self.V)
        print("Number of Edges:",self.E)

    def shortestpath(self):
        def dfs0(node):
            if (node != end):
                for n in self.graph[node]:
                    previous.append([n,node])
                    dfs0(n.id)
        max = 0
        for i in range(self.V):
            for j in range(i+1,self.V):
                start = i
                end  = j
                previous = []
                dist = 0
                dfs0(start)
            if previous != []:
                print(i,end=' ')
                for i in range(len(previous)):
                    print(previous[i][0].id,end=" ")
                    dist+=1
                if max < dist: max = dist
                print("\nDistance:",dist)
                print()
        print("\nDiameter (Longest Shortest Path): ",max)

        
                    

    def makematrix(self,edges):
        for i in edges:
            if(i.source.lable=='None'):
                i.source.latitude=i.source.longitude=0
            if(i.target.lable=='None'):
                i.target.latitude=i.target.longitude=0

            dist1=(i.source.latitude-i.target.latitude)**2
            dist2=(i.source.longitude-i.target.longitude)**2
            l=sqrt(dist1+dist2)
            self.matrix[i.source.id][i.target.id] = l
            
            self.undirected_matrix[i.source.id][i.target.id] = l
            self.undirected_matrix[i.target.id][i.source.id] = l

        self.edge_list = edges

def buildgraph(file):
    text = ""
    with open(file) as f:
        txt = f.readlines()
    for i in txt:
        text += " " + i.strip()
    text = text.strip().split("node")
    vertices = text[1:-1]
    edges = text[-1].strip().split("edge")[1:]
    vertices.append(text[-1].strip().split("edge")[0])

    # Extract Vertices

    graph_vertices = []

    for i in vertices:
        text = i.strip().split(" ")[1:-1]
        id=lable=country=longitude=internal=latitude=type = None
        id = int(text[text.index("id")+1])
        lable = text[text.index("label")+1].strip('"')
        if lable != "None":
            country = text[text.index("Country")+1].strip('"')
            longitude = float(text[text.index("Longitude")+1])
            internal = int(text[text.index("Internal")+1])
            latitude = float(text[text.index("Latitude")+1])
            type = " ".join(text[text.index("type")+1:]).strip().strip('"')
        graph_vertices.append(Node(id,lable,country,longitude,internal,latitude,type))

    # Extract Edges

    graph_edges = []

    for i in edges:
        text = i.strip().split(" ")[1:-1]
        source = target = linklabel = None
        source = int(text[text.index("source")+1])
        target = int(text[text.index("target")+1])
        linklabel = " ".join(text[text.index("LinkLabel")+1:]).strip().strip("]").strip().strip('"')
        graph_edges.append(Edge(graph_vertices[source],graph_vertices[target],linklabel))

    
    G = Graph(len(graph_vertices),len(graph_edges))

    for i in graph_edges:
        G.addEdge(i.source,i.target)
    G.makematrix(graph_edges)

    G.printGraph()
    print("---------------------------------------------------\n")  
    G.print_scc()
    print("Is it Acyclic? : ",G.isDAG())
    if(G.isDAG()):
        print("Topological Sort:")
        G.topologicalSort()
        print("----------------------------------------------------")

    G.prims() 
    G.kruskal()  
    print("---------------------------------------------------\n")
    print("Shortest Path")
    G.shortestpath()
    print("---------------------------------------------------\n")
def main():
    buildgraph("input.gml")

if __name__ == "__main__":
    main()