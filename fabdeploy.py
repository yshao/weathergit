import tarfile
from fabric.operations import put, run

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

def deploy_smap_server():
    ""
    indir='smapserver'
    pkg='server.tar.gz'
    res=put(pkg)
    outdir='smapserver'

    run('tar -xf -C %s')
    run('deploy_smap_server')

def deploy_smap_bbb():
    ""
    indir='smapsource'
    pkg='smapbbb.tar.gz'
    outdir='smapbbb'
    res=put(pkg)
    run('tar -xf ')


# def deploy_smap_ipcam():
#     ""
#     pkg='smapipcam.tar.gz'
#     res=put(pkg)
#     if res.success:
#         outdir='server/ip'
#         remove('')
#         run('tar -xf -C %s' % outdir)
#
# def deploy_webpage():
#     ""
#     pkg='webpage.tar.gz'
#     outdir=''
#     with():
#         'tar -cvf webpage.tar.gz'
#
#
# def run_webpage():
#     with():
#         'python server_daemon.py start'


