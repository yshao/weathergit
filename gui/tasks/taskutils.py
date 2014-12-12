import os
import re
import psycopg2
from best.common.sysutils import Command
from weathergit.common.config import Config

config=Config("../../common/weatherplotter.conf")

def testConnection(ip):
    def parse(res):
        ""
        # print res[0]
        if res[2] == '':
            for ln in res[1].split('\n'):
                m=re.search('1ms',ln)
                if m != None:
                    return True

            return False
        else:
            return False,res[2]


    command = Command("ping -n 1 %s" % ip,parse)
    res =  command.run(timeout=3)
    return parse(res)


# root_dir = os.path.abspath(os.path.dirname(__file__))
# print root_dir


import sys
import psycopg2

def testPostgreConnection(login):
    conn_string = "host='%(host)s' dbname='%(dbname)s' user='%(user)s' password='%(password)s' port='%(port)i'"\
                    % login

    # print the connection string we will use to connect
    # print "Connecting to database\n ->%s" % (conn_string)

    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        cursor.execute('SELECT version()')
        ver = cursor.fetchone()[0]
        # print ver[0]
        m=re.search(r'PostgreSQL',ver)
        if m != None:
            return True

        # print "Connected!\n"
    except psycopg2.DatabaseError, e:
        # print 'Error %s' % e

        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        # sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
        return False,exceptionType

