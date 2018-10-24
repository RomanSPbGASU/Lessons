def authenticate(locked_func):
    right_pass = "1234qwerty"
    password = input("Введите пароль: ")
    if password == right_pass:
        return locked_func
    else:
        print("Пароль неверный. Доступ к функции func() закрыт")


@authenticate
def func():
    print("Доступ к функции func() открыт!")


if __name__ == "__main__":
    if func:
        func()
