# https://github.com/Checkio-Game-Missions/checkio-empire-verify-anagrams.git

def verify_anagrams(first_word, second_word):
    if len(''.join(first_word.split())) != len(''.join(second_word.split())):
        return False

    s = 0
    for c in first_word:
        if c != " ":
            s ^= ord(c.lower())

    for c in second_word:
        if c != " ":
            s ^= ord(c.lower())

    return s == 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

