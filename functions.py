from random import randint
from math import floor, log
from typing import Iterable

def get_vowel_count(input_string: str):
    """
    Parameters: 
    - input_string (str)

    Output:
    - total number of vowels in input_string (int)
    """
    VOWELS = 'aeiouAEIOU'
    sum = 0
    for character in input_string:
        if character in VOWELS:
            sum += 1
    return sum
    # alternative 1-liner: return sum(1 for character in input_string if character in 'aeiouAEIOU')

def get_random_iterable_element(iterable: Iterable):
    # from random import randint
    # from typing import Iterable (optional, but remove ': Iterable' in parameters if not using)
    """
    Parameters: 
    - iterable (iterbale)
     
    Output:
    - random element from itterable
    """
    return iterable[randint(0, len(iterable) - 1)]

def generate_password(length = 25, complexity = 3):
    """
    Parameters: 
    - length (int) (optional)
    - complexity (int) (optional)
        - 0: only digits
        - 1: as above and lowercase letters
        - 2: as above and uppercase letters
        - 3: as above and special characters: !()-.?[]_'~;:!@#%^&*+=

    Output:
    - password (str)
    """
    password = ""
    DIGITS = "1234567890"
    LOWERCASE_LETTERS = "qwertyuiopasdfghjklzxcvbnm"
    UPPERCASE_LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
    SPECIAL_CHARACTERS = "!()-.?[]_'~;:!@#%^&*+="
    # adding more to SPECIAL_CHARACTERS depending on complexity:
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

def denary_to_binary(denary_number: int, bits = -1):
    # from math import floor, log
    """
    Parameters: 
    - denary_number (int)
    - bits (int) (optional)
     
    Output:
    - binary conversion of denary_number (str)
    """
    binary_number = ''
    start_index = floor(log(denary_number, 2))
    for i in range(start_index, -1, -1):
        if denary_number >= 2 ** i:
            denary_number -= 2 ** i
            binary_number += '1'
        else:
            binary_number += '0'

    if bits > 0:
        if len(binary_number) > bits:
            raise Exception("number too large, increase the bits or lower the number")
        
        leading_0s = bits - len(binary_number)
        binary_number = '0' * leading_0s + binary_number
    
    return binary_number

def denary_to_hexadecimal(denary_number: int, bits = -1):
    # from math import floor, log
    """
    Parameters: 
    - denary_number (int)
    - bits (int) (optional)
     
    Output:
    - hexadecimal conversion of denary_number (str)
    """
    DENARY_TO_HEXADECIMAL = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    hexadecimal_number = ''
    start_index = floor(log(denary_number, 16))
    for i in range(start_index, -1, -1):
        count = 0
        while denary_number >= 16 ** i:
            count += 1
            denary_number -= 16 ** i
        hexadecimal_number += DENARY_TO_HEXADECIMAL[count]

    if bits > 0:
        if len(hexadecimal_number) > bits:
            raise Exception("number too large, increase the bits or lower the number")
        
        leading_0s = bits - len(hexadecimal_number)
        hexadecimal_number = '0' * leading_0s + hexadecimal_number
    
    return hexadecimal_number

def denary_to_base_n(denary_number, base: int, precision = 0, bits = -1):
    # from math import floor, log
    """
    Parameters: 
    - denary_number (int/float) (>= 0)
    - base (int) (>= 2, <= 36)
    - precision (int) (optional) number of digits after the radix point
    - bits (bool/int) (optional)
     
    Output:
    - base n conversion of denary_number (str) (default = integer version)
    """
    # checking if arguments are valid:
    if base > 36 or base < 2:
        raise Exception("base out of range, 2 <= base <= 36")
    if base.is_integer() == False:
        raise ValueError("base must be int")
    if bits <= 0 and bits != -1:
        raise Exception("bits must be >= 0, or -1 for default bits")

    # defining the conversion dictionary (from 0: '0' to 35: 'z'):
    DENARY_TO_BASE_n = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z' } 

    base_n_number = ''
    start_exponent = floor(log(denary_number, base)) # the power of n to start subtracting

    for i in range(start_exponent, -precision - 1, -1): # i decrements to decrease the power of n being subtracted
        count = 0
        if i == -1: # assigns radix point if applicable
            base_n_number += '.'
        while denary_number >= base ** i:
            count += 1
            denary_number -= base ** i
        base_n_number += DENARY_TO_BASE_n[count]

    # reduces number of significant figures 
    if precision < 0:
        base_n_number += '0' * -precision

    # adding leading 0s if applicable:
    if precision > 0: # accounting for the radix point
        length = len(base_n_number) - 1
    else:
        length = len(base_n_number)
    if length > bits and bits != -1: # checking if number can fit within allocated bits
        raise Exception("number too large, increase the bits or lower the input number")
    leading_0s = bits - length
    base_n_number = '0' * leading_0s + base_n_number

    return base_n_number

# asserts:

assert get_vowel_count("Hello") == 2
assert get_vowel_count("Did you ever hear the tragedy of Darth Plagueis the Wise?") == 19

assert get_random_iterable_element([4, "testing", ['a', 'b']]) in [4, "testing", ['a', 'b']]

assert denary_to_binary(19) == "10011"
assert denary_to_binary(19, 8) == "00010011"

assert denary_to_hexadecimal(82014) == "1405e"
assert denary_to_hexadecimal(430, 5) == "001ae"

assert denary_to_base_n(511, 7) == '1330'
assert denary_to_base_n(511, 7, 4) == '1330.0000'
assert denary_to_base_n(511, 7, 0, 9) == '000001330'
assert denary_to_base_n(511, 7, 3, 9) == '001330.000'
assert denary_to_base_n(511, 7, -2) == '1300'

