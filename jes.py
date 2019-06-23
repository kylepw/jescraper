"""
    jes.py
    ~~~~~~

    Scrape first result from each part of speech for given word (JP or Eng).

    Usage:
        python3 jes.py [word]

"""

from bs4 import BeautifulSoup
import requests
import sys


def scrape_alc(query=None):
    if not query:
        return

    url_template = 'https://eow.alc.co.jp/search?q=%s'

    url = url_template % query.replace(' ', '+')

    POS_KEYS = {'形': 'adj', '名': 'n', '動': 'v', '副': 'adv', '間投': 'interj'}

    r = requests.get(url)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'html.parser')

    try:
        # Grab first result of each part of speech (POS) only
        pos_content = (
            soup.find('div', {'id': 'resultsList'}).find('ul').find('li').find_all('ol')
        )
    except AttributeError:
        sys.exit('No results found for %s.' % query)

    results = {}
    for p in pos_content:
        # Remove `span` tags
        for s in p.find_all('span'):
            s.replace_with('')

        first_result = p.find('li')
        if not first_result:
            # POS with only one result is not wrapped in `li` tags
            first_result = p

        # Find part of speech, default to 'other'
        pos_key = 'other'
        for k, v in POS_KEYS.items():
            if k in p.previous_element:
                pos_key = v
                break

        # Sort by part of speech
        results.setdefault(pos_key, []).append(first_result.text)

    return results


def print_data(query=None, data=None):
    if not query or not data:
        return

    try:
        print(query + '\n')
        for pos, vals in data.items():
            print(f'[{pos}]')
            for v in vals:
                print(v)
    except (TypeError, AttributeError):
        return


if __name__ == '__main__':
    try:
        query = sys.argv[1]
        print_data(query, scrape_alc(query))
    except IndexError:
        query = 'missing'
        print_data(query, scrape_alc(query))
