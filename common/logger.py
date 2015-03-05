__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/2/2015' '3:00 PM'

class Logger():
    def __init__(self,name):
        ""
        logger=logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(name+'.log')
        fh.setLevel(logging.DEBUG)


        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')
        self.l=logger


import logging

# logger = logging.getLogger('simple_example')
#
#
# # create console handler with a higher log level
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
# # create formatter and add it to the handlers
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
# # add the handlers to logger
# logger.addHandler(ch)
# logger.addHandler(fh)
