import json
from turtle import title
from typing import List
FILE_PATH = 'user.json'


class RegisterMixin:
    def __init__(self, name) -> None:
        self.name = name 

    def create(self, name: str, password: str, data: List[dict], **kwargs: dict) -> None:
        new_id = self.__find_max_id(data)
        data.append({'id': new_id, **kwargs})
        
        if len (password) < 8:
            raise Exception('Пароль слишком короткий! ')
        elif password.isdigit() or password.isalpha():
            raise Exception('Пароль должен состоять из бкув и цифр! ')
        
        if name in FILE_PATH.data:
            return 'Такой юзер уже существует!'
        else:
            print('Successfully registered')

        if len (password) < 8:
            raise Exception('Пароль слишком короткий! ')
        elif password.isdigit() or password.isalpha():
            raise Exception('Пароль должен состоять из бкув и цифр! ')

        with open(FILE_PATH, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return password

    def __find_max_id(self, data: List[dict]) -> int:
        if data:
            ids = [i['id'] for i in data]
            return max(ids) + 1
        return 0
    

# 'Такой юзер уже существует!  'Successfully registered'


class LoginMixin:
    def __init__(self, name) -> None:
        self.name = name 

    def login(self, name: str):
        if name in FILE_PATH.data:
            return 'Такой юзер уже существует!'
        else:
            raise 'Нет такого юзера в БД!'

    def validate_password(self, password, password2, data: List[dict]):        
        if len (password) < 8:
            raise Exception('Пароль слишком короткий! ')
        elif password.isdigit() or password.isalpha():
            raise Exception('Пароль должен состоять из букв и цифр! ')
        if password != password2:
            raise Exception('Пароли не совпадают! ')

        with open(FILE_PATH, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return password

# 'Нет такого юзера в БД!'    'Неверный пароль!'    'Вы успешно залогинились!'


class ChangePasswordMixin:
    def __init__(self, name) -> None:
        self.name = name 

    def login(self, name: str):
        if name in FILE_PATH.data:
            return 'Такой юзер уже существует!'
        else:
            raise 'Нет такого юзера в БД!'

    def change_password(self, old_password: str, new_password: str, password: str, password2: str, data: List[dict]):
        self.password = old_password
        self.old_password = new_password
        if len (password) < 8:
            raise Exception('Пароль слишком короткий! ')
        elif password.isdigit() or password.isalpha():
            raise Exception('Пароль должен состоять из букв и цифр! ')
        if password != password2:
            raise Exception('Пароли не совпадают! ')
        if old_password == new_password:
            raise Exception('Старый пароль указан не верно!')
        else:
            print('Password changed successfully!')
        with open(FILE_PATH, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return password    
    
#  'Старый пароль указан не верно!'   'Password changed successfully!'


class ChangeUsernameMixin:
    def __init__(self, name) -> None:
        self.name = name 
        

    def change_name(self, old_name, new_name):
        self.name = old_name
        self.old_name = new_name



#  'Нет такого зарегистрированного юзера в БД!'  'Пользователь с таким именем уже существует!'   'Username changed successfully!'


class CheckOwnerMixin:
    def __init__(self, name) -> None:
        self.name = name 

    def check(self, owner):
        self.name = owner
        if owner in FILE_PATH:
            raise Exception('Такой пользователь уже существует! ')
        return owner

# 'Нет такого пользователя!'


class Post(CheckOwnerMixin):
    def __init__(self, title, description, price, quantity, owner) -> None:
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.owner = owner


class User(RegisterMixin, LoginMixin, CheckOwnerMixin, ChangePasswordMixin, ChangeUsernameMixin):
    def __init__(self, user_name, password, password_confirm) -> None:
        self.user_name = self.check(user_name)
        self.password = self.validate_password(password, password_confirm)
        User.FILE_PATH.append(user_name)

    
        with open(FILE_PATH, 'w') as file:
            json.dump(file, ensure_ascii=False, indent=4)
        

    def validate_password(self, pass1: str, pass2: str):
        if len (pass1) < 8:
            raise Exception('Пароль слишком короткий! ')
        elif pass1.isdigit() or pass1.isalpha():
            raise Exception('Пароль должен состоять из бкув и цифр! ')
        if pass1 != pass2:
            raise Exception('Пароли не совпадают! ')

        return pass1


john = User('John312', '12345678a', '12345678a')
# # john = User('John312', '12345678', '1234567')

sam = User('John_2_312', 'a1234567', 'a1234567')