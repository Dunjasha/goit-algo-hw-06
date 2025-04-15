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
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Phone number must be 10 digits long.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))  
        except ValueError as e:
            print(f"Error adding phone: {e}")


    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return f"Phone number updated: {str(self)}"
        return f"Phone number '{old_phone}' not found in {self.name.value}'s record."
    
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return f"Phone number {phone_number} found in {self.name.value}'s record."
        return f"Phone number {phone_number} not found in {self.name.value}'s record."
    
    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return "Видалено успішно"
        raise ValueError(f"Phone number '{phone_number}' not found.")
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return f"Record with name '{name}' not found."
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record with name '{name}' has been deleted."
        else:
            return f"Record with name '{name}' not found."

    def __str__(self):
        result = ""
        for record in self.data.values():
            result += str(record) + "\n"
        return result.strip()
    
    
book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print(book)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  

book.delete("Jane")

print(book)