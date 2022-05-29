def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newStr = ""
   
    for letter in phrase:
        if letter == to_swap:
            newStr += letter.swapcase()
        elif letter == to_swap.swapcase():
            newStr += letter.swapcase()
        else:
            newStr += letter
    
    return newStr
