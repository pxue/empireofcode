# https://github.com/Empire-of-Code-Puzzles/checkio-empire-index-power

def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if len(array) <= n:
        return -1
    
    return array[n]**n
