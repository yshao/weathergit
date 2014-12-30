# smap_picture
#

## postgre ###

conn = ''
pic='test.jpg'

time='12172014'


conn.insert()
# update "Employees" set "photo" = ( select bytea_
# import('/usr/local/pgsql/backups/nwindpics/emp/1.jpg')) % time
# where "fileid"=1; % time


#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


def get_header():


def get_time():
    purl_utc()
    'smap-query'


def readImage():

    try:
        fin = open("woman.jpg", "rb")
        img = fin.read()
        return img

    except IOError, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:

        if fin:
            fin.close()


try:
    login=dict(host='',password='',dbname='',user='',port=5432)
    con = DbConn(login)
    # con = psycopg2.connect(database="testdb", user="janbo")

    stmt="INSERT into public()"
    con.insert()

    cur = con.cursor()
    # data = readImage()
    # binary = psycopg2.Binary(data)
    headerstamp=get_header(data)
    timestamp=get_time()
    filep=IMG_DIR+'/'+timestamp+'.jpg'

    # filep=IMG_DIR+filename
    cur.execute("INSERT into public()",(filep,headerstamp))
    # cur.execute("INSERT INTO Images(Id, Data) VALUES (1, %s)", (binary,) )

    con.commit()

except psycopg2.DatabaseError, e:

    if con:
        con.rollback()

    print 'Error %s' % e
    sys.exit(1)

finally:

    if con:
        con.close()