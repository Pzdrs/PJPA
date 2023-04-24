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
    r'(\d+)\)\s(\w+\s*\w*)\s(\d+:\d+:\d+)\s\(([a-zA-Z- ]+),\s([a-zA-Z- ]+),\s([a-zA-Z- ]+)\)'
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


def load_competitors(json_file: str) -> list[dict]:
    """
    Načte data z databáze závodníků.
    """
    with open(json_file, 'r', encoding='utf-8') as json_data:
        return json.load(json_data)


def lookup_competitor(**filters) -> dict | None:
    """
    Vyhledá závodníka v databázi závodníků.
    """
    results = []
    for competitor in competitors:
        if all(competitor.get(key) == value for key, value in filters.items()):
            results.append(competitor)
    return results


def process_country_results(country_results: tuple[tuple, ...], gender: str, debug: bool = False):
    """
    Zpracuje výsledky závodu pro jednu zemi.
    """
    lookups = []
    for result in country_results:
        people = []
        if debug:
            print(result)
        for person in result[3:]:
            person_name = person.split(' ')
            lookup_result = lookup_competitor(
                gender=gender, lastname=person_name[1], firstname=person_name[0]
            )
            if debug:
                print(lookup_result)
            people.append((person, lookup_result))
        lookups.append((result, tuple(people)))
    return tuple(lookups)


def build_final_results(processed_country_data: tuple[tuple, tuple]):
    """
    Vytvoří výsledky pro každého závodníka v závodě.
    """
    to_return = []
    original_data = processed_country_data[0]
    looked_up_people = processed_country_data[1]
    for pos, person in enumerate(looked_up_people, start=1):
        looked_up_for = person[0]
        lookup_result = person[1]
        lookup_result_len = len(lookup_result)
        if lookup_result_len == 1:
            lookup_result = lookup_result[0]
            to_return.append({
                'id': lookup_result['id'],
                'result': pos,
                'time': original_data[1],
            })
        elif lookup_result_len == 0:
            to_return.append({
                'id': False,
                'result': pos,
                'time': original_data[1],
                'no_match': looked_up_for,
            })
        else:
            raise ValueError(f'Inconclusive lookup, {len(person)} results found')
    return tuple(to_return)


if __name__ == '__main__':
    competitors = load_competitors('competitors.json')
    relay_data = extract_relay_data('result.html')

    print('Processing data...', end='')
    processed_country_data__females = process_country_results(relay_data[0], 'F')
    processed_country_data__males = process_country_results(relay_data[1], 'M')
    print('done')

    final_results = []
    for a in processed_country_data__females + processed_country_data__males:
        final_results.extend(build_final_results(a))

    # first soubor
    print('Writing output.json...', end='')
    output_json(final_results)
    print('done')

    # second soubor
    print('Writing compare.txt...', end='')
    with open('compare.txt', 'w', encoding='utf-8') as compare:
        for result in sorted(
                [final_result for final_result in final_results if final_result['id'] is not False],
                key=lambda x: x['id']
        ):
            compare.write(f'{result["id"]} {result["result"]}\n')
    print('done')

    # third soubor
    print('Writing errors.txt...', end='')
    with open('errors.txt', 'w', encoding='utf-8') as errors:
        for result in sorted(
                [final_result for final_result in final_results if final_result['id'] is False],
                key=lambda x: x['id']
        ):
            errors.write(f'{result["no_match"]}\n')
    print('done')
