import sys
print(sys.path)

import re
text = 'Mi numero de telefono es 5544366971, mi codigo postal es 14410 y mi nuemero de la suerte es el 5'

result = re.findall('[0-9]+', text)
resultabc = re.findall('[A-z]+', text)

print(result)
print(resultabc)

import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)

import collections
numbers = [1,2,2,3,4,4,5,1,5,2,6,2,3,4,5,6,7]
counter = collections.Counter(numbers)
print(counter)