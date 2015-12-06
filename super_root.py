import math

mod = 0

def f_prime(x):
    return x**x * (math.log1p(x) + 1)

def f(x):
    return x**x - mod

# newton's method
def super_root(number):
    p = 0.0001 # precision
    x = math.log1p(number)

    global mod
    mod = float(number)

    while True:
        x1 = x - f(x)/f_prime(x)
        t = abs(x1**x1 - number)
        if t < p:
            x = x1
            break
        x = x1

    return x

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        print p - number
        if number - 0.001 < p < number + 0.001:
            return True
        return False

    #assert check_result(super_root, 4), "Square"
    #assert check_result(super_root, 27), "Cube"
    #assert check_result(super_root, 81), "Eighty one"
    assert check_result(super_root, 9999999999), "FUCK"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")

