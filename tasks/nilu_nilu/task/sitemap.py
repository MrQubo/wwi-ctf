
with open('ids', 'r') as f:
    lines = [l for l in f.read().split('\n') if l.strip() != '']

s = []
for l in lines:
    s += [f'''  <url>
    <loc>https://ctf.staszic.waw.pl/aio/{l}</loc>
  </url>''']
s = '\n'.join(s)

s = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://ctf.staszic.waw.pl</loc>
  </url>
  <url>
    <loc>https://ctf.staszic.waw.pl/notifications</loc>
  </url>
  <url>
    <loc>https://ctf.staszic.waw.pl/users</loc>
  </url>
  <url>
    <loc>https://ctf.staszic.waw.pl/teams</loc>
  </url>
  <url>
    <loc>https://ctf.staszic.waw.pl/scoreboard</loc>
  </url>
  <url>
    <loc>https://ctf.staszic.waw.pl/challenges</loc>
  </url>
  <url>
    <loc>https://ctf.staszic.waw.pl/user</loc>
  </url>
  <url>
    <loc>https://ctf.staszic.waw.pl/team</loc>
  </url>
  <url>
    <loc>https://ctf.staszic.waw.pl/settings</loc>
  </url>
{s}
</urlset>'''
print(s)
