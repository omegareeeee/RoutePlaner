from fastapi import APIRouter

router = APIRouter()


@router.get("/{country_code}")
def get_route(dest):
    pass
