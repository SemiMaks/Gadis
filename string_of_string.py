# Программа позволяет находить подстроку внутри других строковых данных.

def main():
    filename = input('Введите название файла: ')
    if filename.endswith('.txt'):
        print('Это имя текстового файла.')
    elif filename.endswith('.py'):
        print('Это название исходного файла Python.')
    elif filename.endswith('.doc'):
        print('Это имя документа текстового редактора.')
    else:
        print('Неизвестный тип файла.')

main()
