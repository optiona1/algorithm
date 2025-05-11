from graph_adjacency_list import GraphAdjList, Vertex


def dfs(graph: GraphAdjList, visited: set[Vertex], res: list[Vertex], vet: Vertex):
    res.append(vet)
    visited.add(vet)
    for adj_vet in graph.adj_list[vet]:
        if adj_vet in visited:
            continue
        dfs(graph, visited, res, adj_vet)


def graph_dfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    res = []
    visited = set[Vertex]()
    dfs(graph, visited, res, start_vet)
    return res


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

    # 执行 DFS
    start_vertex = v1
    dfs_result = graph_dfs(graph, start_vertex)
    print("\nDFS 遍历结果（从顶点 {} 开始）：".format(start_vertex.val))
    for vertex in dfs_result:
        print(vertex.val, end=" ")
