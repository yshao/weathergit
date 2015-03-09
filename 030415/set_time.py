import psutil

__author__ = 'yuping'

def start_webgen():
    ""
    run('daemon.py')


def check():
    ### fabric ###

    if condition=True:
        actuate()

def actuate():
    beep_pomo()

def beep_pomo():
    ""

####
def check():
    check_pid('')

def actuate():
    start_webgen()


def check_pid(process_name):
    for proc in psutil.process_iter():
        process = psutil.Process(proc.pid)# Get the process info using PID
        pname = process.name()# Here is the process name
        #print pname
        if pname == process_name:
            print ("have")
        else:
            print ("Dont have")