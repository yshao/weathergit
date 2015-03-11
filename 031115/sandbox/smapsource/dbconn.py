import psycopg2
import psycopg2.extensions
import logging
import json
import sys


class LoggingCursor(psycopg2.extensions.cursor):
    def execute(self, sql, args=None):
        logger = logging.getLogger('sql_debug')
        logger.info(self.mogrify(sql, args))

        try:
            psycopg2.extensions.cursor.execute(self, sql, args)
        except Exception, exc:
            logger.error("%s: %s" % (exc.__class__.__name__, exc))
            raise

# # Try to connect
#
# login={"host":"192.168.1.120","dbname":"archiver","user":"archiver","password":"password"}
#
# conn=None
# # print "host='%(host)s' dbname='%(dbname)s' user='%(user)s' password='%(password)s'" % login
# try:
#     conn=psycopg2.connect("host='%(host)s' dbname='%(dbname)s' user='%(user)s' password='%(password)s'" % login)
# except:
#     print "I am unable to connect to the database."
#
#
# cur = conn.cursor(cursor_factory=LoggingCursor)
#
#
# try:
#
#     cur.execute("SELECT * from stream")
#     rows = cur.fetchall()
#     for row in rows:
#         ""
#         # print row[2],row[3]
#         # js=json.load(row[3])
#
#         # print js
#
#
# except Exception,e:
#     print "cannot select"
#
#
# s='"Path"=>"/KCABERKE25/dew_point", "uuid"=>"0049d709-eb70-50b5-8349-859ab8b9c9f8", "Readings"=>"[[1402685274000L, 10.6]]", "Metadata/SourceName"=>"WunderGround Data", "Properties/Timezone"=>"US/Pacific", "Metadata/Location/Uri"=>"http://wunderground.com/weatherstation/", "Metadata/Location/City"=>"Berkeley", "Properties/ReadingType"=>"double", "Metadata/Location/State"=>"CA", "Properties/UnitofMeasure"=>"C", "Metadata/Extra/StationType"=>"Davis VP2", "Metadata/Location/Altitude"=>"188 ft", "Metadata/Location/Latitude"=>"37.892567", "Metadata/Location/Longitude"=>"-122.280258", "Metadata/Location/StationID"=>"KCABERKE25"'
# s1=s.replace("=>",":")
#
# try:
#     meta=json.loads('{'+s1+'}')
#
# except Exception,e:
#     print e
#
#
# # print meta['uuid']
#
#
#


class DbConn(object):
    def __init__(self,login):
        """"""
        self.conn=psycopg2.connect("host='%(host)s' dbname='%(dbname)s' user='%(user)s' password='%(password)s'" % login)


    def get_uuid(self):
        cur = self.conn.cursor(cursor_factory=LoggingCursor)
        cur.execute("SELECT * from stream")
        rows = cur.fetchall()
        self.uuid={}
        for row in rows:
            s1=row[3].replace("=>",":")
            val=json.loads('{'+s1+'}')
            self.uuid[val['uuid']]=val


        return self.uuid

    def insert_record(self):
        """"""
        cur = self.conn.cursor(cursor_factory=LoggingCursor)


    def __del__(self):
        """"""
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



