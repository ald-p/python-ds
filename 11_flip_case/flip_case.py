def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    new_phrase_lst = []
    for idx, ltr in enumerate(phrase.lower()):
        if ltr == to_swap.lower():
            new_phrase_lst.append(phrase[idx].swapcase())
        else:
            new_phrase_lst.append(phrase[idx]) 

    return "".join(new_phrase_lst)        