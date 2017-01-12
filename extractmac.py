import re
p = re.compile(ur'(?:[0-9a-fA-F]:?){12}')

file = open('/home/asm/vijay/diag.out','rb').read()

rawdata = re.findall(p, file)

for macaddress in rawdata:
    print  macaddress 



