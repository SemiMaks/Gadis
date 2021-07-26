# Эта программа демонстрирует различные операции над множествами

baseball = set(['Джоди', 'Кармен', 'Аида', 'Алиция'])
basketball = set(['Эва', 'Кармен', 'Алиция', 'Сара'])


def print_p():
    print('-' * 25)


# Показать членов бейсбольной команды
print('-' * 25)
print('Члены бейсбольной команды: ')
for name in baseball:
    print(name)

# Показать членов баскетбольной комнады
print_p()
print('Члены баскетбольной команды: ')
for name in basketball:
    print(name)

# Продемонстрировать пересечение
print_p()
print('Те, кто играют в бейсбол и в баскетбол: ')
for name in baseball.intersection(basketball):
    print(name)

# Продемонстрировать объединение
print_p()
print('Эти люди играют в одну или обе игры: ')
for name in baseball.union(basketball):
    print(name)

# Продемонстрировать разность между бейсболом и баскетболом:
print_p()
print('Эти люди играют в бейсбол, но не баскетбол:')
for name in baseball.difference(basketball):
    print(name)

# Продемонстрировать разность между бейсболом и баскетболом:
print_p()
print('Эти люди играют в баскетбол, но не бейсбол:')
for name in basketball.difference(baseball):
    print(name)

# Прдемонстрировать симметричную разность:
print_p()
print('Эти люди играют в одну из игр, но не в обе: ')
for name in baseball.symmetric_difference(basketball):
    print(name)
