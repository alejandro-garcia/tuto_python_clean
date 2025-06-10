from fastapi import FastAPI 
from src.shared.infraestructure.api import router

app = FastAPI()
app.include_router(router)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
