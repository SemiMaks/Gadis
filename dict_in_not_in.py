# Создаем словарь и проверяем вхождение в него какого-либо значения

def main():
    # Создаём и печатаем словарь
    phone_book = {'Крис': '555-555-000', 'Элли': '555-555-111', 'Аня': '555-555-222'}
    print('Вновь созданный словарь: ', phone_book)

    # Проверяем вхождение ключей в словарь
    if 'Крис' in phone_book:
        print('Крис - ', phone_book['Крис'])
    if 'Джуди' not in phone_book:
        print('А вот Джуди в словаре нет.')

    # Добавляем/заменяем (если есть такой ключ- значение обновится) в словарь Джуди
    phone_book['Джуди'] = '555-555-333'
    if 'Джуди' in phone_book:
        print('А теперь есть. Джуди -', phone_book['Джуди'])
    print(phone_book)

    # Теперь удалим запись 'Джуди' в словаре
    # Предварительно проверив его наличие,
    # чтобы предотвратить вызов исключения KeyError.
    if 'Джуди' in phone_book:
        del phone_book['Джуди']
    else:
        print('Такого ключа в словаре нет.')
    print('После удаления записи Джуди: ', phone_book)
    len_pb = len(phone_book)
    print('Количество пар ключ:значение в phone_book: ', len_pb)

    for key in phone_book:
        print(key, phone_book[key])

    # Некоторые словарные методы
    # Печатаем все ключи
    print(phone_book.keys())
    # Печатаем все значения
    print(phone_book.values())
    # Печатаем всё- и ключи и значения, т.е. получаем словарное представление
    # (особого типа последовательность)
    print(phone_book.items())
    # Печатаем значение Мэта, если такого нет - то значение по умолчанию(запись не найдена)
    print(phone_book.get('Мэт', 'запись не найдена'))
    print(phone_book.get('Крис', 'Записи нет'))

    # Перебор кортежей впоследовательности применив цикл
    for key, value in phone_book.items():
        print(key, value)

    for key in phone_book.keys():
        print(key)

    for key in phone_book:
        print('Словарь phone_book, ключ: ', key)

    phone_num = phone_book.pop('Эллис', 'Нет такого значения, увы')
    print(phone_num)


main()
