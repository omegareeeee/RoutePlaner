import pytest
from app.modules.route.service import RouteService
from app.modules.route.schema import RouteIn, RouteResponse

# Test to get route for Belize
def test_happy_path_to_blz():
    routeService = RouteService()
    input = RouteIn(dest="BLZ")

    res = routeService.get_route(input)

    assert res.dest == "BLZ"
    assert res.route == ["USA", "MEX", "BLZ"]

# Test to get route for Panama
def test_happy_path_to_pan():
    routeService = RouteService()
    input = RouteIn(dest="PAN")

    res = routeService.get_route(input)

    assert res.dest == "PAN"
    assert res.route == ["USA", "MEX", "GTM", "HND", "NIC", "CRI", "PAN"]

# Test if return value is None of the dest. doesn't exist
def test_dest_not_exist():
    routeService = RouteService()
    input = RouteIn(dest="DoesNotExist")

    res = routeService.get_route(input)

    assert res == None


# Test is similar to case 1, but in lowercase
def test_case_insensitive():
    routeService = RouteService()
    input = RouteIn(dest="blz")

    res = routeService.get_route(input)

    assert res.dest == "BLZ"
    assert res.route == ["USA", "MEX", "BLZ"]