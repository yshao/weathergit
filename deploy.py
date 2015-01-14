def deploy_server_package():
    ""
    pkg='server.tar.gz'
    res=put(pkg)
    outdir='server'

    run('tar -xf -C %s')

def deploy_smap_bbb():
    ""
    pkg='smapbbb.tar.gz'
    outdir='smapbbb'
    res=put(pkg)
    run('tar -xf ')


def deploy_smap_ipcam():
    ""
    pkg='smapipcam.tar.gz'
    res=put(pkg)
    if res.success:
        outdir='server/ip'
        remove('')
        run('tar -xf -C %s' % outdir)

