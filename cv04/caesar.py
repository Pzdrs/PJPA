"""
Vytvorte funkce encrypt a decrypt pro Caesarovu sifru.
Kompletni zadani v elearningu.
"""
LOWER_BOUNDS = (ord('a'), ord('z'))
UPPER_BOUNDS = (ord('A'), ord('Z'))


def shift(letter: chr, offset: int) -> chr:
    """
    Shifts a letter in the ASCII table by an offset
    """
    # MOJE PUVODNI RESENI, CHATGPT TO MA MNOHEM LEPSI NGL
    # new_ascii = ord(letter) + offset
    # if letter.islower():
    #     if new_ascii > LOWER_BOUNDS[1]:
    #         new_ascii = LOWER_BOUNDS[0] + (abs(new_ascii - LOWER_BOUNDS[1]) - 1)
    #     if new_ascii < LOWER_BOUNDS[0]:
    #         new_ascii = LOWER_BOUNDS[1] - (abs(new_ascii - LOWER_BOUNDS[0]) - 1)
    # elif letter.isupper():
    #     if new_ascii > UPPER_BOUNDS[1]:
    #         new_ascii = UPPER_BOUNDS[0] + (abs(new_ascii - UPPER_BOUNDS[1]) - 1)
    #     if new_ascii < UPPER_BOUNDS[0]:
    #         new_ascii = UPPER_BOUNDS[1] - (abs(new_ascii - UPPER_BOUNDS[0]) - 1)
    # return chr(new_ascii)
    if letter.islower():
        base = ord('a')
    elif letter.isupper():
        base = ord('A')
    else:
        return letter
    shifted_ascii = (ord(letter) - base + offset) % 26 + base
    return chr(shifted_ascii)


def encrypt(word: str, offset: int) -> str:
    """
    :param word - slovo k zasifrovani
    :param offset - znakovy posun
    :return: zasifrovane slovo
    """
    cipher = []
    for letter in word:
        if not letter.isalpha():
            cipher.append(letter)
            continue
        cipher.append(shift(letter, offset))
    return ''.join(cipher)


def decrypt(word: str, offset: int) -> str:
    """
    :param word - zasifrovane slovo
    :param offset - znakovy posun
    :return: desifrovane slovo
    """
    return encrypt(word, -offset)
