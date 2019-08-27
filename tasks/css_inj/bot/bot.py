import time
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import functools
print = functools.partial(print, flush=True)

session = requests.session()

SRV = 'http://cssinjweb:8000'

PASSWORD = 'SkjwYOSuOps39gjvHIckEw'

login_data = {
    'username': 'bot',
    'password': PASSWORD,
}

while True:
    try:
        resp = session.get(SRV+'/login')
        if resp.status_code == 200:
            break
        print("Still waiting...", resp.status_code)
    except Exception as e:
        print(e)
        pass
    time.sleep(1)


csrf = session.get(SRV+'/login/').cookies['csrftoken']
login_data['csrfmiddlewaretoken'] = csrf
print(session.post(SRV + '/login/', login_data).content)

options = Options()
options.headless = True

while True:
    todo = session.get(SRV + '/bot/list').json()['urls']
    if len(todo) == 0:
        print("Nothing to do...")
        time.sleep(2)
    else:
        for el in todo:
            print("Processing %s" % el)
            try:
                browser = webdriver.Firefox(options=options)
                browser.set_page_load_timeout(4)
                browser.get(SRV+'/login/')
                browser.find_element_by_id('id_username').send_keys('bot')
                browser.find_element_by_id('id_password').send_keys(PASSWORD)
                browser.find_element_by_id('submit').click()
                time.sleep(2)
                browser.get(SRV+el)
                time.sleep(4)
            except Exception as e:
                print(e)
            finally:
                browser.quit()
