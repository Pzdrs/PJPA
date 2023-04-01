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


def load(file_path: str) -> tuple[tuple, ...]:
    """
    Loads a file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        doors = []
        for _ in range(int(file.readline())):
            words = []
            for _ in range(int(file.readline())):
                words.append(file.readline().strip())
            doors.append(tuple(words))
        return tuple(doors)


def solve(words: tuple[str]) -> tuple[int, bool]:
    """
    Determines if a chain can be constructed using recursion
    """
    for word in words:
        _words = list(words)
        _words.remove(word)
        for _word in _words[:]:
            if word[-1] == _word[0]:
                _words.remove(_word)
                word = _word
        if len(_words) == 0:
            return len(words), True

    return len(words), False


if __name__ == '__main__':
    data = load('large.txt')
    for door in data:
        with open('vysledky.txt', 'a', encoding='utf-8') as result_file:
            result = solve(door)
            result_file.write(f'{result[0]} {result[1]}\n')
