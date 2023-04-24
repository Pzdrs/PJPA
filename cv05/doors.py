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

import os


def get_word_degrees(words: list[str]) -> dict[str, tuple[int, int]]:
    degrees = {}
    for word in words:
        safe_word = word.strip()
        leading_letter = safe_word[0]
        trailing_letter = safe_word[-1]
        if leading_letter not in degrees:
            degrees[leading_letter] = (0, 0)
        if trailing_letter not in degrees:
            degrees[trailing_letter] = (0, 0)
        in_degree, out_degree = degrees[leading_letter]
        degrees[leading_letter] = (in_degree, out_degree + 1)
        in_degree, out_degree = degrees[trailing_letter]
        degrees[trailing_letter] = (in_degree + 1, out_degree)
    return degrees


def is_eulerian_path(degrees: dict[str, tuple[int, int]]) -> bool:
    odd_degree_count = 0
    for in_degree, out_degree in degrees.values():
        if abs(in_degree - out_degree) == 1:
            odd_degree_count += 1
        elif in_degree != out_degree:
            return False
    return odd_degree_count <= 2


def solve(file_path: str) -> list[str]:
    if not os.path.isfile(file_path):
        return []
    door_data = []
    with open(file_path, "r", encoding="utf-8") as file:
        door_count = int(file.readline().strip())
        for _ in range(door_count):
            word_count = int(file.readline().strip())
            words = [file.readline().strip() for _ in range(word_count)]
            degrees = get_word_degrees(words)
            door_data.append(f'{word_count} {is_eulerian_path(degrees)}')
    return door_data


if __name__ == '__main__':
    door_data = solve("./large.txt")
    with open("./vysledky.txt", "w", encoding="utf-8") as file:
        for result in door_data:
            file.write(f'{result}\n')
