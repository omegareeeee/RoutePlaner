from app.modules.route.schema import RouteIn, RouteResponse
from app.modules.graph.service import get_route_to_dest,  contains_country

class RouteService():

    def __init__(self):
        pass

    def get_route(self, data: RouteIn):
        dest = data.dest

        if contains_country(dest) == None:
            return None

        route = get_route_to_dest("USA", dest=dest)
        res = RouteResponse(dest=dest, route=route)

        return res


