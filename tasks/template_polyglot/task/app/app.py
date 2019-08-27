from flask import Flask, render_template_string, request, make_response, redirect, abort, send_file
from bs4 import BeautifulSoup
import magic

app = Flask(__name__)

FLAG = "wwi{Hyp3Rte#t_3xP3Rts_6R0up}"

@app.context_processor
def inject_flag():
    return dict(flag=FLAG)

def check_html(content):
    content = content.decode('iso8859_2')
    return bool(BeautifulSoup(content, 'html.parser').find()) and '<html' in content


def check_jpeg(content):
    return magic.from_buffer(content, mime=True) == 'image/jpeg'


@app.route('/')
def index():
    return redirect('/index.html', 301)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    content = f.read()
    if not check_jpeg(content):
        return 'Not a picture, sir.'
    with open(f'./uploads/{f.filename}', 'wb') as f2:
        f2.write(content)
    return f'Your link: <a href="/uploads/{f.filename}">Click</a>'


@app.route('/uploads/<name>', methods=['GET'])
def uploads(name):
    try:
        return send_file(f'./uploads/{name}')
    except FileNotFoundError:
        return 'I can\'t find a file'


@app.route('/<name>', methods=['GET'])
def template(name):
    try:
        with open(f'./files/{name}', 'rb') as f:
            content = f.read()
    except FileNotFoundError:
        abort(404)

    if check_html(content):
        return render_template_string(content.decode('iso8859_2'))
    elif check_jpeg(content):
        response = make_response(content)
        response.headers['Content-Type'] = 'image/jpeg'
        return response
