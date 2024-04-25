def get_vowel_count(input_string):
    """
    Parameters: 
    - input_string (str)

    Output:
    - int - total number of vowels in input_string
    """
    VOWELS = 'aeiouAEIOU'
    sum = 0
    for character in input_string:
        if character in VOWELS:
            sum += 1
    return sum
    # return sum(1 for character in input_string if character in 'aeiouAEIOU')

def get_random_iterable_element(iterable):
    from random import randint
    return iterable[randint(0, len(iterable) - 1)]

def generate_password(length = 25, complexity = 3):
    """
    Parameters: 
    - length (int)
    - complexity (int)
        - 0 means only digits
        - 1 means as above and lowercase letters
        - 2 means as above and uppercase letters
        - 3 means as above and special characters: !()-.?[]_'~;:!@#%^&*+=

    Output:
    - str - password
    """
    password = ""
    DIGITS = "1234567890"
    LOWERCASE_LETTERS = "qwertyuiopasdfghjklzxcvbnm"
    UPPERCASE_LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
    SPECIAL_CHARACTERS = "!()-.?[]_'~;:!@#%^&*+="
    if complexity == 0:
        CHARACTERS = DIGITS
    if complexity == 1:
        CHARACTERS = DIGITS + LOWERCASE_LETTERS
    if complexity == 2:
        CHARACTERS = DIGITS + LOWERCASE_LETTERS + UPPERCASE_LETTERS
    if complexity >= 3:
        CHARACTERS = DIGITS + LOWERCASE_LETTERS + UPPERCASE_LETTERS + SPECIAL_CHARACTERS
    for i in range(length):
        password += get_random_iterable_element(CHARACTERS)
    return password

def assert_all_functions():
    assert get_vowel_count("Hello") == 2
    assert get_vowel_count("Did you ever hear the tragedy of Darth Plagueis the Wise?") == 19
    assert get_random_iterable_element([4, "testing", ['a', 'b']]) in [4, "testing", ['a', 'b']]
assert_all_functions()