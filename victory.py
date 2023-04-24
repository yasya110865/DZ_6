
import random
import copy
def victory(n, date):

    date_dict = {
    'Альберт Эйнштейн':'14.03.1879'

    }
    new_format_date = ['четырнадцатое марта 1879 года']

    date_dict_1 = date_dict.copy()

    new_format_dict = dict(zip(list(date_dict_1.keys()), new_format_date))

    sample_list = random.sample(list(date_dict.keys()), n)
    for sample in sample_list:
        date = date
        if date == date_dict[sample]:
            print('Верно!')
            return True
        else:
            print(f'Верный ответ: {new_format_dict[sample]}')
            return False
a = victory(1,'123')
print(a)
