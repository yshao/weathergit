#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
from weathergit.common.dbconn import DbConn


con = None

def insert_snapshot(image):
    try:
        image=('Cam1-18-12-201411-51-14.jpg','18-12-201411-51-14')
        # fmt='dd-mm-yyyy hh24-mm-ss'
        query = "INSERT INTO images (ImagePath, ImageIdx) VALUES (%s, %s)"

        con.insert_img(query,image)
    except psycopg2.DatabaseError,e:
        if con:
            # con.rollback()
            ""
        print str(e)
    finally:
        if con:
            con.close()


###retrieve
def readImage(fpath):
    try:
        fout = open(fpath,'wb')
        # fout.write(data)


    except IOError, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:
        if fout:
            fout.close()


def convert_to_video():
    'avconv -f image2 -i figMatplotlib%d.png -r 76 -s 800x600 foo.avi'

def get_image():
    try:
        con=DbConn()
        stmt="SELECT ImagePath FROM images LIMIT 1"
        res=con.select(stmt)
        fpath = res.fetchone()[1]

        fh=readImage(fpath)


    except psycopg2.DatabaseError, e:

        print 'Error %s' % e

    finally:

        if con:
            con.close()