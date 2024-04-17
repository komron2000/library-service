import requests


class LibrariesAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_all_clothes(self):
        url = self.base_url
        res = requests.get(url).json()
        return res

    def get_cloth_by_id(self, cloth_id: int):
        url = f"{self.base_url}{cloth_id}"
        res = requests.get(url).json()
        return res


def test_get_all_clothes(api: LibrariesAPI):
    res = api.get_all_clothes()
    assert (res == [{'library_id': 1,
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

def test_get_cloth_by_id(api: LibrariesAPI):
    res = api.get_cloth_by_id(1)
    assert (res == {'library_id': 1,
              'name': 'Central Library',
              'address': '123 Main Street',
              'square_meters': 5000,
              'city': 'New York'})


def test_get_cloth_by_name(api: LibrariesAPI):
    # Проверка получения информации по имени
    clothes = api.clothes()
    clothes_name = clothes[0]['name']  # Предполагаем, что компания существует в списке
    res = api.get_cloth_by_name(clothes_name)
    assert (res['name'] == clothes_name)


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/libraries/'
    api = LibrariesAPI(URL)
    test_get_cloth_by_id(api)
    test_get_all_clothes(api)
    test_get_cloth_by_name(api)
