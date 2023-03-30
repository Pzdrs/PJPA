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
import math
import time


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
    time_taken = []
    for i, word in enumerate(words):
        print(f'{i}/{len(words)}')
        t1 = time.time_ns()
        _words = list(words)
        _words.remove(word)
        for _word in _words[:]:
            if word[-1] == _word[0]:
                _words.remove(_word)
                word = _word
        t2 = time.time_ns()
        took = (t2 - t1) / int(1e6)
        time_taken.append(took)
        print(f'took {math.floor(took)}ms')
        print(f'estimated {math.floor(((sum(time_taken) / len(time_taken)) * (len(words) - i + 1)) / 60000)}min left')
        if len(_words) == 0:
            return len(words), True

    return len(words), False


def solve_recursion(door):
    def find_next_link(word: str, _words: list[str]):
        if len(_words) == 0:
            return True
        for _word in _words:
            if word[-1] == _word[0]:
                _words.remove(_word)
                return find_next_link(_word, _words)
        return False

    for door_word in door:
        word_list = list(door)
        word_list.remove(door_word)
        if find_next_link(door_word, word_list):
            return len(door), True
    return len(door), False


if __name__ == '__main__':
    data = load('test_limit_positive.txt')
    for door in data:
        print(solve(door))
