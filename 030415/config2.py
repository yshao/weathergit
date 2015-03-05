__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/4/2015' '5:39 PM'

### gets secured and config


class SecuredConfig():
    def __init__(self):
        ""
        d={}
        kd=get_passwords(d['keyfile'])
        d.merge(kd)