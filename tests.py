import csv
import os
import unittest

from main import Contact
from main import PhoneBook


class TestPhoneBook(unittest.TestCase):

    def setUp(self) -> None:
        self.filename = "test_contacts.csv"
        self.book = PhoneBook(self.filename)
        self.test_contact = {
            "Имя": "Тест",
            "Фамилия": "Тестов",
            "Отчество": "Тестович",
            "Организация": "ООО Тест",
            "Рабочий_телефон": "+7-123-456-78-90",
            "Личный_телефон": "+7-098-765-43-21",
        }

    def tearDown(self) -> None:
        os.remove(self.filename)

    def test_add_contact(self) -> None:
        self.book.add_contact(self.test_contact)
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
            assert len(data) == 1
            assert data[0] == self.test_contact

    def test_edit_contact(self) -> None:
        self.book.add_contact(self.test_contact)
        self.book.edit_contact("Тест", Фамилия="Новое")
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
            assert len(data) == 1
            assert data[0]["Фамилия"] == "Новое"

    def test_search_contact(self) -> None:
        self.book.add_contact(self.test_contact)
        search_results = self.book.search(Имя="Тест")
        assert search_results != []
        assert isinstance(search_results[0], Contact)
        assert search_results[0].model_dump() == self.test_contact


if __name__ == "__main__":
    unittest.main()
