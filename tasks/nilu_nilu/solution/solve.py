import os
import re

import requests


def solve():
    base_url = os.environ.get('CTFT_BASE_URL')
    if base_url[-1] != '/':
        base_url += '/'

    sitemap = requests.get(base_url + 'sitemap.xml').text

    for m in re.finditer('<loc>(.*?)</loc>', sitemap):
        url = m.group(1)
        page = requests.get(url).text
        m2 = re.match('wwi{.*}', page)
        if m2:
            yield m2.group(0)


def main():
    print('\n'.join(solve()))


if __name__ == '__main__':
    main()
