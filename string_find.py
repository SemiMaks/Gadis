# Метод find() отыскивает заданную подстроку,
# если подстрока не найдена метод возвращает -1

def find_string():
    string = 'Восемьдесят семь лет назад'
    position = string.find('семь')
    if position != -1:
        print('Слово "семь" найдено в индексной позиции', position)
    else:
        print('Слово "семь" не найдено.')

# Метод replace() позволяет найти подстроку и заменить новой


def replace_string():
    string = 'Сто дней назад'
    print(string)
    new_string = string.replace('дней', 'лет')
    print(new_string)


find_string()
replace_string()
