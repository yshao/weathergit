
# from weathergit.common.smaplib.jprint import pprint
# from weathergit.common.smaplib.smap_query import *
from weathergit.common.smaplib.smap_tool import *
# from weathergit.common.smaplib.smap_load import *
# from weathergit.common.smaplib.smap_load_csv import *
# SOURCE='http://192.168.1.146:8079'


### preserved for all options to be enabled
from optparse import OptionParser

default_backend = 'http://192.168.1.120:8079/api/query'
# usage = 'usage: %prog [options] url'


# sql="select data in (\"1/1/2012\", \"1/7/2012\") where uuid='62a74dc0-d3c1-5986-aefa-953bf7a616e7'"
# sql="select data in (\"12/29/2014\", \"12/30/2014\")  streamlimit 200 where uuid='62a74dc0-d3c1-5986-aefa-953bf7a616e7'"

class SmapUtils(object):
    """
    Facade to provided smap toolsets, timeseries client, and smap data client
    """
    parser = OptionParser()
    opts={}
    args={}

    def __init__(self):
        ""
        args={}
        self.url='http://192.168.1.146:8079'



    def _init_smap_load(self):
        ""
        self.parser.add_option('-t', '--timefmt', dest='timefmt', default='%m-%d-%Y',
                          type='str',
                          help='time format string for start and end ("%m-%d-%Y")')
        self.parser.add_option('-m', '--start-time', dest='start_time',
                          default="now_minus_1hour", type='str',
                          help='start time of import')
        self.parser.add_option('-n', '--end-time', dest='end_time',
                          default="now", type='str',
                          help='end time of import')
        self.parser.add_option('-z', '--timezone', dest='timezone',
                          default='Local', type='str',
                          help='time zone for time conversion')
        self.parser.add_option('-s', '--reset', dest='reset',
                          default=False, action='store_true',
                          help='reset drivers before running')
        self.parser.add_option('-a', '--no-cache', dest='cache',
                          default=True, action='store_false',
                          help='don\'t cache downloaded data')

        self.opts, self.args = self.parser.parse_args()

    def _init_smap_load_csv(self):
        self.parser = OptionParser()

        self.parser.add_option('-u', '--uuid', dest='uuid',
                          default='9ffb78a6-4c6a-11e2-b19e-d78597b0c967',
                          help='root uuid')
        self.parser.add_option('-i', '--ignore-channels', dest='ignore',
                          default='', help='comma-separated list of column names '
                          'or indexes to ignore')
        self.parser.add_option('-c', '--take-channels', dest='takes',
                          default='', help='comma-separated list of column names '
                          'or indexes to load')
        self.parser.add_option('-t', '--time-channel', dest='time',
                          default='', help='name or index of the column with '
                          'timestamps')
        self.parser.add_option('-f', '--time-format', dest='time_format',
                          default='%s', help='format string used to parse the '
                          'timestamps')
        self.parser.add_option('-z', '--time-zone', dest='time_zone',
                          default='America/Los_Angeles', help='time zone name')
        self.parser.add_option('-d', '--report-dest', dest='report_dest',
                          default=None, help='reporting destination')
        self.parser.add_option('-v', '--verbose', dest='verbose',
                          default=False, help='verbose', action='store_true')
        self.parser.add_option('-k', '--skip-lines', dest='skip_lines',
                          default=0, type='int', help='number of lines to skip')
        self.parser.add_option('-l', '--limit-lines', dest='limit', type='int',
                          default=None, help='only process this many lines from the file')
        self.parser.add_option('-s', '--source-name', dest='source_name',
                          default='CSV Input', help='Metadata/SourceName tag value')

        self.opts, self.args = self.parser.parse_args()


    def _init_smap_query(self):
        ""
        self.parser.add_option('-b', '--url', dest='url',
                          default=default_backend,
                          help='location of backend server')
        self.parser.add_option('-k', '--key', dest='key', default=None,
                          help='api keys: k1[,k2 ...]')
        self.parser.add_option('-r', '--private', dest='private', default=False,
                          help='display only results associated with the api key',
                          action='store_true')
        self.parser.add_option('-t', '--timeout', dest='timeout', default=60,
                          type="int")
        self.parser.add_option('-v', dest='verbose', default=0,
                          help="be verbose", action="count")
        self.parser.add_option('-n', '--no-dates', dest='dates',
                          default=True, action='store_false',
                          help='don\'t convert dates to string representation')
        self.parser.add_option('-d', '--dry-run', dest='noop',
                          default=False, action='store_true',
                          help='mutations display their results but don\'t actually happen')

        self.opts, self.args = self.parser.parse_args()

    def _init_smap_tool(self):
        ""
        self.parser.add_option('-l', '--liveness', dest='liveness',
                          default=False, action='store_true',
                          help="Test sMAP source for for liveness")
        self.parser.add_option('-u', '--uuids', dest='uuids',
                          default=False, action='store_true',
                          help="Print uuids instead of paths")
        self.parser.add_option('-p', '--reports', dest='reports',
                          default=False, action='store_true',
                          help="Display report destinations for the source")
        self.parser.add_option('-c', '--create-report', dest='destination',
                          default=None,
                          help="Start sending data to a new destination URL")
        self.parser.add_option('-e', '--delete-report', dest='report_name',
                          default=None,
                          help="Remove a report (by name)")

        self.opts, self.args = self.parser.parse_args()
        # print 'B'

    def run_server_query(self,sql):
        self._init_smap_query()
        run_query(self.opts, sql)

    def run_server_calc(self,conf_filep):
        self._init_smap_tool()

    def get_curr_val(self,path):
        ""
        def parse(json):
            print pprint(json)

        self._init_smap_query()
        response=dict(out='',err=False,code=0)
        sql="select data before now where Path='%s'" % path
        try:
            res=run_query(self.opts,sql)
            if res != '[]':
                val=parse(res)
            response['msg']=val

        except Exception,e:
            print e
            response['err']=True
            response['code']=e

        return response

    def get_smap_monitor(self):
        self._init_smap_tool()
        return get_liveness(self.url)


    def show_smap_monitor(self):
        self._init_smap_tool()
        test_liveness(self.url, self.opts)

    def show_smap_reports(self):
        self._init_smap_tool()
        display_reports(self.url,self.opts)

    # def load_server_csv(self,filep,stream=None):
    #     ""
    #     self._init_smap_tool_csv()
    #     if stream == None:
    #         server_load_csv(filep,self.opts)
    #     else:
    #         server_load_csv(filep,stream,self.opts)


    # def add_smap_driver(self,):
    #     ""
    #
    #

if __name__ == '__main__':
    su=SmapUtils()
    # su.get_smap_monitor()
    su.show_smap_monitor()
    # d=su.get_smap_monitor()
    # for uid in d.keys():
    #     print d[uid]['path'] + ' ' + d[uid]['curr'] + ' ' + str(d[uid]['props'])
