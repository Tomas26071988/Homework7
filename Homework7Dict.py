my_dict = {'Artem': 1988, 'Natalya': 1991, 'Arseny': 2015, 'Marya': 2019}
print(my_dict['Marya'])
my_dict['Ivan'] = 1985
print(my_dict)
my_dict.update({'Sveta': 1962, 'Valera': 1963})
del my_dict['Artem']        # удалить ключ
print(my_dict.items())     # вывести значение от этого удаленного ключа
print(my_dict)
