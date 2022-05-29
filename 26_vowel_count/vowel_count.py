def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = {"a", "e", "i", "o", "u"}
    downed_phrase = phrase.lower()

    vowels_in_phrase= {ltr: downed_phrase.count(ltr) for ltr in downed_phrase if ltr in vowels}
    
    return vowels_in_phrase