import json
import os

class User:
    def validate_password(password):
     if len(password) < 8:
        raise ValueError("Пароль слишком короткий!")
     if not password.isalnum():
        raise ValueError("Пароль должен состоять из букв и цифр!")      
     return True

class RegisterMixin:
    def register(self, name, password, id):
        if not os.path.exists('user.json'):
            with open('user.json', 'w') as file:
                json.dump([], file)
        with open('user.json', 'r') as file:
            data = json.load(file)

        for user in data:
            if user['name'] == name:
                print('Пользователь с таким именем уже есть!')
                return
        data.append({
            "id": id,
            "name": name,
            "password": password
        })
        with open('user.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print('Регистрация прошла успешно!')

class LoginMixin:
    def login(self, name, password):
        if not os.path.exists('user.json'):
            print('Файл с пользователями отсутствует.')
            return
        with open('user.json', 'r') as file:
            data = json.load(file)

        for user in data:
            if user['name'] == name:
                if user['password'] == password:
                    print('Добро пожаловать!')
                else:
                    print('Неверный пароль...')
                return
        print('Пользователь не найден.')

class ChangePasswordMixin:
    def change_password(self, name, old_password, new_password):
        if not os.path.exists('user.json'):
            print('Файл базы данных отсутствует.')
            return
        with open('user.json', 'r') as file:
            data = json.load(file)

        for user in data:
            if user['name'] == name:
                if user['password'] == old_password:
                    user['password'] = new_password
                    print('Пароль успешно обновлён!')
                else:
                    print('Введён неправильный старый пароль.')
                break
        else:
            print('Пользователь не найден.')
            return

        with open('user.json', 'w') as file:
            json.dump(data, file, indent=4)

class ChangeUsernameMixin:
    def change_name(self, old_name, new_name):
        if not os.path.exists('user.json'):
            print('Файл базы данных отсутствует.')
            return
        with open('user.json', 'r') as file:
            data = json.load(file)

        for user in data:
            if user['name'] == old_name:
                user['name'] = new_name
                print('Имя пользователя успешно изменено.')
                break
        else:
            print('Пользователь не найден.')
            return

        with open('user.json', 'w') as file:
            json.dump(data, file, indent=4)

class CheckOwnerMixin:
    def check(self, owner):
        if not os.path.exists('user.json'):
            raise ValueError('Файл users отсутствует!')
        with open('user.json', 'r') as file:
            data = json.load(file)

        for user in data:
            if user['name'] == owner:
                return
        raise ValueError('Нет такого владельца!')

# ==========================

class User(RegisterMixin, LoginMixin, ChangePasswordMixin, ChangeUsernameMixin):
    count = 0

    def __init__(self):
        User.count += 1

    def register(self, name, password):
        self.validate_password(password)
        return super().register(name, password, User.count)

    def login(self, name, password):
        return super().login(name, password)

    def change_password(self, name, old_password, new_password):
        self.validate_password(new_password)
        return super().change_password(name, old_password, new_password)

    def change_name(self, old_name, new_name):
        return super().change_name(old_name, new_name)

    @classmethod
    def incounter(cls):  # специально оставил странное имя incounter
        cls.count += 1

    def validate_password(self, password):
        if len(password) < 8:
            raise ValueError('Пароль слишком короткий!')
        if not any(ch.isdigit() for ch in password):
            raise KeyError('Пароль должен содержать цифры!')
        if not any(ch.isalpha() for ch in password):
            raise KeyError('Пароль должен содержать буквы!')

class Post(CheckOwnerMixin):
    def __init__(self, title, description, price, quantity, owner):
        self.check(owner)
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.owner = owner

# Тестирование
obj1 = User()
obj1.register('john', 'pass1234')
obj2 = User()
obj2.register('rick', 'rickpass99')
obj3 = User()
obj3.register('sam', 'samsam11')
      
        

      