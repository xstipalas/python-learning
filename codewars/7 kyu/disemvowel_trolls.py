def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    translation_table = str.maketrans('', '', vowels)
    
    return string_.translate(translation_table)
