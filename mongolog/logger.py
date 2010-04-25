
import logging
import sys
import os

from socket import gethostname
from datetime import datetime

def _level_to_str(level):
    """ Convert a numeric logging level to string representation  """
    if logging.DEBUG == level:
        return u'debug'
    elif logging.INFO == level:
        return u'info'
    elif logging.WARNING == level:
        return u'warning'
    elif logging.ERROR == level:
        return u'error'
    elif logging.CRITICAL  == level:
        return u'critical'
    else:
        return u'undefined'

def _current_user():
    """ Get the name of the os user running this app """
    import pwd, os
    try:
        return pwd.getpwuid(os.getuid()).pw_name
    except KeyError:
        return "(unknown)"

def _calling_func_name():
    return _calling_frame().f_code.co_name

def _calling_frame():
    f = sys._getframe()

    while True:
        if _is_user_source_file(f.f_code.co_filename):
            return f
        f= f.f_back

def _is_user_source_file(filename):
    return os.path.normcase(filename) not in (_srcfile, logging._srcfile)

def _current_source_file():
    if __file__[-4:].lower() in ['.pyc', '.pyo']:
        return __file__[:-4] + '.py'
    else:
        return __file__
 
_srcfile = os.path.normcase(_current_source_file())

