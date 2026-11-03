from fastapi import APIRouter, Depends,status,HTTPException
from app.modules.route.schema import RouteIn, RouteResponse
from app.modules.route.service import RouteService
from app.modules.route.dependencies import get_route_service



router = APIRouter()


@router.get("/{country_code}", response_model=RouteResponse, status_code= status.HTTP_200_OK)
def get_route(data: RouteIn, service: RouteService = Depends(RouteService)):
    route = service.get_route(dest=data)
    if(route == None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return route
    
