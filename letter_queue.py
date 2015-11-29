# https://github.com/Empire-of-Code-Puzzles/checkio-empire-letter-queue
def letter_queue(commands):
    q = []
    for c in commands:
        if "POP" in c:
            q = q[1:]
        elif "PUSH" in c:
            q.append(c[-1])

    return "".join(q)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(("PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T")) == "DOT", "dot example"
    assert letter_queue(("POP", "POP")) == "", "Pop, Pop, empty"
    assert letter_queue(("PUSH H", "PUSH I")) == "HI", "Hi!"
    assert letter_queue(()) == "", "Nothing"

    print("All done? Earn rewards by using the 'Check' button!")
