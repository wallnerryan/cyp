#May need to change to just " .base " if import error
#from settings.base import *
from .base import *

try:
  #May need to change to just " .local " if import error
  from settings.local import *
  from .local import *
except ImportError as e:
  print e
  pass