import psycopg2
from best.common.sysutils import Command

def testConnection(ip):
    def parse():
        ""


    command = Command("ping -n 1 %s" % ip,parse)
    code,out,err =  command.run(timeout=3)



import sys

def testPostgreConnection():
    host = 'smapserver'
    dbname = 'weather'
    user = 'best'
    password = 'best'
    port = 5432

    conn_string = "host='%s' dbname='%s' user='%s' password='%s' port='%i'"\
                    % (host, dbname, user, password, port)

    # print the connection string we will use to connect
    print "Connecting to database\n ->%s" % (conn_string)

    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        print "Connected!\n"
    except:
        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        sys.exit("Database connection failed!\n ->%s" % (exceptionValue))


if __name__ == '__main__':
    testPostgreConnection()