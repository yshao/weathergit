__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/26/2015' '1:18 PM'

import PyV8
ctxt = PyV8.JSContext()          # create a context with an implicit global ob
ctxt.enter()                     # enter the context (also support with statem
ctxt.eval("1+2")                 # evalute the javascript expression
                                 # return a native python int
class Global(PyV8.JSClass):      # define a compatible javascript class
  def hello(self):               # define a method
    print "Hello World"

ctxt2 = PyV8.JSContext(Global()) # create another context with the global obje
ctxt2.enter()
ctxt2.eval("hello()")            # call the global object from javascript
