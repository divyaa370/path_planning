import json
from .graph import Cell


def trace_path(cell, graph):
    path = []
    while cell is not None:
        path.append(Cell(cell.i, cell.j))
        cell = graph.get_parent(cell)
    path.reverse()
    return path


def generate_plan_file(graph, start, goal, path, algo="", out_name="out.planner"):
    print(f"Saving planning data to file: {out_name}")

    path_data = [[cell.i, cell.j] for cell in path]
    visited_cells_data = [[cell.i, cell.j] for cell in graph.visited_cells]

    plan = {
        "path": path_data,
        "visited_cells": visited_cells_data,
        "dt": [],
        "map": graph.as_string(),
        "start": [start.i, start.j],
        "goal": [goal.i, goal.j],
        "planning_algo": algo
    }

    with open(out_name, 'w') as outfile:
        json.dump(plan, outfile)
