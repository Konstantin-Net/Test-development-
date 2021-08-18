import requests
import unittest

token = ""   # Тут надо ввести токен с Полигона Яндекс.Диска

def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }


def _creating_folder():     # Функция создаёт папку на яндекс диске
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = get_headers()
    params = {"path": "тестовая папка"}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code


class TestSomething(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start of test")

    def test_creating_folder_true(self):    # Проверка ответа сервера на код 200
        self.assertEqual("2", str(_creating_folder())[0])

    def test_creating_folder_false(self):
        self.assertEqual("4", str(_creating_folder())[0])   # Проверка ответа сервера на код 400

    @classmethod
    def tearDownClass(cls):
        print("End of the test")


if __name__ == '__main__':
    unittest.main()
