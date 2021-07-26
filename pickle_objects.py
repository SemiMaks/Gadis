# Эта программа демонстрирует консервацию объектов.

import pickle


def main():
    again = 'д'

    output_file = open('info.dat', 'wb')

    # Получать данные, пока пользователь не решит прекратить
    while again.lower() == 'д':
        save_data(output_file)

        # Пользователь желает ввести ещё данные?
        again = input('Желаете ввести данные ещё? (д/н): ')

    output_file.close()
    print('Еще операция')

    with open('info.dat', 'rb') as f:
        data = pickle.load(f)
        print(data)


# Функция save_data получает данные о человеке,
# сохраняет их в словарь и затем консервирует
# словарь в указанном файле
def save_data(file):
    # Создать пустой словарь
    person = {}
    # Получить данные о человеке и сохранить
    # их в словаре
    person['имя'] = input('Введите имя: ')
    person['возраст'] = input('Введите возраст: ')
    person['масса'] = float(input('Введите вес: '))

    # Законсервировать словарь
    pickle.dump(person, file)


main()
