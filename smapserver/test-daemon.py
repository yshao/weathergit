__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/10/2015' '1:44 PM'


import time
from daemon import Daemon


class pantalaimon(Daemon):
    def run():
        time.sleep(5)
        with open('code.txt','wb') as f:
            f.write('A')



pineMarten = pantalaimon('test-daemon.pid')
pineMarten.start()