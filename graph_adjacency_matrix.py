class GraphAdjMat:
    def __init__(self, vertices: list[int], edges: list[list[int]]):
        self.vertices: list[int] = []
        self.adj_mat: list[list[int]] = []
        for val in vertices:
            self.add_vertex(val)
        for e in edges:
            self.add_edge(e[0], e[1])

    def size(self) -> int:
        return len(self.vertices)

    def add_vertex(self, val: int):
        n = self.size()
        self.vertices.append(val)

        new_row = [0] * n
        self.adj_mat.append(new_row)
        for row in self.adj_mat:
            row.append(0)

    def remove_vertex(self, index: int):
        if index >= self.size():
            raise IndexError()

        self.vertices.pop(index)
        self.adj_mat.pop(index)
        for row in self.adj_mat:
            row.pop(index)

    def add_edge(self, i: int, j: int):
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()

        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1

    def remove_edge(self, i: int, j: int):
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()

        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0

    def print(self):
        print("顶点列表 =", self.vertices)
        print("领接矩阵 =")
        self.print_matrix(self.adj_mat)
        
    @staticmethod
    def print_matrix(matrix):
        """打印矩阵"""
        for row in matrix:
            print(row)


# 测试代码
if __name__ == "__main__":
    # 创建一个无向图
    vertices = [1, 2, 3, 4]
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    graph = GraphAdjMat(vertices, edges)
    print("初始图：")
    graph.print()

    # 添加一个顶点
    graph.add_vertex(5)
    print("\n添加顶点 5 后：")
    graph.print()

    # 添加一条边
    graph.add_edge(3, 4)
    print("\n添加边 (3, 4) 后：")
    graph.print()

    # 删除一条边
    graph.remove_edge(0, 2)
    print("\n删除边 (0, 2) 后：")
    graph.print()

    # 删除一个顶点
    graph.remove_vertex(1)
    print("\n删除顶点 1 后：")
    graph.print()
