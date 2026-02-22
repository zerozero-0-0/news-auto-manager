from pydantic import BaseModel


class Source(BaseModel):
    id: str | None
    name: str


class DataClass(BaseModel):
    source: Source
    author: str | None
    title: str | None
    description: str | None
    url: str | None
    urlToImage: str | None
    publishedAt: str | None
    content: str | None


class JSONResponse(BaseModel):
    status: str
    totalResults: int
    articles: list[DataClass]

class CoreData(BaseModel):
    title: str
    description: str
    url: str

class DisplayData(BaseModel):
    title: str
    summary: str
    url: str