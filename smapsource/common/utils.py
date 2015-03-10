class DaqException(Exception):
    """Generic error"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code

class DeviceException(Exception):
    """"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code


class WXT520Exception(DeviceException):
    """"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code 
        
class GPS18xLVCException(DeviceException):
    """"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code        
        
        
class MLxException(DeviceException):
    """"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code
        
class PRACOException(DeviceException):
    """"""
    def __init__(self, message, http_code=None):
        Exception.__init__(self, message)
        self.http_code = http_code
        
