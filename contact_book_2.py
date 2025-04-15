from collections import UserDict


class Field:
    """Базовий клас для полів, таких як Name або Phone."""
    pass


class Phone(Field):
    """Клас для представлення номера телефону."""
    def __init__(self, phone_number):
        if len(str(phone_number)) == 10 and phone_number.isdigit():
            self.value = phone_number
        else:
            raise ValueError("Номер телефону має бути 10-значним числом.")

    def __str__(self):
        return self.value


class Record:
    """Клас для представлення запису в адресній книзі."""
    def __init__(self, name):
        self.name = name  # Об'єкт Name
        self.phones = []  # Список для зберігання об'єктів Phone

    def add_phone(self, phone_number):
        """Додає номер телефону до запису."""
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        """Видаляє номер телефону зі списку."""
        phone_to_remove = None
        for phone in self.phones:
            if phone.value == phone_number:
                phone_to_remove = phone
                break
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError("Номер телефону не знайдений.")

    def edit_phone(self, old_number, new_number):
        """Редагує номер телефону."""
        found = False
        for phone in self.phones:
            if phone.value == old_number:
                found = True
                phone.value = new_number
                break
        if not found:
            raise ValueError("Старий номер телефону не знайдений.")

    def find_phone(self, phone_number):
        """Шукає номер телефону."""
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        phones_str = ", ".join(str(phone) for phone in self.phones)
        return f"{self.name}: {phones_str if phones_str else 'Немає номерів телефону'}"


class AddressBook(UserDict):
    """Клас для адресної книги."""
    def __init__(self):
        super().__init__()

    def add_record(self, name, phone):
        """Додає запис до self.data (зберігається в словнику)."""
        record = Record(name)
        record.add_phone(phone)
        self.data[record.name] = record  # Використовуємо self.data для збереження запису

    def find(self, name):
        """Знаходить запис за ім'ям. Повертає об’єкт Record або None."""
        return self.data.get(name, None)

    def delete(self, name):
        """Видаляє запис за ім'ям."""
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Запис не знайдений.")

    def __str__(self):
        """Магічний метод __str__ для красивого виводу об’єкту класу AddressBook."""
        return "\n".join(str(record) for record in self.data.values())


# Приклад використання:

book = AddressBook()

# Додаємо записи
book.add_record("Daniil", "9012456789")
book.add_record("Davyd", "9012345678")

# Виводимо адресну книгу
print(book)

# Шукаємо запис
record = book.find("Daniil")
if record:
    print(f"Знайдений запис: {record}")

# Редагуємо телефон
record.edit_phone("9012345678", "9012233445")
print(book)

# Видаляємо запис
book.delete("Davyd")
print(book)
