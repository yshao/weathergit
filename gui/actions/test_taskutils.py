from taskutils import *
import unittest

class ConnectionTest(unittest.TestCase):
    def test_connection(self):
        assert testConnection("www.google") == True

    def test_connection_fail(self):
        assert testConnection("aaa") == False

    def test_postgreConnection(self):
        login={}
        login['host'] = '192.168.1.120'
        login['dbname'] = 'archiver'
        login['user'] = 'archiver'
        login['password'] = 'password'
        login['port'] = 5432
        assert testPostgreConnection(login) == True

    def test_postgreConnection_fail(self):
        login={}
        login['host'] = '192.168.1.121'
        login['dbname'] = 'archiver'
        login['user'] = 'archiver'
        login['password'] = 'password'
        login['port'] = 5432
        assert testPostgreConnection(login) == False