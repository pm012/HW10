from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    # def __eq__(self, other):
    #     return self.value == other.value
    
    # @property
    # def value(self):
    #     return self.value
    
    # @value.setter
    # def value(self, value):
    #     self.__value = value

class Name(Field):
    def __init__(self, name):
        self.value = name
    # реалізація класу

class Phone(Field):
    def __init__(self, phone):
        self.value = phone

    def is_phone_valid(self):
        return True if re.match(r'^\d{10}$', self.value) else False


   
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)

        if phone.is_phone_valid():
            self.phones.append(phone)
        else:
            raise ValueError
    
    def edit_phone(self, phone_old, phone_new):
        phone_new = Phone(phone_new)
        for i, phone in enumerate(self.phones):
            if phone.value == phone_old:
                if phone_new.is_phone_valid():
                    self.phones[i] = phone_new
                else:
                    raise ValueError("Invalid phone number")
                return
        raise ValueError("Phone not found")
    
    def find_phone(self, phone):
        for _, phone_item in enumerate(self.phones):
            if phone_item.value == phone:
                return phone
            
        return None

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        if record.name:
            self.data.update({record.name.value: record})

    def find(self, name:str):
        # for key, record in   self.data.items():
        #     if key == name:
        #         return record
          
        return  self.data.get(name, None)
    
    def delete(self, name:str):        
        del self.data[name]


if __name__ == '__main__':
 # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    for name, record in book.data.items():
        print(record)