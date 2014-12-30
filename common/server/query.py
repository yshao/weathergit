import readingdb as rdb

# specify default host/port
rdb.db_setup('localhost', 4242)

# create a connection
db = rdb.db_open('localhost')

# add data.  the tuples are  (timestamp, seqno, value)
rdb.db_add(db, 1, [(x, 0, x) for x in xrange(0, 100)])

# read back the data we just wrote using the existing connection
# the args are streamid, start_timestamp, end_timestamp
print rdb.db_query(1, 0, 100, conn=db)
# close
rdb.db_close(db)

# read back the data again using a connection pool this time.  You can
# specify a list of streamids to range-query multiple streams at once.
rdb.db_query([1], 0, 100) 