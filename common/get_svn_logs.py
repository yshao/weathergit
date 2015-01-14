__author__ = 'Ping'

import re

from subprocess import Popen, PIPE
p = Popen('svn log -v --stop-on-copy http://subversion.repository.com/svn/repositoryname',
          stdout=PIPE)
stdout, stderr = p.communicate()


m = re.search('\r\nr(?P<rev>\d+)\s+\|\s+(?P<author>\w+)\s+\|\s+(?P<timestamp>.*?)\s|', stdout)
{'timestamp': '2011-10-10 10:45:01 +0000 (wed, okt 10 2011)',
 'rev': '1234',
 'author': 'someuser'
}