from disk_usage import diskmain
from actions.notify import send_event_email
from event.supervisory import get_pids

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/10/2015' '4:56 PM'

def update_status():
    txt1='\n'.join(diskmain())
    txt2='\n'.join(get_pids())

    content='\n'.join([txt1,txt2])
    send_event_email(content)
class Monitor():
    def __init__(self):
        ""

    def update_status(self):
        txt1='\n'.join(diskmain())
        txt2='\n'.join(get_pids())

        content='\n'.join([txt1,txt2])
        send_event_email(content)


    def watchdog(self):
        ""
        # 1. check()
        # 2.
        # 3. check

