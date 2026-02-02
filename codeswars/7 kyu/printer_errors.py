def printer_error(s):
    abc = 'abcdefghijklm'
    s_list = [letter for letter in s if letter in abc]
    
    return f'{len(s) - len(s_list)}/{len(s)}'
