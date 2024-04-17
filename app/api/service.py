import os
import httpx

READER_SERVICE_HOST_URL = 'http://localhost:8020/api/v1/reader/'

def is_reader_present(reader_id: int):
    return True