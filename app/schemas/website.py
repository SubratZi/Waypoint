from __future__ import annotations
from enum import Enum
from pydantic import BaseModel, HttpUrl
from uuid import uuid4
from pydantic import BaseModel, Field, HttpUrl

class Source(str, Enum):
    KNOWLEDGE = "knowledge"
    DUCKDUCKGO = "duckduckgo"
    REDDIT = "reddit"
    GITHUB = "github"
    YOUTUBE = "youtube"

class Pricing(str, Enum):
    FREE = "free"
    FREEMIUM = "freemium"
    PAID = "paid"
    UNKNOWN = "unknown"

class Website(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    url: HttpUrl
    description: str
    category: str
    tags: list[str] = []
    source: Source
    pricing: Pricing = Pricing.UNKNOWN
    official: bool = False
    verified: bool = False
    worldwide: bool = True
    score: float = 0.0
    reason : str | None = None