# Применив метод pickle

import pickle

phonebook = {'Крис': '111-111-111',
             'Эллис': '222-222-222',
             'Кэт': '333-333-333'}

with open('phonebook.pickle', 'wb') as f:
    pickle.dump(phonebook, f)

with open('phonebook.pickle', 'rb') as f:
    data_new = pickle.load(f)

print(data_new)
