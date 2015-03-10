from enum import Enum

Event = enum(SYSTEM='server',
             STORAGE='disk',
             INSTRUMENT='instrument',
             SMAP='smap',
             SMAP_DISK='smap_disk',
             USER='user',
             SERVICE='service'
            )


def send_email(event):
  ""
  classname=event.__class__.__name__
  
  if classname == SYSTEM:
    
  elif classname == DISK:
  
  elif classname == SMAP:
  
  elif classname == INSTRUMENT:
  
  
  
