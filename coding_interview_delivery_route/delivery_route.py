
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def hashkey(self):
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

