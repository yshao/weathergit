from common.smap.smap_query import run_query
from common.smap.smap_tool import *

SOURCE='http://192.168.1.146:8079'


# if __name__ == '__main__':
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
parser.add_option('-d', '--delete-report', dest='report_name',
                  default=None,
                  help="Remove a report (by name)")

opts, args = parser.parse_args()

test_liveness(SOURCE, opts)

display_reports(SOURCE,opts)
sq="select * from "
run_query(opts, sq)

# if not len(args):
#     parser.print_help()
#     sys.exit(1)

# for source_url in args:
#     if opts.liveness: test_liveness(source_url, opts)
#     if opts.destination: install_report(source_url, opts)
#     if opts.report_name: delete_report(source_url, opts)
#     if opts.reports: display_reports(source_url, opts)
#

# print test_liveness(SOURCE)


# cmd='x11vnc -bg -o %HOME/.x11vnc.log.%VNCDISPLAY -auth /var/run/lightdm/root/:0 -forever'
#
# sudo(cmd)
#
# browser.open('192.168.1.146:5900')
#
# '"C:\Program Files\Google\Chrome\Application\chrome.exe"  --profile-directory=Default --app-id=iabmpiboiopbgfabjmgeedhcmjenhbla'