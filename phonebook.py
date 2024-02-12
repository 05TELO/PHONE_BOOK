import csv
import os
from typing import Any
from typing import List

from pydantic import ValidationError

from models import Contact


class PhoneBook:
    def __init__(self, filename: str = "contacts.csv") -> None:
        """
        Инициализирует телефонную книгу, загружая данные из файла CSV.

        :param: filename: имя CSV-файла для загрузки контактов.
        """
        self.filename = filename
        if not os.path.isfile(self.filename):
            open(self.filename, "w").close()
        self.contacts = self.load_data_from_csv()
        self.fieldnames = Contact.model_fields.keys()

    def load_data_from_csv(self) -> List[Contact]:
        """
        Загружает контакты из файла CSV.

        :return: список объектов Contact, загруженных из файла CSV.
        """
        contacts = []
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(Contact(**row))
        return contacts

    def add_contact(self, info: dict) -> None:
        """
        Добавляет контакт в телефонную книгу и записывает его в файл CSV.

        :param info: словарь с информацией о контакте.
        """
        try:
            contact = Contact(**info)
        except ValidationError as e:
            raise e
        self.contacts.append(contact)
        self.append_contact_to_csv(contact)

    def append_contact_to_csv(self, contact: Contact) -> None:
        """
        Добавляет контакт в файл CSV.

        :param contact: объект Contact для добавления в файл CSV.
        """
        with open(self.filename, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(contact.model_dump())

    def view_contacts(self) -> None:
        """
        Показывает все контакты в телефонной книге.
        """
        for contact in self.contacts:
            contact.view_contact()

    def edit_contact(self, name: str, **kwargs: Any) -> None:
        """
        Изменяет информацию о контакте и обновляет файл CSV.

        :param name: имя контакта, которого надо изменить.
        :param kwargs: словарь с изменяемыми полями и их новыми значениями.
        """
        for contact in self.contacts:
            if contact.Имя == name:
                for key, value in kwargs.items():
                    setattr(contact, key, value)
                self.rewrite_csv()

    def rewrite_csv(self) -> None:
        """
        Перезаписывает файл CSV новыми данными из телефонной книги.
        """
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.model_dump())

    def search(self, **kwargs: Any) -> List[Contact]:
        """
        Поиск контактов, соответствующих заданным параметрам.

        :param kwargs: словарь с полями и значениями для поиска.
        :return: список объектов Contact, соответствующих параметрам поиска.
        """
        found_contacts: list = []
        for contact in self.contacts:
            if all(
                getattr(contact, key) == value for key, value in kwargs.items()
            ):
                found_contacts.append(contact)
        return found_contacts
