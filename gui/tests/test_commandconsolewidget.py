import json
import os
import unittest
from weathergit.gui.commandconsolewidget import *


class Test_CommandConsole(unittest.TestCase):
    def setUp(self):
        ""

    def test_show_smap_status(self):
        res=json.loads(show_smap_status())[0]
        self.assertListEqual(res,[])

    def test_get_data(self):
        self.assertEqual(get_data().__class__,'numpy')


    def test_take_snapshot(self):
        ""
        name=take_snapshot()
        assert os.path.exists('',name)

    def test_smap_connected(self):
        res=json.loads(smap_connected())[0]
        self.assertListEqual(res,['smapbbb_connected','server_connected','smapipcam_connected'])

    def test_show_disk_size(self):
        res=json.loads(disk_size())[0]
        self.assertListEqual(res,['smapbbb_free','server_free'])

    def test_del_stream(self):
        add_stream()
        res=del_stream()
        self.assertTrue(res)

    def test_add_stream(self):
        res=add_stream()
        self.assertTrue(res)

    def test_show_streams(self):


        res=show_streams()
        self.assertListEqual(res,[''])

    def test_show_time(self):
        res=show_time()
        self.assertListEqual(res,['smapbbb','server','smapipcam'])

    def test_sync_time(self):
        res=sync_time()
        self.assertTrue(res)