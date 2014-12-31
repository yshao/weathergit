import unittest

from weathergit.common.operator.smaputils import run_server_query

# query language
# http://www.cs.berkeley.edu/~stevedh/smap2/archiver.html#archiverquery
#
# =	compare tag values; tagname = “tagval“
# like	string matching with SQL LIKE; tagname like “pattern“
# ~	regular expression matching; tagname ~ “pattern“
# has	assert the stream has a tag; has tagname
# and	logical and of two queries
# or	logical or of two queries
# not	invert a match

class smaputilsTest(unittest.TestCase):
    def setUp(self):
        ""
        # self.c=


    def test_querySelect(self):
        # self.c.
        run_server_query('select * where')

    def test_scanSmapMonit(self):
        ""

    def test_operationAndLoad(self):
        ""

    def test_loadCSVSource(self):
        ""