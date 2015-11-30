#I 1 (unus)
#V 5 (quinque)
#X 10 (decem)
#L 50 (quinquaginta)
#C 100 (centum)
#D 500 (quingenti)
#M 1,000 (mille)

#https://github.com/Empire-of-Code-Puzzles/checkio-empire-roman-numerals

def roman(number):
    # up to 3999, check number places

    R = []
    while number > 0:
        if number >= 1000:
            number -= 1000
            R.append("M")
        elif number >= 500:
            number -= 500 
            R.append("D")
        elif number >= 100:
            number -= 100
            R.append("C")
        elif number >= 50:
            number -= 50
            R.append("L")
        elif number >= 10:
            number -= 10
            R.append("X")
        elif number >= 5:
            number -= 5
            R.append("V")
        else:
            number -= 1
            R.append("I")

    ret = ''.join(R)
    ret = ret.replace("VIIII", "IX")
    ret = ret.replace("IIII", "IV")

    ret = ret.replace("LXXXX", "XC")
    ret = ret.replace("XXXX", "XL")

    ret = ret.replace("DCCCC", "CM")
    ret = ret.replace("CCCC", "CD")

    print ret
    return ret


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert roman(6) == 'VI', '6'
    assert roman(76) == 'LXXVI', '76'
    assert roman(499) == 'CDXCIX', '499'
    assert roman(3888) == 'MMMDCCCLXXXVIII', '3888'
    assert roman(10) == 'X', '10'
    print("Earn cool rewards by using the 'Check' button!")

