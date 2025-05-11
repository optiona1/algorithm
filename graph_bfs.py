from collections import deque
from graph_adjacency_list import GraphAdjList, Vertex


def graph_bfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    res = []
    visited = set[Vertex]([start_vet])
    que = deque[Vertex]([start_vet])

    while len(que) > 0:
        vet = que.popleft()
        res.append(vet)
        for adj_vet in graph.adj_list[vet]:
            if adj_vet in visited:
                continue
            que.append(adj_vet)
            visited.add(adj_vet)
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

    # 执行 BFS
    start_vertex = v1
    bfs_result = graph_bfs(graph, start_vertex)
    print("\nBFS 遍历结果（从顶点 {} 开始）：".format(start_vertex.val))
    for vertex in bfs_result:
        print(vertex.val, end=" ")

