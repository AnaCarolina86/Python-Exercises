def is_pangram(sentence):
    new_sentence = sentence.lower()
    variable = 97
    while variable < 123:
        if new_sentence.find(chr(variable)) < 0:
            return False
        variable += 1
    return True
