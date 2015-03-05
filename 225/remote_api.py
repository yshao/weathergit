__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/25/2015' '1:50 PM'

def get_scheduler_status():
    with settings(host_string='data@192.168.1.120',password='reverse'):
        p=psutil.Process()
        d= p.get_connections()

    return d


get_scheduler_status()