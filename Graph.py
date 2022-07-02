class Node:
    def __init__(self,id,lable,country,longitude,internal,latitude,type):
        self.id = id
        self.lable = lable
        self.country = country
        self.longitude = longitude
        self.internal = internal
        self.latitude = latitude
        self.type = type
        self.next = None
    
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
        self.graph= [None] * self.V
        self.matrix = [[0 for i in range(self.V)] for i in range(self.V)] 
    
    def addEdge(self,source,target):
        
        if self.graph[source.id] is not None:
            if target.id == self.graph[source.id].id:
                return 
        node=target
        node.next=self.graph[source.id]
        self.graph[source.id]=node

    def printGraph(self):
        print("Adjacency List:")
        for i in range(self.V):
            print("ID "+str(i) + ":",end=" ")
            temp=self.graph[i]
            while temp:
                print(" -> ",temp.id,end=" ")
                temp=temp.next
            print()
        
        print("\n---------------------------------------------------\n\n")
        print("Adjacency Matrix for first 50 elements: ")
        print(end="   ")
        for i in range(50): print(i,end=" ")
        print("\n",0,"",sep="",end=" ")
        for i in range(50):
            if i!= 0: print(i,end=" ")
            if(i<10): print(end=" ")
            for j in range(50):
                print(self.matrix[i][j],end=" ")
                if(j>10): print(end=" ")
                if(j==10):print(end=" ")
            print()

        print("\nNumber of Vertices:",self.V)
        print("Number of Edges:",self.E)

    
    def makematrix(self,edges):
        for i in edges:
            self.matrix[i.source.id][i.target.id] = 1

        


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

def main():
    buildgraph("Colt.gml")

if __name__ == "__main__":
    main()
