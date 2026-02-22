from pydantic import BaseModel


class _SOURCE(BaseModel):
    id: str | None
    name: str


class _data_class(BaseModel):
    source: _SOURCE
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
    articles: list[_data_class]

class COREDATA(BaseModel):
    title: str
    description: str
    url: str

class DisplayData(BaseModel):
    title: str
    summary: str
    url: str