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
    url_template = 'https://eow.alc.co.jp/search?q=%s'

    # Random example
    if not query:
        query = 'missing'

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

    print(query + '\n')
    for pos, vals in results.items():
        print(f'[{pos}]')
        for v in vals:
            print(v)


if __name__ == '__main__':
    try:
        scrape_alc(sys.argv[1])
    except IndexError:
        scrape_alc()
