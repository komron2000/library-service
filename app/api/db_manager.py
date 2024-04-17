from app.api.models import LibraryIn, LibraryOut, LibraryUpdate
from app.api.db import libraries, database


async def add_library(payload: LibraryIn):
    query = libraries.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_libraries():
    query = libraries.select()
    return await database.fetch_all(query=query)


async def get_library(id):
    query = libraries.select(libraries.c.id == id)
    return await database.fetch_one(query=query)


async def delete_library(id: int):
    query = libraries.delete().where(libraries.c.id == id)
    return await database.execute(query=query)


async def update_library(id: int, payload: LibraryIn):
    query = (
        libraries
        .update()
        .where(libraries.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
