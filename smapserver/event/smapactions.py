from disk_usage import diskmain
from actions.notify import send_event_email

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/10/2015' '4:56 PM'



def update_status():

    txt=diskmain()
    print txt
    send_event_email(txt)
