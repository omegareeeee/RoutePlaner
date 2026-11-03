import pytest

# Test to get route for Belize
def test_happy_path_to_blz_endpoint(client):
    res = client.get("/BLZ")
    assert res.status_code == 200
    assert res.json() == {"dest":"BLZ", "route":["USA", "MEX", "BLZ"]}

# Test to get route for Panama
def test_happy_path_to_pan_endpoint(client):
    res = client.get("/PAN")

    assert res.status_code == 200
    assert res.json() == {"dest":"PAN", "route":["USA", "MEX", "GTM", "HND", "NIC", "CRI", "PAN"]}

# Test if return value is None of the dest. doesn't exist
def test_dest_not_exist_endpoint(client):
    res = client.get("/DoesNotExist")
    assert res.status_code == 404

# Test is similar to case 1, but in lowercase
def test_case_insensitive_endpoint(client):
    res = client.get("/blz")

    assert res.status_code == 200
    assert res.json() == {"dest":"BLZ", "route":["USA", "MEX", "BLZ"]}