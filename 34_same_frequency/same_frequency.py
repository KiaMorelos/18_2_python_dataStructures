def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    make_str_one = str(num1)
    make_str_two = str(num2)

  
    make_dict_one = { digit: make_str_one.count(digit) for digit in make_str_one }

    make_dict_two = { digit: make_str_two.count(digit) for digit in make_str_two }


    return make_dict_one == make_dict_two