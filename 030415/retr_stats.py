from fabric.decorators import task
from fabric.tasks import execute

@task
def stats():

    memusage = execute("""

      #! /usr/bin/env python
      import psutil

      pid = open('pidfile').read()
      process = psutil.Process(int(pid))
      print process.get_memory_percent()

    """, 'memusage.py', verbose=False, dir='/var/ampify')