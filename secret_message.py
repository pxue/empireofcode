#https://github.com/Empire-of-Code-Puzzles/checkio-empire-secret-message

def find_message(text):
    """Find a secret message"""
    
    return "".join([x for x in text if x.istitle()])
