from pydantic import BaseModel, field_validator

class RouteResponse(BaseModel):
    dest: str
    route: list[str]


class RouteIn(BaseModel):
    dest: str

    @field_validator("dest")
    @classmethod
    def clean_dest(cls, dest: str) -> str:
        return dest.strip().upper()

