cutils

get_curr_data():

find_query():


def query_device_on(uuid):
  data=sutil.run_curl()
  return jprint(data)

def


def init():
    # signal, slot
    self.connect(actionUpdateMonitor,lambda: guiUpdate(self.layout1,is_device_on()))
  

  
@pyqtSlot()
def guiUpdate(layout,data):
  for item in layout.items():
    item.field.value = data[item.name.replace('out','')]