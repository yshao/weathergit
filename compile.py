
# check depency
# check leaks

# build doc
run_command('pydoc gui/weatherclient.py')

run_command('pyinstaller gui/weatherclient.py')

#remove build
#package dist in zip
#package in python27
#build innosetup



#create daemon
#run_command('pyinstaller server/server_daemon.py')
#run_command('pyinstaller server/_daemon.py')
# package all

# installation
#
# run_command('tar -cvf server.tar.gz server')
# run_command('tar -cvf smapipcam.tar.gz smapipcam')
# run_command('tar -cvf smapbbb.tar.gz smapbbb')

# deploy
# put(server)
# put(smap)
# put(server)
# run(server_daemon)
# run(smapipcam)


#
#os.remove('build')
#os.remove('dist')