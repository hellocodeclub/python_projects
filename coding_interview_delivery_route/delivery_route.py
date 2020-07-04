
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

def find_route(area):
    area_graph = build_graph(area)

    # Start at the 0,0 cell
    current_cell = Cell(0,0)
    already_visited_list = [current_cell]
    path =[current_cell]

    while(area[current_cell.row][current_cell.col]!=2):
        current_cell = move_next_available(current_cell,already_visited_list,area_graph)
        if(not current_cell):
            # the truck got to dead end, go back
            current_cell = already_visited_list[len(already_visited_list)-2]
            path.pop()
        else:
            already_visited_list.append(current_cell)
            path.append(current_cell)

    return len(path)-1

def move_next_available(current_cell, alreadyVisitedCells, area_graph):
    for adjacent_cell in area_graph[current_cell.hashkey()]:
        if(not (adjacent_cell in alreadyVisitedCells)):
            return adjacent_cell

    return None
