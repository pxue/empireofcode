import string
Z = 27 # xor of ord values a-z
def check_pangram(text):

    s = set([ord(ch) for ch in text.lower() if 97 <= ord(ch) <= 122])
    return reduce(lambda x,y: x^y, s) == Z


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"

    print("All done? Earn rewards by using the 'Check' button!")
