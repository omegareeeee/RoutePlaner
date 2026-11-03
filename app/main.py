from fastapi import FastAPI
from app.modules.route import router as CountryRoutesRouter


app = FastAPI()

app.include_router(CountryRoutesRouter)