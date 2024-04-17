from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException

app = FastAPI(openapi_url="/api/v1/libraries/openapi.json", docs_url="/api/v1/libraries/docs")

libraries_router = APIRouter()

libraries = [{'library_id': 1,
              'name': 'Central Library',
              'address': '123 Main Street',
              'square_meters': 5000,
              'city': 'New York'},
             {'library_id': 2,
              'name': 'City Public Library',
              'address': '456 Elm Avenue',
              'square_meters': 3500,
              'city': 'Los Angeles'},
             {'library_id': 3,
              'name': 'Metropolitan Library',
              'address': '789 Oak Boulevard',
              'square_meters': 4200,
              'city': 'Chicago'},
             {'library_id': 4,
              'name': 'Downtown Library',
              'address': '101 Pine Street',
              'square_meters': 2800,
              'city': 'London'},
             {'library_id': 5,
              'name': 'Main City Library',
              'address': '555 Maple Drive',
              'square_meters': 3800,
              'city': 'Tokyo'}]


@libraries_router.get("/")
async def read_libraries():
    return libraries


@libraries_router.get("/{libraries_id}")
async def read_libraries(libraries_id: int):
    for library in libraries:
        if library['libraries_id'] == libraries_id:
            return library
    return None


app.include_router(libraries_router, prefix='/api/v1/libraries', tags=['libraries'])

if __name__ == '__main__':
    import uvicorn
    import os

    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
