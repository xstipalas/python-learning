import string

def rot13(message):
    STEP = 13
    
    ascii = string.ascii_lowercase + string.ascii_uppercase
    ascii_shift = string.ascii_lowercase[STEP:] + string.ascii_lowercase[:STEP] + string.ascii_uppercase[STEP:] + string.ascii_uppercase[:STEP]
    
    table = str.maketrans(ascii, ascii_shift)
    
    return message.translate(table)
