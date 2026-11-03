from app.modules.graph.constant import COUNTRY_BORDER_GRAPH
from collections import deque

def contains_country(country: str):
    return country in COUNTRY_BORDER_GRAPH

def get_route_to_dest(graph: dict, src: str, dest: str):
    if src == dest:
        return [src]

    queue = deque([src, [src]])
    prev = {src}

    while queue:
        cur, route = queue.popleft()

        for node in graph.get(cur, []):
            if node == dest:
                return route + [node]

            if node not in prev:
                prev.add(node)
                queue.append((node, route + [node]))

    return None