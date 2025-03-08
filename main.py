def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """

    # check if within bounds first
    if not 1 <= num <= 3999:
        # throw error
        raise ValueError("invalid num")

    # set up arrays
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["", "M", "MM", "MMM"]

    # calc each
    thous = num // 1000
    hund = (num % 1000) // 100
    ten = (num % 100) // 10
    singles = num % 10

    # get numeral for each
    thousRoman = thousands[thous]
    hundRoman = hundreds[hund]
    tenRoman = tens[ten]
    singleRoman = ones[singles]

    # combine strings
    roman_numeral = thousRoman
    roman_numeral = roman_numeral + hundRoman
    roman_numeral = roman_numeral + tenRoman
    roman_numeral = roman_numeral + singleRoman

    return roman_numeral

