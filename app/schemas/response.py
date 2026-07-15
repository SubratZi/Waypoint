from pydantic import BaseModel
from app.schemas.website import Website

class Route(BaseModel):
    title: str
    websites: list[Website]

class Response(BaseModel):
    intent: str
    routes: list[Route]