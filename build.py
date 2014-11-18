from best.common.sysutils import *
from best.common.fileutils import *

### bbb with os ###

### comm with BBB ###
# start server
# client to server
# poll data

def build():
    """
    :param dir:
    :type dir: str

    :return:
    """

from best.common.sysutils import *
from best.common.fileutils import *

### build all ui
folder="gui"
for f in list_files(folder,".ui"):
    target=os.path.join(folder,"ui_"+os.path.basename(f)[:-3]+".py")
    run_command('pyuic4 -x %s -o %s' %(f,target))


# run_command("msbuild DAQArchImu /p:Configuration=Debug")
# run_command("msbuild DAQrad1 /p:Configuration=Debug")
# run_command("msbuild DAQenc /p:Configuration=Debug")

### deploy production project to embedded

# run_command('ipython notebook --no-browser')
