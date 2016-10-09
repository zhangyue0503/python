__version__ = '0.1'
__all__ = [
    'executeMmDb'
]

__author__ = 'zhangyue'


from .mmdb import *

def executeMmDb(sql):
    return mmdb().execute(sql)


