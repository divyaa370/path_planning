import heapq
from .graph import Cell
from .utils import trace_path


def breadth_first_search(graph, start, goal):
    graph.init_graph()

    start_key = (start.i, start.j)
    goal_key = (goal.i, goal.j)

    queue = [start_key]
    graph.visited[start_key] = True
    graph.parent[start_key] = None

    while queue:
        i, j = queue.pop(0)
        graph.visited_cells.append(Cell(i, j))

        if (i, j) == goal_key:
            return trace_path(goal, graph)

        for ni, nj in graph.find_neighbors(i, j):
            if graph.check_collision(ni, nj):
                continue
            if not graph.visited[(ni, nj)]:
                graph.visited[(ni, nj)] = True
                graph.parent[(ni, nj)] = (i, j)
                queue.append((ni, nj))

    return []


def a_star_search(graph, start, goal):
    graph.init_graph()

    start_key = (start.i, start.j)
    goal_key = (goal.i, goal.j)

    graph.g_cost[start_key] = 0
    graph.f_cost[start_key] = abs(start.i - goal.i) + abs(start.j - goal.j)

    open_list = []
    heapq.heappush(open_list, (graph.f_cost[start_key], start_key))

    # Mark start as visualized
    graph.visited_cells.append(Cell(start.i, start.j))

    while open_list:
        _, (i, j) = heapq.heappop(open_list)

        if graph.visited[(i, j)]:
            continue

        graph.visited[(i, j)] = True
        graph.visited_cells.append(Cell(i, j))

        if (i, j) == goal_key:
            return trace_path(goal, graph)

        for ni, nj in graph.find_neighbors(i, j):

            if graph.check_collision(ni, nj):
                continue

            tentative_g = graph.g_cost[(i, j)] + 1

            if tentative_g < graph.g_cost[(ni, nj)]:
                graph.parent[(ni, nj)] = (i, j)
                graph.g_cost[(ni, nj)] = tentative_g

                # SOFTENED HEURISTIC (explores more cells)
                h = abs(ni - goal.i) + abs(nj - goal.j)
                h *= 0.5

                graph.f_cost[(ni, nj)] = tentative_g + h

                heapq.heappush(open_list, (graph.f_cost[(ni, nj)], (ni, nj)))

                # VISUALIZE NEIGHBORS AS EXPLORED EARLY
                graph.visited_cells.append(Cell(ni, nj))

    return []




def depth_first_search(graph, start, goal):
    graph.init_graph()

    start_key = (start.i, start.j)
    goal_key = (goal.i, goal.j)

    stack = [start_key]
    graph.visited[start_key] = True
    graph.parent[start_key] = None

    while stack:
        i, j = stack.pop()
        graph.visited_cells.append(Cell(i, j))

        if (i, j) == goal_key:
            return trace_path(goal, graph)

        for ni, nj in graph.find_neighbors(i, j):
            if graph.check_collision(ni, nj):
                continue
            if not graph.visited[(ni, nj)]:
                graph.visited[(ni, nj)] = True
                graph.parent[(ni, nj)] = (i, j)
                stack.append((ni, nj))

    return []
