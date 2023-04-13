# -*- coding: utf-8 -*-

"""
Úkol 6.
Vaším dnešním úkolem je vytvořit program, který o zadaném textu zjistí některé
údaje a vypíše je na standardní výstup. Hlavním smyslem cvičení je procvičit
si práci s regulárními výrazy, takže pro plný bodový zisk je nutné použít k
řešení právě tento nástroj.

Program musí pracovat s obecným textem, který bude zadaný v souboru. Jméno
souboru bude zadáno jako vstupní parametr funkce main, která by měla být
vstupním bodem programu. Samozřejmě, že funkce main by neměla řešit problém
kompletně a měli byste si vytvořit další pomocné funkce. Můžete předpokládat,
že soubor bude mít vždy kódování utf-8 a že bude psaný anglicky, tedy jen
pomocí ASCII písmen, bez české (či jiné) diakritiky.

Konkrétně musí program zjistit a vypsat:

1. Počet slov, která obsahují nejméně dvě samohlásky (aeiou) za sebou. Například
slovo bear.

2. Počet slov, která obsahují alespoň tři samohlásky - například slovo atomic.

3. Počet slov, která mají šest a více znaků - například slovo terrible.

4. Počet řádků, které obsahují nějaké slovo dvakrát.

Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""
import re

REGEX_1 = re.compile(r'\b\w*[aeiyou]{2,}\w*\b', re.IGNORECASE)
REGEX_2 = re.compile(r'\b(?:\w*[aeiyouAEIYOU]){3,}\w*\b', re.IGNORECASE)
REGEX_3 = re.compile(r'\w{6,}', re.IGNORECASE)
REGEX_4 = re.compile(r'\b(\w+)\b.*\b\1\b', re.IGNORECASE)

REGEXES = (REGEX_1, REGEX_2, REGEX_3, (REGEX_4, False))


def main(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contents = file.read()
        for regex in REGEXES:
            if isinstance(regex, tuple):
                matches = re.findall(regex[0], contents)
                print(len(matches))
            else:
                matches = re.findall(regex, contents)
                matches = list(set(map(lambda x: x.lower(), matches)))
                print(len(matches))


if __name__ == '__main__':
    main('test_file.txt')
