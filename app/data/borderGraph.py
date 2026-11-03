from collections import defaultdict

BORDERS = ( ("USA", "CAN"),
                    ("USA", "MEX"),
                    ("MEX", "BLZ"),
                    ("MEX", "GTM"),
                    ("GTM", "BLZ"),
                    ("GTM", "SLV"),
                    ("GTM", "HND"),
                    ("HND", "NIC"),
                    ("NIC", "CRI"),
                    ("CRI", "PAN"))

def build_graph(borders):
    graph = defaultdict(set)
    for country1, country2 in borders:
        graph[country1].add(country2)
        graph[country2].add(country1)
    return dict(graph)