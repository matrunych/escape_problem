from queue import Queue


def check(x, y):
    return x in graph[y]


def add(*args):
    vertex = args[0]
    for i in args[1:]:
        if not check(vertex, i):
            graph[i].append(vertex)
        if not check(i, vertex):
            graph[vertex].append(i)


def escape_problem(data):
    counter = 0
    global used1
    global graph
    used1 = [False] * (len(data) ** 2)
    graph = []
    coords = []
    for i in range(len(data) ** 2):
        graph.append([])
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 1:
                coords.append(i * len(data) + j)
                used1[i * len(data) + j] = True
                counter += 1
            vertex = i * len(data) + j
            if i == 0 and j == 0:
                add(vertex, vertex + len(data), vertex + 1)
            elif i == len(data) - 1 and j == len(data) - 1:
                add(vertex, vertex - len(data), vertex - 1)
            elif i == 0 and j == len(data) - 1:
                add(vertex, vertex + len(data), vertex - 1)
            elif i == len(data) - 1 and j == 0:
                add(vertex, vertex + 1, vertex - len(data))
            elif i == 0:
                add(vertex, vertex + 1, vertex - 1, vertex + len(data))
            elif j == 0:
                add(vertex, vertex + 1, vertex + len(data), vertex - len(data))
            elif i == len(data) - 1:
                add(vertex, vertex - 1, vertex + 1, vertex - len(data))
            elif j == len(data) - 1:
                add(vertex, vertex - 1, vertex + len(data), vertex - len(data))
            else:
                add(vertex, vertex + 1, vertex - 1, vertex + len(data), vertex - len(data))
    flows = []
    for i in coords:
        if i % len(data) == 0 or i % len(data) == len(data) - 1 or i // len(data) == len(data) - 1 or i // len(
                data) == 0:
            flows.append([[i // len(data), i % len(data)]])
        else:
            d = []
            result = []
            for j in range(len(data) ** 2):
                d.append(-1)
            queue = Queue()
            queue.put(i)
            flag = False
            used = [False] * len(data) ** 2
            used[i] = True
            while not queue.empty():
                v = queue.get()
                for l in graph[v]:
                    if not used1[l] and not used[l]:
                        d[l] = v
                        queue.put(l)
                        used[l] = True
                        if l % len(data) == len(data) - 1 or l % len(data) == 0 or l // len(data) == len(
                                data) - 1 or l // len(data) == 0:
                            last = l
                            flag = True
                            break
                if flag:
                    break
            if flag:
                p = last
                result.append([p // len(data), p % len(data)])
                while d[p] != -1:
                    p = d[p]
                    used1[p] = True
                    result.append([p // len(data), p % len(data)])
                result = result[::-1]
                flows.append(result)
    return flows


print(escape_problem([[0, 1, 0, 1, 1, 1, 0, 0],
                      [0, 1, 1, 0, 0, 0, 1, 1],
                      [0, 1, 1, 1, 1, 0, 0, 0],
                      [1, 0, 0, 0, 1, 0, 0, 0],
                      [1, 0, 1, 1, 1, 0, 0, 1],
                      [0, 0, 0, 0, 1, 0, 1, 1],
                      [0, 1, 1, 0, 1, 1, 0, 1],
                      [1, 1, 1, 1, 0, 1, 0, 0]]))
