def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = ['string', 2, False]
values_dict = {1: 2, 'строка': 'string2', True: False}
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
