import requests
from weathergit.common.env import Env


SMAP_SOURCE=Env.getparam("smap_source")
SMAP_SERVER=Env.getparam("smap_server")

path=dict()

sql=""
requests.GET(SMAP_SOURCE,query,sql)

requests.GET(SMAP_SERVER,'republish')

requests.GET(SMAP_SERVER,'next')

requests.GET(SMAP_SERVER,'tags')

requests.GET(SMAP_SERVER,'streams')

# requests.GET(SMAP_SOURCE,'reports')



### run ipython server ###
# fabfile runipython
# ipython notebook --ip=* --no-browser
# webview ipython calc