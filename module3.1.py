calls = 0


def count_calls(func):
    global calls

    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        return func(*args, **kwargs)

    return wrapper


@count_calls
def string_info(string):
    return (len(string), string.upper(), string.lower())


@count_calls
def is_contains(string, list_to_search):
    string = string.lower()
    return any(s.lower() == string for s in list_to_search)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))  # False

print(calls)
