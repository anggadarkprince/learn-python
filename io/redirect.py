print('hello')

import sys
sys.stdout.write('This output will redirected into console\n')
sys.stdout = open('text.dat', 'a')
print('hello')

textfile = open('text.dat', 'a')
print >> textfile,'hey'
print('goodbye')
exit()
