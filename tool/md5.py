# Import hashlib library (md5 method is part of it)
import hashlib

# File to check
file_name = 'C:/Users/Ping/Downloads/qt-everywhere-opensource-src-4.8.6.tar.gz'

# Correct original md5 goes here
original_md5 = 'ddf9c20ca8309a116e0466c42984238009525da6'

# Open,close, read file and calculate MD5 on its contents
with open(file_name) as file_to_check:
    # read contents of the file
    data = file_to_check.read()
    print len(data)
    # pipe contents of the file through
    md5_returned = hashlib.sha1(data).hexdigest()

# Finally compare original MD5 with freshly calculated
if original_md5 == md5_returned:
    print "MD5 verified."
else:
    print "MD5 verification failed!."