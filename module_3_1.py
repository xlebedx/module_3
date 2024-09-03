calls = 0


def count_calls():
    global calls
    calls += 1
    return calls - 1


def string_info(string: str):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: list):
    count_calls()
    lower_string = string.lower()
    lower_list = [element.lower() for element in list_to_search]
    if lower_string in lower_list:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Capygeddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('Suburban', ['cycle', 'uRbaN', 'SuBuRbAn', ]))
print(calls)
