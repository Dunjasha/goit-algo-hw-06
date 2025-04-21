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
        if self.find_phone(phone):
            raise ValueError(f"Phone number '{phone}' already exists.")
        self.phones.append(Phone(phone))



    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(new_phone):
            raise ValueError(f"Phone number '{new_phone}' already exists.")
        self.remove_phone(old_phone)
        self.add_phone(new_phone)



    
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
    
    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if not phone:
            raise ValueError(f"Phone number '{phone_number}' not found.")
        self.phones.remove(phone)
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Record with name '{name}' not found.")

    def __str__(self):
        result = ""
        for record in self.data.values():
            result += str(record) + "\n"
        return result.strip()
    