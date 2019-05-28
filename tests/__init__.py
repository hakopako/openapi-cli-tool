import sys
from os.path import dirname, abspath, join, sep
src = dirname(dirname(abspath(__file__)))
assert src.split(sep)[-1].lower() == 'src'
sys.path.append(src)
print('src folder appended to path: ', src)
