import psutil

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/25/2015' '10:23 AM'


class DriverConfig(JsonConfig):
    ""
    def __init__(self):
        ""


class EventConfig(JsonConfig):
    ""
    def __init__(self):
        ""

    def daemonize(self):
        ""





camdriver=DriverConfig()

camdriver.load()
camdriver.send('')

camdriver.status()

weatherdriver.status()

pracodriver.status()

### psutil ###
p=psutil.Process()
p.pid()
