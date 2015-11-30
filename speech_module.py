#https://github.com/Checkio-Game-Missions/checkio-empire-speech-module.git

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"

def tell_number(number):
    if number == 0:
        return "zero"

    def do_number(number):
        th = h = -1
        t = tn = o = None

        n = abs(number)

        while n > 0:
            if n >= 1000:
                n -= 1000
                th += 1
            elif n >= 100:
                n -= 100
                h += 1
            elif n >= 20:
                x = n/10
                t = OTHER_TENS[int(x)-2]
                n -= int(x) * 10
            elif 10 <= n < 20:
                tn = SECOND_TEN[int(n % 10)]
                break
            else:
                o = FIRST_TEN[int(n)-1]
                n = 0

        return th, h, t, tn, o
        
        
    th, h, t, tn, o = do_number(number)

    ret = []
    if number < 0:
        ret += ["minus"]
    
    if th >= 0:
        if th > 9:
            z = do_number(th+1)

            if z[1] >= 0:
                ret += [FIRST_TEN[z[1]], HUNDRED]

            if z[2] != None:
                ret.append(z[2])

            if z[3] != None:
                ret.append(z[3])

            if z[4] != None:
                ret.append(z[4])
            
            ret.append(THOUSAND)
        else:
            ret += [FIRST_TEN[th], THOUSAND]

    if h >= 0:
        ret += [FIRST_TEN[h], HUNDRED]

    if t != None:
        ret.append(t)

    if tn != None:
        ret.append(tn)

    if o != None:
        ret.append(o)

    return ' '.join(ret)

if __name__ == '__main__':
    #assert tell_number(4) == 'four', "1st example"
    #assert tell_number(133) == 'one hundred thirty three', "2nd example"
    #assert tell_number(12) == 'twelve', "3rd example"
    #assert tell_number(101) == 'one hundred one', "4th example"
    #assert tell_number(212) == 'two hundred twelve', "5th example"
    #assert tell_number(40) == 'forty', "6th example"
    assert tell_number(-1000) == 'minus one thousand', "6th example"
    #assert not tell_number(212).endswith(' '), "Dont forget strip whitespaces at the end of string"

    #assert tell_number(-133) == 'minus one hundred thirty three', "Minus"
    #assert tell_number(0) == 'zero', "Zero"

    #assert tell_number(42000) == 'forty two thousand', "42 many"
    #assert (tell_number(-999999) ==
            #"minus nine hundred ninety nine thousand nine hundred ninety nine"), "Abyss"

    print("Earn cool rewards by using the 'Check' button!")
