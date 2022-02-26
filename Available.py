import sys
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from line_notify import LineNotify

class Available():
    def __init__(self, url='', config = {}, interval = 1, line_token =''):
        self.url = url
        self.config = config
        self.interval = interval
        self.line_notify = LineNotify(line_token)

    
    def printLog(self, *texts):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        text = current_time + ' : ' + ' '.join([str(text) for text in texts])
        print(text)

    def start_bot(self):
        while True:
            try:
                self.start()
            except Exception as e:
                self.printLog(str(e))

            time.sleep(self.interval * 2)

    def start(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, 'html.parser')
        checks = soup.select(self.config['selector'])

        is_available = False
        for check in checks:
            if check.get_text().find(self.config['available_text']) != -1:
                is_available = True

        if is_available:
            self.line_notify.send(f'🔥🔥 สินค้ามาแล้ว 🔥🔥\n{self.url}')
            if self.config['onetime']:
                sys.exit(1)
        else:
            self.printLog('[INFO] สินค้าหมด')
            

