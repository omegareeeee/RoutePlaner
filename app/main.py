from fastapi import FastAPI
from app.modules.route.router import router as CountryRoutesRouter


app = FastAPI(
    title="Country Router Planner",
    description="An Api to get a route to a destination (currently the start is USA only)"
)

app.include_router(CountryRoutesRouter,tags=["Country Planner"])