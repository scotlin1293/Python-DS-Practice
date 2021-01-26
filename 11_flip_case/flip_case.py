def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    res = ""
    for ltr in phrase:
        if ltr.lower() == to_swap.lower() or ltr.upper() == to_swap.upper():
            ltr = ltr.swapcase()
        res += ltr
    return res

print(flip_case('FoRk', 'f'))
