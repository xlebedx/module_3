def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = ['string', 2, False]
values_dict = {'a': 2, 'b': 'string2', 'c': False}
values_list_2 = [54.32, 'Строка']
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
print_params(b=25)
print_params(c=[1, 2, 3])

