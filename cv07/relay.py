# -*- coding: utf-8 -*-

"""
Cvičení 7. - práce s daty

Vaším dnešním úkolem je spojit dohromady data, uložená ve dvou různých
souborech. První soubor obsahuje výsledky závodu - jména a časy závodníků. Druhý
pak obsahuje databázi závodníků uloženou jako JSON - mimo jiné jejich id. Cílem
je vytvořit  program, který tyto data propojí, tedy ke každému závodníkovi ve
štafetě najde jeho id. Případně také nenajde, data nejsou ideální. I tuto
situaci ale musí program korektně ošetřit.  Výsledky programu bude potřeba
zapsat do dvou souborů.

Kompletní zadání je jako vždy na https://elearning.tul.cz/

"""
import json
import re

from bs4 import BeautifulSoup

RELAY_RESULTS_PATTERN = re.compile(
    r'\d+\)\s(\w+\s*\w*)\s(\d+:\d+:\d+)\s\(([a-zA-Z- ]+),\s([a-zA-Z- ]+),\s([a-zA-Z- ]+)\)'
)


def output_json(result_list):
    """
    Uloží list slovníků do souboru output.json tak jak je požadováno
    v zadání.
    """
    with open('output.json', 'w', encoding='utf-8') as output:
        output.write(json.dumps(result_list, indent=4, sort_keys=True))


def extract_relay_data(html_file: str):
    """
    Extrahuje data ze souboru s výsledky štafetového závodu.
    """
    with open(html_file, 'r', encoding='utf-8') as html:
        soup = BeautifulSoup(html, 'html.parser')
        paragraphs = soup.findAll('p')
        women = paragraphs[18]
        men = paragraphs[20]
        return tuple(RELAY_RESULTS_PATTERN.findall(women.text)), \
            tuple(RELAY_RESULTS_PATTERN.findall(men.text))


if __name__ == '__main__':
    relay_data = extract_relay_data('result.html')
