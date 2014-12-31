import unittest
from weathergit.common.smaputil.smap_query import *
from weathergit.common.smaputil.smap_tool import *

SOURCE='http://192.168.1.146:8079'


### preserved for all options to be enabled
default_backend = 'http://192.168.1.120:8079/api/query'
usage = 'usage: %prog [options] url'
parser = OptionParser(usage=usage)
parser.add_option('-l', '--liveness', dest='liveness',
                  default=False, action='store_true',
                  help="Test sMAP source for for liveness")
parser.add_option('-u', '--uuids', dest='uuids',
                  default=False, action='store_true',
                  help="Print uuids instead of paths")
parser.add_option('-r', '--reports', dest='reports',
                  default=False, action='store_true',
                  help="Display report destinations for the source")
parser.add_option('-c', '--create-report', dest='destination',
                  default=None,
                  help="Start sending data to a new destination URL")
parser.add_option('-e', '--delete-report', dest='report_name',
                  default=None,
                  help="Remove a report (by name)")

parser.add_option('-b', '--url', dest='url',
                  default=default_backend,
                  help='location of backend server')
parser.add_option('-k', '--key', dest='key', default=None,
                  help='api keys: k1[,k2 ...]')
parser.add_option('-p', '--private', dest='private', default=False,
                  help='display only results associated with the api key',
                  action='store_true')
parser.add_option('-t', '--timeout', dest='timeout', default=60,
                  type="int")
parser.add_option('-v', dest='verbose', default=0,
                  help="be verbose", action="count")
parser.add_option('-n', '--no-dates', dest='dates',
                  default=True, action='store_false',
                  help='don\'t convert dates to string representation')
parser.add_option('-d', '--dry-run', dest='noop',
                  default=False, action='store_true',
                  help='mutations display their results but don\'t actually happen')

opts, args = parser.parse_args()

test_liveness(SOURCE, opts)

display_reports(SOURCE,opts)
# sql="select data in (\"1/1/2012\", \"1/7/2012\") where uuid='62a74dc0-d3c1-5986-aefa-953bf7a616e7'"
sql="select data in (\"12/29/2014\", \"12/30/2014\")  streamlimit 200 where uuid='62a74dc0-d3c1-5986-aefa-953bf7a616e7'"
run_query(opts, sql)


# cmd='x11vnc -bg -o %HOME/.x11vnc.log.%VNCDISPLAY -auth /var/run/lightdm/root/:0 -forever'
#
# sudo(cmd)
#
# browser.open('192.168.1.146:5900')
#
# '"C:\Program Files\Google\Chrome\Application\chrome.exe"  --profile-directory=Default --app-id=iabmpiboiopbgfabjmgeedhcmjenhbla'


# class smaputilsTest(unittest.TestCase):
#     def setUp(self):
#         ""
#         self.c=
#
#     def test_querySelect(self):
#         self.c.