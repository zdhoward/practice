roman_numerals = [
    (1000, "M"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def main():
    int_to_roman(444)
    roman_to_int("CDXLIV")


def int_to_roman(num):
    if num <= 1000:
        start = num
        roman = ""
        while num > 0:
            for digit, numeral in roman_numerals:
                if num >= digit:
                    roman += numeral
                    num -= digit
    else:
        print("Number must be less than or equal to 1000")
    print(start, "is", roman)
    return roman


def roman_to_int(roman):
    start = roman
    num = 0
    while roman != "":
        for digit, numeral in roman_numerals:
            if len(roman) >= 2:
                if roman[0] == "C" and roman[1] == "D":
                    num += 400
                    roman = roman[2:]
                elif roman[0] == "X" and roman[1] == "L":
                    num += 40
                    roman = roman[2:]
                elif roman[0] == "I" and roman[1] == "V":
                    num += 4
                    roman = roman[2:]
            elif len(roman) >= 1:
                for digit, numeral in roman_numerals:
                    if roman[0] == numeral:
                        num += digit
                        roman = roman[1:]
    print(start, "is", num)
    return num


if __name__ == "__main__":
    main()
