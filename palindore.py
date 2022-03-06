from itertools import combinations


def check_palindorme_or_not(str_char):
    reverse_str = str_char.lower()[::-1]
    print(f"{reverse_str}====={str_char.lower()}")
    return reverse_str == str_char.lower()


def character_palindrome_check(str_char):
    if len(str_char) == 1:
        return False

    if check_palindorme_or_not(str_char):
        return True

    else:
        all_combinations = sum([list(map(list, combinations(str_char, i)))
                                for i in range(len(str_char) + 1)], [])
        for combo in all_combinations:
            if len(combo) >= len(str_char)-1:
                if check_palindorme_or_not(''.join(combo)):
                    return True
        return False


if __name__ == '__main__':
    # print("Madhu"[::-1])
    str_char = input("Please enter the character:")
    print(character_palindrome_check(str_char))
