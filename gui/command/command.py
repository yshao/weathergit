import abc
import os

class Command(object):
    # handler=None
    __metaclass__ = abc.ABCMeta
    logger=None

    def __init__(self):
        """"""

    # @abc.abstractmethod
    # def parse(self):
        """"""

    @abc.abstractmethod
    def execute(self):
        """"""

    def undo(self):
        """"""
