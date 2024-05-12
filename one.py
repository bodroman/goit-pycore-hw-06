from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("невірний формат номера телефону")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Використання класів
if __name__ == "__main__":
    # Створюємо нову адресну книгу
    book = AddressBook()

    # Створюємо запис для контакта John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додаємо запис контакта John до адресної книги
    book.add_record(john_record)

    # Створюємо новий запис для контакта Jane з його додаванням
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виводимо всі записи у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходимо та редагуємо телефон для контакта John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виводимо Contact name: John - phones: 1112223333, 5555555555

    # Шукаємо потрібний номер телефону у записі контакту John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виводимо: 5555555555

    # Видаляємо дані конаткту Jane
    book.delete("Jane")
