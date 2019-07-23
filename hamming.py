
def distance(strand_a, strand_b):
    counter: int = 0
    count = 0
    if len(strand_a) == len(strand_b):
        while count < len(strand_b):
            if strand_a[count] != strand_b[count]:
                counter += 1
            count += 1

    if len(strand_a) != len(strand_b):
        raise ValueError(".+")
        
    return counter




