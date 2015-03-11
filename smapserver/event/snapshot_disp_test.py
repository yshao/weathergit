from common.smaputils import SmapUtils
from common.remote.remote import Remote


def webgen():
    d=Env().getConfig()

    args=dict(url=d['smap_source_host'])
    smaputils=SmapUtils(args)

    gen={}
    gen['lon']=smaputils.get_curr_val('/garmin0/longitude')
    gen['lat']=smaputils.get_curr_val('/garmin0/latitude')
    gen['alt']=smaputils.get_curr_val('/garmin0/altitude')


    with open('panel','wb') as f:
        f.write(gen)

    # get image from database
    filep=smaputils.get_curr_val('/trendnet0/timestamp')

    #
    remote=Remote.gen_login('data_server')
    d=remote.gen_login('data_server')
    remote.

    # get plots
    paths=['']
    for p in paths:
        ""

    def get_smap_values():
        ""