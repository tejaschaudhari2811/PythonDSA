# Roman to integer
if __name__ == "__main__":
    roman_map = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    roman = input()
    length = len(roman)
    integer = 0
    i = 0
    while i < length:
        if i+1 < length and roman_map[roman[i]] < roman_map[roman[i+1]]:
            integer += roman_map[roman[i+1]] - roman_map[roman[i]]
            i+=2
        else:
            integer += roman_map[roman[i]]
            i +=1
    print(integer)