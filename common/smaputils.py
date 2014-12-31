import unittest
from weathergit.common.smaplib.smap_query import *
from weathergit.common.smaplib.smap_tool import *
from weathergit.common.smaplib.smap_load import *
from weathergit.common.smaplib.smap_load_csv import *
SOURCE='http://192.168.1.146:8079'


### preserved for all options to be enabled
default_backend = 'http://192.168.1.120:8079/api/query'
# usage = 'usage: %prog [options] url'


# sql="select data in (\"1/1/2012\", \"1/7/2012\") where uuid='62a74dc0-d3c1-5986-aefa-953bf7a616e7'"
sql="select data in (\"12/29/2014\", \"12/30/2014\")  streamlimit 200 where uuid='62a74dc0-d3c1-5986-aefa-953bf7a616e7'"

class SmapUtils(object):
    """
    Facade to provided smap toolsets, timeseries client, and smap data client
    """
    parser = OptionParser()
    opts={}
    args={}

    def __init__(self,args):
        ""


    def init_smap_load(self):
        ""
        parser.add_option('-t', '--timefmt', dest='timefmt', default='%m-%d-%Y',
                          type='str',
                          help='time format string for start and end ("%m-%d-%Y")')
        parser.add_option('-m', '--start-time', dest='start_time',
                          default="now_minus_1hour", type='str',
                          help='start time of import')
        parser.add_option('-n', '--end-time', dest='end_time',
                          default="now", type='str',
                          help='end time of import')
        parser.add_option('-z', '--timezone', dest='timezone',
                          default='Local', type='str',
                          help='time zone for time conversion')
        parser.add_option('-s', '--reset', dest='reset',
                          default=False, action='store_true',
                          help='reset drivers before running')
        parser.add_option('-a', '--no-cache', dest='cache',
                          default=True, action='store_false',
                          help='don\'t cache downloaded data')

        opts, args = parser.parse_args()

    def init_smap_query(self):
        ""
        parser.add_option('-b', '--url', dest='url',
                          default=default_backend,
                          help='location of backend server')
        parser.add_option('-k', '--key', dest='key', default=None,
                          help='api keys: k1[,k2 ...]')
        parser.add_option('-r', '--private', dest='private', default=False,
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

    def init_smap_tool(self):
        ""
        parser.add_option('-l', '--liveness', dest='liveness',
                          default=False, action='store_true',
                          help="Test sMAP source for for liveness")
        parser.add_option('-u', '--uuids', dest='uuids',
                          default=False, action='store_true',
                          help="Print uuids instead of paths")
        parser.add_option('-p', '--reports', dest='reports',
                          default=False, action='store_true',
                          help="Display report destinations for the source")
        parser.add_option('-c', '--create-report', dest='destination',
                          default=None,
                          help="Start sending data to a new destination URL")
        parser.add_option('-e', '--delete-report', dest='report_name',
                          default=None,
                          help="Remove a report (by name)")

        opts, args = parser.parse_args()

    def run_server_query(self,sql):
        self.init_smap_query()
        run_query(opts, sql)

    def run_server_calc(self,conf_filep):
        self.init_smap_tool()

    def get_curr_val(self,path):
        ""
        self.init_smap_query()
        response=dict(out='',err=False,code=0)
        sql="select data before now where uuid='%s'" % path
        try:
            res=run_query(opts,sql)
            if res != '[]':
                val=parse(res)
            response['msg']=val

        except Exception,e:
            print e
            response['err']=True
            response['code']=e

        return response



    def show_smap_monitor(self,url):
        test_liveness(url, opts)

    def show_smap_reports(self,url):
        display_reports(url,opts)

    def load_server_csv(self,filep):
        ""

    def add_smap_driver(self,):
        ""




# cmd='x11vnc -bg -o %HOME/.x11vnc.log.%VNCDISPLAY -auth /var/run/lightdm/root/:0 -forever'
#
# sudo(cmd)
#
# browser.open('192.168.1.146:5900')
#
# '"C:\Program Files\Google\Chrome\Application\chrome.exe"  --profile-directory=Default --app-id=iabmpiboiopbgfabjmgeedhcmjenhbla'


