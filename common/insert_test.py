#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
from common.dbconn import DbConn


cars = (
    (1, 'Audi', 52642),
)

con = None

try:
     
    con = psycopg2.connect("dbname='testdb' user='janbodnar'")   
  
    cur = con.cursor()  
    
    # cur.execute("DROP TABLE IF EXISTS Cars")
    # cur.execute("CREATE TABLE Cars(Id INT PRIMARY KEY, Name TEXT, Price INT)")
    query = "INSERT INTO Snapshots (Id, ImagePath, ImageIdx) VALUES (%s, %s, %s)"
    cur.executemany(query, cars)
        
    con.commit()
    

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
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
        # con = psycopg2.connect(database="testdb", user="janbodnar")
        con=DbConn()
        cur = con.cursor()
        cur.execute("SELECT ImagePath FROM Snapshots LIMIT 1")
        fpath = cur.fetchone()[1]

        fh=readImage(fpath)


    except psycopg2.DatabaseError, e:

        print 'Error %s' % e
        sys.exit(1)

    finally:

        if con:
            con.close()