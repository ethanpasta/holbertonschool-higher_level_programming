#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return None
    dic_s = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    dic_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    num = 0
    while i < len(roman_string):
        if i < len(roman_string) - 1:
            str1 = roman_string[i] + roman_string[i + 1]
        else:
            str1 = roman_string[i]
        if str1 in dic_s.keys():
            num += dic_s[str1]
            i += 2
        else:
            num += dic_n[roman_string[i]]
            i += 1
    return num
