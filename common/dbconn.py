import psycopg2
import psycopg2.extensions
import logging
import json
import sys
from weathergit.common.config import Config


class LoggingCursor(psycopg2.extensions.cursor):
    def execute(self, sql, args=None):
        logger = logging.getLogger('sql_debug')
        logger.info(self.mogrify(sql, args))

        try:
            psycopg2.extensions.cursor.execute(self, sql, args)
        except Exception, exc:
            logger.error("%s: %s" % (exc.__class__.__name__, exc))
            raise

import re

from weathergit.common.env import Env


class DbConn(object):
    connected=False

    def __init__(self,login=None):

        if login == None:
            login={}
            config=Config(Env.getpath('HOME')+'/common/weatherplotter.conf')
            login['dbname']=config['smap_server_db_dbname']
            login['user']=config["smap_server_db_user"]
            login['password']=config['smap_server_db_password']
            login['host']=config['smap_server_host']
            login['port']=config['smap_server_db_port']
            self.login=login
        else:
            self.login=login
        self.connect()


    def connect(self):
        """"""

        login=self.login
        conn_string = "host='%(host)s' dbname='%(dbname)s' user='%(user)s' password='%(password)s' port='%(port)i'"\
                        % login

        try:
            self.conn = psycopg2.connect(conn_string)

            self.cursor = self.conn.cursor()
            cursor=self.cursor
            cursor.execute('SELECT version()')
            ver = cursor.fetchone()[0]
            m=re.search(r'PostgreSQL',ver)
            if m != None:
                self.connected = True


        except psycopg2.DatabaseError, e:
            print 'Error %s' % e

            # Get the most recent exception
            exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
            # sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
            pass




    def get_uuid(self):
        cur=self.conn.cursor()
        # cur = self.conn.cursor(cursor_factory=LoggingCursor)
        cur.execute("SELECT * from stream")
        rows = cur.fetchall()
        self.uuid={}
        for row in rows:
            s1=row[3].replace("=>",":")
            val=json.loads('{'+s1+'}')
            self.uuid[val['uuid']]=val


        return self.uuid

    def select(self,query):
        res=self.cursor.execute(query)
        return res.fetchall()

    def insert_img(self,query,val):
        """"""
        self.cursor.execute(query, val)

        self.conn.commit()

    # def __del__(self):
    #     """"""
    #     print self.conn
    #     self.conn.close()
    #     return True

    def close(self):
        self.conn.close()



# conn=DbConn(login)
# try:
#     uuid=conn.get_uuid()
#     # print uuid
#
#     # print uuid['0049d709-eb70-50b5-8349-859ab8b9c9f8']['Path']
#
#
# except Exception,e:
#     print e

### insert ###

# namedict = ({"first_name":"Joshua", "last_name":"Drake"},
#             {"first_name":"Steven", "last_name":"Foo"},
#             {"first_name":"David", "last_name":"Bar"})
#
#
# cur = conn.cursor()
# cur.executemany("""INSERT INTO bar(first_name,last_name) VALUES (%(first_name)s, %(last_name)s)""", namedict)

# try:
#     cur.execute("""DROP DATABASE foo_test""")
# except:
#     print "I can't drop our test database!"



