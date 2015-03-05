import time

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/4/2015' '5:28 PM'

def tm_to_localtime(count):
    ""
    return time.gmtime(count/1000)

