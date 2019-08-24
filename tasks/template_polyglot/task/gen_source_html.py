import html


with open('./app/app.py', 'r') as f:
    source = f.read()

with open('./app/files/source.html', 'w') as f:
    f.write('<html><body><code><pre>' + html.escape(source) + '</pre></code></body></html>')
