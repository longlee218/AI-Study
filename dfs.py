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
stack = set()


def dfs_search(node, graph, end):
    if node not in stack:
        print(node)
        stack.add(node)
        for child in graph[node]:
            if child == end:
                return
            dfs_search(child, graph, end)


visit = dict()
for i, j in graph.items():
    visit[i] = False

print(visit)


def dfs_part2(graph, node, end):
    visit[node] = True
    stack = [node]
    while stack:
        current = stack.pop()
        if current == end:
            print(current)
            break
        print(current)
        for child in graph[current]:
            if visit[child] is False:
                stack.append(child)
                visit[child] = True


if __name__ == '__main__':
    end = 'G'
    # dfs_search('A', graph, end)
    dfs_part2(graph, 'A', 'G')
    # print(end)
