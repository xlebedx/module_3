calls = 0


def count_calls(calls):
    pass


def string_info(string: str):
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: list):
    lower_string = string.lower()
    lower_list = [element.lower() for element in list_to_search]
    if lower_string in lower_list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
