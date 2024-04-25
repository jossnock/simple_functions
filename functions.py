def get_count(sentence):
    VOWELS = 'aeiouAEIOU'
    sum = 0
    for character in sentence:
        if character in VOWELS:
            sum += 1
    return sum
    # return sum(1 for character in sentence if character in 'aeiouAEIOU')

def assert_all_functions():
    assert get_count("Hello") == 2
    DPTW = """
    Did you ever hear the tragedy of Darth Plagueis the Wise?\n
    I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis... was a Dark Lord of the Sith so powerful and so wise, he could use the Force to influence the midi-chlorians... to create... life. He had such a knowledge of the dark side, he could even keep the ones he cared about... from dying.\n
    The dark side of the Force is a pathway to many abilities... some consider to be unnatural.\n
    "He became so powerful, the only thing he was afraid of was... losing his power. Which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew. Then his apprentice killed him in his sleep. It's ironic. He could save others from death, but not himself.\n
    """
    assert get_count(DPTW) == 228
assert_all_functions()