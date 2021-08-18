import unittest
from Function import *


class TestSomething(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start of test")

    def test_people_11_2(self):     # Поверка выдачи имени по номеру документа
        self.assertEqual("Геннадий Покемонов", people("11-2"))

    def test_add_doc(self):     # Поверка редактирования словаря и списка
        add("passport", "12345", "Миладзе", "3")
        d = {"type": "passport", "number": "12345", "name": "Миладзе"}
        self.assertTrue(d in documents and "12345" in directories.get("3"))

    def test_delete_doc(self):  # Поверка удаления документа по номеру
        delete("10006")
        variable = 0
        for dic in documents:
            if "10006" in dic.values():
                variable = 1
        for k, v in directories.items():
            if "10006" in v:
                variable = 1
        self.assertTrue(variable == 0)

    @classmethod
    def tearDownClass(cls):
        print("End of the test")


if __name__ == '__main__':
    unittest.main()

