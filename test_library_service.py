import requests


def test_get_all_libraries(url: str):
    res = requests.get(url).json()
    assert(res == [{'library_id': 1,
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
              'city': 'Tokyo'}])


def test_get_library_by_id(url: str):
    res = requests.get(url).json()
    assert(res == {'library_id': 1,
              'name': 'Central Library',
              'address': '123 Main Street',
              'square_meters': 5000,
              'city': 'New York'})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/libraries'
    test_get_library_by_id(URL + '1')
    test_get_all_libraries(URL)