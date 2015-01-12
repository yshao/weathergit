import readingdb as rdb

class RDBClient(object):
    def __init__(self):
        # specify default host/port
        rdb.db_setup('localhost', 4242)

        # create a connection
        self.db = rdb.db_open('localhost')

    def add_data(self):
        # add data.  the tuples are  (timestamp, seqno, value)
        rdb.db_add(self.db, 1, [(x, 0, x) for x in xrange(0, 100)])

    def query(self,query):

        # read back the data we just wrote using the existing connection
        # the args are streamid, start_timestamp, end_timestamp
        print "object"

        print "query: %s"+query
        print rdb.db_query(1, 0, 100, conn=db)
        # close

    def close(self):
        rdb.db_close(self.db)

# read back the data again using a connection pool this time.  You can
# specify a list of streamids to range-query multiple streams at once.
# print rdb.db_query([1], 0, 100)