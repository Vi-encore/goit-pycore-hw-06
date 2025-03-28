from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    # реалізація класу


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isnumeric():
            value
        else:
            raise ValueError
        super().__init__(value)

    # реалізація класу


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, number, new_number):
        pass


class AddressBook(UserDict):

    def __init__(self) -> None:
        super().__init__()

    # реалізація класу

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        for record in self.data:
            if record == name:
                return self.data[record]
            return None

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)

    #     # Створення нової адресної книги


book = AddressBook()


#     # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
# print(john_record.phones[0], john_record.name)

#     # Додавання запису John до адресної книги
book.add_record(john_record)
# print(book)
#     # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

#     # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

#     # Знаходження та редагування телефону для John
john = book.find("John")
# print(john)
#     john.edit_phone("1234567890", "1112223333")

#     print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#     # Пошук конкретного телефону у записі John
#     found_phone = john.find_phone("5555555555")
#     print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

#     # Видалення запису Jane


book.delete("Jane")
print(book)
