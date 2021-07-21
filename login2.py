# Функция get_login_name принимает имя, фамилию и
# идентификационный номер в качестве аргументов.
# Она возвращает имя для входа в систему.

def get_login_name(first, last, idnumber):
    # Получить первые три буквы имени.
    # Если длина менее 3х букв, то
    # срез вернёт всё имя целиком.
    set1 = first[:3]

    # Получить первые три буквы фамилии.
    # Если длина фамилии меньше 3х букв, то
    # срез вернёт всю фамилию целиком.
    set2 = last[:3]

    # Получить последние три буквы идентификатора.
    # Если длина идентификатора меньше 3х символов,
    # срез вернёт весь идентификатор целиком.
    set3 = idnumber[:3]

    # Собрать воедино наборы символов
    login_name = set1 + set2 + set3

    # Вернуть имя для входа в систему
    return login_name


# Функция valid_password принимает пароль в качестве
# аргумента и возвращает истину/ложь, сообщая о его
# допустимости. Допустим пароль: не менее 7 символов,
# минимум один символ в верхнем регистре, один в нижнем
# и одну цифру.


def valid_passsword(password):
    # Назначить булевым переменным False.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Приступаем к валидации.
    if len(password) >= 7:
        correct_length = True
        # Проанализировать каждый символ и выставить
        # соответствующий флаг, когда символ найден.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
        # Определить все ли требования к паролю выполнены.
        # Если Да, то назначить is_valed значение True.
        # В противном случае назначить is_valid значение False.
        if correct_length and has_uppercase and \
                has_lowercase and has_digit:
            is_valid = True
        else:
            is_valid = False

        # Вернуть переменную is_valid
        return is_valid
