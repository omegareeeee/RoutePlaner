from fastapi import APIRouter, Depends,status,HTTPException
from app.modules.route.schema import RouteIn, RouteResponse
from app.modules.route.service import RouteService
from app.modules.route.dependencies import get_service



router = APIRouter()


@router.get("/{country_code}", response_model=RouteResponse, status_code= status.HTTP_200_OK)
def get_route(data: str, service: RouteService = Depends(get_service)):
    
    route = service.get_route(data=RouteIn(dest=data))
    if(route == None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return route
    
