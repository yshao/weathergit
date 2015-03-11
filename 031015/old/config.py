import json
from pprint import pprint


class Config(object):
    def __init__(self,path):
        self.fhandle=open(path)
        self.data = json.load(self.fhandle)

    def save(self):
        js=json.write(self.data)
        self.fhandle(js)

    def close(self):
        self.fhandle.close()

    def __str__(self):
        return str(self.data)

    def __getitem__(self, item):
        return self.data[item]


