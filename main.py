from models import Contact
from phonebook import PhoneBook


def console_interface(book: PhoneBook) -> None:
    while True:
        print("\n1. Добавить контакт")
        print("2. Просмотреть справочник")
        print("3. Редактировать контакт")
        print("4. Поиск по справочнику")
        print("5. Выход")
        user_choice = input("Выберите действие: ")

        if user_choice == "1":
            info = {}
            for field in Contact.model_fields.keys():
                user_input = input(f"Введите {field}: ")
                info[field] = user_input
            book.add_contact(info)

        elif user_choice == "2":
            book.view_contacts()

        elif user_choice == "3":
            name = input("Введите имя контакта для редактирования: ")
            if not any(contact.Имя == name for contact in book.contacts):
                print("Контакт с таким именем не найден.")
                continue
            print("Введите изменения'. Для завершения введите 'end'.")
            changes = {}
            while True:
                key = input("Введите поле: ")
                if key.lower() == "end":
                    break
                value = input("Введите значение: ")
                changes[key] = value
                break
            book.edit_contact(name, **changes)

        elif user_choice == "4":
            print("Введите параметры поиска'. Для завершения введите 'end'.")
            search_params = {}
            while True:
                key = input("Введите поле: ")
                if key.lower() == "end":
                    break
                value = input("Введите значение: ")
                search_params[key] = value
                break
            search_contacts = book.search(**search_params)
            for contact in search_contacts:
                contact.view_contact()

        elif user_choice == "5":
            break

        else:
            print("Некорректный ввод. Выберите действие от 1 до 5.")


if __name__ == "__main__":
    phone_book = PhoneBook()
    console_interface(phone_book)
