from pydantic import BaseModel

class RouteResponse(BaseModel):
    dest: str
    list: dict


class RouteIn(BaseModel):
    dest: str

