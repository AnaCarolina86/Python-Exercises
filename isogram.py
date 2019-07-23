def is_isogram(string):
    new_string = string.lower()
    n = 0
    t = len(new_string)
    while n < t:
        if new_string[n].isalpha() and new_string.count(new_string[n]) > 1:
            return False
        n += 1
    return True

