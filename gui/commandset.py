import inspect


class CommandSet(object):
    def __init__(self):
        ""

        a=[]
        lis=inspect.getmembers(self, inspect.ismethod)
        for item in lis:
            a.append(item[0])

        self.cmdset=a
        # smap=SmapUtils()
        # fab=FabUtils()
        print a


    def run(self,b):
        print b

    def add(self,a,b):
        print a+b


    def get_data(self):
        ""


    def add_stream(self,csvfilep):
        ""
        # smap.load_csv(csvfilep)

    def del_stream(self):
        ""

    def show_streams(self):
        ""