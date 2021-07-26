# Вызов встроенной функции set для
# создания пустого множества.

myset = set()
print(type(myset))
myset = set(['a', 'b', 'g', 'u'])
print(myset)
print('Длина сэта -', len(myset))

myset2 = set()
myset2.add(1)
myset2.add(2)
myset2.add(3)
print(myset2)

myset.update(['1', '2', '3'])
print(myset)

myset.update(myset2)
print(myset)

# myset.remove('u')
myset.discard('u')
print(myset)

myset.clear()
print(myset)

for key in myset2:
    print(key)

if 1 in myset2:
    print('1 входит в множество myset2')

if 4 not in myset2:
    print('4 не входит в множество myset2')

myset3 = set([1, 2, 3, 4, 5])
myset4 = set([4, 5, 6, 7, 8])
print(myset3, myset4)

# Объединение множеств:
myset5 = myset3 | myset4    # myset3.union(myset4
print('Объединение множеств', myset5)

# Пересечение множеств:
myset6 = myset3 & myset4    # myset3.intersection(myset4)
print('Пересечение множеств: ', myset6)

# Разность множест:
myset7 = myset3 - myset4    # myset3.difference(myset4)
print('Разность множеств: ', myset7)

# Симметричная разнасть множеств:
myset8 = myset3 ^ myset4    # myset3.symmetric_difference(myset4)
print('Симметричная разность множеств: ', myset8)

# Подмножества и надмножества
print(myset <= myset3) # myset.issubset(myset3) - подмножество True
print(myset3 >= myset3) # myset3.issuperset(myset) - надмножество True
print(myset4 <= myset3) # False



