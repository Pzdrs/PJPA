# -*- coding: utf-8 -*-

"""
Úkol 5.
Napište program, který načte soubor large.txt a pro každé dveře vyhodnotí,
zda je možné je otevřít nebo ne. Tedy vyhodnotí, zda lze danou množinu uspořádat
požadovaným způsobem. Výstup z programu uložte do souboru vysledky.txt ve
formátu 1 výsledek =  1 řádek. Na řádek napište vždy počet slov v množině a True
nebo False, podle toho, zda řešení existuje nebo neexistuje.

Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""

from enum import IntEnum


class Letters(IntEnum):
    """
    Přehlednější přístup k datové struktuře
    """
    FIRST = 0
    LAST = 1
    PAIR = 2


def is_chain(words: list[str]) -> tuple[int, bool]:
    """
    Funkce řeší zdali zadaný list je possibly chain
    """
    # Počáteční písmena, koncový písmena, slova končící stejně
    letters = [[Letters.FIRST] * 26 for _ in range(3)]

    for word in words:
        first = ord(word[0]) - ord("a")
        last = ord(word[-1]) - ord("a")

        letters[Letters.PAIR][first] += first == last
        letters[Letters.FIRST][first] += 1
        letters[Letters.LAST][last] += 1

    # Návaznost sekvence
    counter = [0, 0, 0]
    letter_vector = {1: [1, 0, 0], -1: [0, 1, 0]}

    is_chain_sequence = True
    for first, last, pairs in zip(letters[Letters.FIRST], letters[Letters.LAST], letters[Letters.PAIR]):
        if pairs != 0 and (first == last == pairs):
            is_chain_sequence = False
            break

        letter = first - last
        if letter != 0:
            counter = [
                x + y for x, y in
                zip(counter, letter_vector.get(letter, [0, 0, 1]))
            ]

    if counter[Letters.FIRST] <= 1 and counter[Letters.LAST] <= 1 and counter[Letters.PAIR] == 0 and is_chain_sequence:
        pass
    else:
        is_chain_sequence = False

    return len(words), is_chain_sequence


def solve(path: str) -> None:
    """
    Funkce ukládá výsledky o tom zdali dveře jsou chain sekvence
    """

    # Preprocessing
    with open(f"./{path}", "r", encoding="utf8") as raw:
        lines: list[str] = [line.rstrip('\n') for line in raw]
        num_of_doors = int(lines.pop(0))

    line_pointer = 0
    with open("vysledky.txt", "w", encoding="utf8") as result:
        for _ in range(num_of_doors):
            num_of_words = int(lines.pop(line_pointer))

            # Hlavní metoda
            num_of_words, is_chain_sequence = is_chain(
                lines[line_pointer:line_pointer + num_of_words])

            result.write(f"{num_of_words} {is_chain_sequence}\n")

            # Posun na další dveře
            line_pointer += num_of_words


if __name__ == '__main__':
    solve("large.txt")
