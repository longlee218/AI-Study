graph = {
    'A': ['D', 'C', 'B'],
    'D': [],
    'C': ['G', 'F'],
    'B': ['F', 'E'],
    'G': [],
    'F': ['J'],
    'E': ['I', 'H'],
    'J': [],
    'I': [],
    'H': []
}


def bfs_part2(graph, node, end):
    visit = dict()
    for i, j in graph.items():
        visit[i] = False
    queue = [node]
    visit[node] = True
    while queue:
        current = queue.pop(0)
        if current == end:
            print(current)
            break
        print(current)
        for child in graph[current]:
            if visit[child] is False:
                queue.append(child)
                visit[child] = True


if __name__ == '__main__':
    end = 'G'
    bfs_part2(graph, 'A', end)