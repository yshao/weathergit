import unittest

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/21/2015' '1:39 PM'

import ConfigParser
import io

sample_config = """
[mysqld]
user = mysql
pid-file = /var/run/mysqld/mysqld.pid
skip-external-locking = 1
old_passwords = 1
skip-bdb = 1
skip-innodb
"""
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

class test(unittest.TestCase):

    def test_config(self):
        # Settings with values are treated as before:
        test.assertEqual(config.get("mysqld", "user"),'mysql')


        # Settings without values provide None:
        test.assertEqual(config.get("mysqld", "skip-bdb"),'1')

        # Settings which aren't specified still raise an error:
        test.assertFail(config.get("mysqld", "does-not-exist"))

    def test_save_config(self):
        ""