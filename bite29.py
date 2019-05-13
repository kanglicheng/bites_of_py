def get_index_different_char(chars):
    alnum_count, other_count = 0, 0
    alnum_index, other_index = 0, 0
    for i, c in enumerate(chars):
        if str(c).isalnum():
            alnum_count += 1
            alnum_index = i
        else:
            other_count += 1
            other_index = i
    return alnum_index if alnum_count == 1 else other_index

print(get_index_different_char(['A', 'f', '.', 'Q', 2]))
