from pydantic import BaseModel
from typing import List, Optional


class LibraryIn(BaseModel):
    name: str
    address: str
    square: int
    city: str
    library_id: List[int]


class LibraryOut(LibraryIn):
    id: int


class LibraryUpdate(LibraryIn):
    name: Optional[str] = None
    address: Optional[str] = None
    square: Optional[int] = None
    city: Optional[str] = None
    library_id: Optional[List[int]] = None