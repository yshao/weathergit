class ProcDriver(ExprDriver)
    def setup(self, opts):
        OperatorDriver.setup(self, opts)
        self.restrict = opts.get('Restrict')
        self.group = opts.get('Group', None)
        self.tz = opts.get('Timezone', core.Timeseries.DEFAULTS['Properties/Timezone'])

        # specialize the input operators
        self.ops = []
        for k, v in opts.iteritems():
            if not k.startswith('Expression'): continue
            self.ops.append(parse_opex(v))


start()
load_tags([path_omega_hi,path_omega_lo])
add_operators()


[server]
Port = 8082

[report 0]
ReportDeliveryLocation = http://localhost:8079/add/key/xVnqQkboDPRnj3169nL6n3coj9ziH9mXcEjY
ReportResource = /+

[/]
uuid = 60ab5366-242e-11e1-b864-378a35ddc0fd

[/r]
type = smap.drivers.expr.ExprDriver
Expression 300 = subsample(300)
Expression 3600 = subsample(3600)

Expression 'HI LO difference' = diff()
Where =
Group = uuid
ChunkSize = 48
Restrict = ((has Path and not (has Metadata/Extra/SourceStream or has Metadata/Extra/Operator)) or (Metadata/Extra/Operator like 'baseline-%'))  and has Properties/UnitofMeasure









addr=Env['smap_server_host']+':'+Env['nbook_port']
if sc.test_live(addr):
  WebCmd(addr)


class ProcDriver(ExprDriver):

  def __init___(self):
  
  
  def setup(self):
  
  
  def proc(self):
    f
    
  def start(self):


addr=dict(smap_bbb='192.168.1.146',smap_server='192.168.1.120',data_server='192.168.1.223')



def check

  #assert
  if ():
    raise e
    
  if re.findall():


class test_perf(unittest.TestCase):
  def setUp(self):
    logger.setLogLevel
    
  def test_perf(self):
    perfTest():       
    
hosts=[]    
multiping()

net = Mininet()

net.iperf(h1,h2)
net.stop

net.iperf(h1,h2)
net.iperf(h1,h3)
net.iperf(h2,h3)

.log