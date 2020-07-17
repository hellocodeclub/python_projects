
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def hashkey(self):
        return str(self.row)+str(self.col)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __str__(self):
        return str(self.row)+str(self.col)

def build_graph(area):
    graph = {}
    for row in range(len(area)):
        for col in range(len(area[row])):
            if (area[row][col] != 0):
                current_cell = Cell(row, col)
                cell_doesnt_exist_on_graph = graph.get(current_cell.hashkey()) == None
                if(cell_doesnt_exist_on_graph):
                    graph[current_cell.hashkey()]= []
                # Check the top, left, down and right cells to know the cell that are connected
                adjacents = graph.get(current_cell.hashkey())
                if(row-1>-1):
                    if(area[row-1][col]!=0):
                        adjacents.append(Cell(row-1,col))
                if(col-1>-1):
                    if(area[row][col-1]!=0):
                        adjacents.append(Cell(row,col-1))
                if(row+1<len(area)):
                    if (area[row+1][col]!=0):
                        adjacents.append(Cell(row+1,col))
                if(col+1<len(area[row])):
                    if(area[row][col+1]!=0):
                        adjacents.append(Cell(row,col+1))
                graph[current_cell.hashkey()] = adjacents

    return graph

def dfs(graph,origin):
    where_to_go_next = Stack()
    where_to_go_next.add(origin)
    already_visited = []

    while not where_to_go_next.is_empty():
        current_node = where_to_go_next.pop()
        print(current_node)
        already_visited.append(current_node)
        neighbours = graph[current_node.hashkey()]
        for neighbour in neighbours:
            if neighbour not in already_visited:
                where_to_go_next.add(neighbour)


def dfs_recursive(graph, origin, visited = []):
    if len(graph.keys())==len(visited):
        return None
    else:
        visited.append(origin)
        print(origin)
        neighbours =  graph[origin.hashkey()]
        for neighbour in neighbours:
            if neighbour not in visited:
                dfs_recursive(graph, neighbour, visited)


def bfs_shortest_path(graph, origin, destination):
    where_to_go_next = Queue()
    where_to_go_next.add(origin)
    already_visited = []
    distance = 0


    while not where_to_go_next.is_empty():
        current_node = where_to_go_next.pop()
        distance = distance+1
        already_visited.append(current_node)
        neighbours = graph[current_node.hashkey()]
        if(destination in neighbours):
            return distance+1
        for neighbour in neighbours:
            if neighbour not in already_visited:
                where_to_go_next.add(neighbour)

    return -1

class Stack:

    def __init__(self):
        self.list = []

    def add(self,item):
        if item:
            self.list.append(item)

    def pop(self):
        if len(self.list) == 0: return None
        last_item = self.list[-1]
        del(self.list[-1])
        return last_item

    def print(self):
        print(self.list)

    def is_empty(self):
        return len(self.list) == 0

class Queue:
    def __init__(self):
        self.list = []

    def add(self,item):
        if item:
            self.list.append(item)

    def pop(self):
        if len(self.list) == 0: return None
        last_item = self.list[0]
        del(self.list[0])
        return last_item

    def is_empty(self):
        return len(self.list) == 0

