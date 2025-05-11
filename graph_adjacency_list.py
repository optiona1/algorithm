class Vertex:
    """顶点类"""

    def __init__(self, val: int):
        """构造方法"""
        self.val = val

    def __eq__(self, other):
        """重写等于运算符"""
        return self.val == other.val

    def __hash__(self):
        """重写哈希方法"""
        return hash(self.val)

    def __repr__(self):
        """重写字符串表示方法"""
        return f"Vertex({self.val})"

    
class GraphAdjList:
    """基于邻接表实现的无向图类"""

    def __init__(self, edges: list[list[Vertex]]):
        """构造方法"""
        # 邻接表，key：顶点，value：该顶点的所有邻接顶点
        self.adj_list = dict[Vertex, list[Vertex]]()
        # 添加所有顶点和边
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])

    def size(self) -> int:
        """获取顶点数量"""
        return len(self.adj_list)

    def add_edge(self, vet1: Vertex, vet2: Vertex):
        """添加边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        # 添加边 vet1 - vet2
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)

    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        """删除边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        # 删除边 vet1 - vet2
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)

    def add_vertex(self, vet: Vertex):
        """添加顶点"""
        if vet in self.adj_list:
            return
        # 在邻接表中添加一个新链表
        self.adj_list[vet] = []

    def remove_vertex(self, vet: Vertex):
        """删除顶点"""
        if vet not in self.adj_list:
            raise ValueError()
        # 在邻接表中删除顶点 vet 对应的链表
        self.adj_list.pop(vet)
        # 遍历其他顶点的链表，删除所有包含 vet 的边
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)

    def print(self):
        """打印邻接表"""
        print("邻接表 =")
        for vertex in self.adj_list:
            tmp = [v.val for v in self.adj_list[vertex]]
            print(f"{vertex.val}: {tmp},")


# 测试代码
if __name__ == "__main__":
    # 创建顶点
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)

    # 创建边
    edges = [[v1, v2], [v1, v3], [v2, v4], [v3, v4], [v4, v5]]

    # 创建图
    graph = GraphAdjList(edges)
    print("初始图：")
    graph.print()

    # 添加顶点
    v6 = Vertex(6)
    graph.add_vertex(v6)
    print("\n添加顶点 6 后：")
    graph.print()

    # 添加边
    graph.add_edge(v4, v6)
    print("\n添加边 (4, 6) 后：")
    graph.print()

    # 删除边
    graph.remove_edge(v1, v3)
    print("\n删除边 (1, 3) 后：")
    graph.print()

    # 删除顶点
    graph.remove_vertex(v2)
    print("\n删除顶点 2 后：")
    graph.print()

