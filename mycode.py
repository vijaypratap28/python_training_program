import re
#import mysqldb

file = open('/home/asm/vijay/diag.out','r').read()


#mac
pma = re.compile(r'(?:[0-9a-fA-F]:?){12}')
foundma = re.findall(pma,file)
print "........."
for mac in foundma:
	print mac



#ipv4

pip = re.compile(r'(?:[\d][1-9]{2,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})')
foundip = re.findall(pip,file)
print "........."
for ip in foundip:
	print ip


#ipv6

#pip = re.compile(r'(?:[\d][1-9]{2,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})')
#foundip = re.findall(pip,file)
#print "........."
#for ip in foundip:
	#print ip

#name

pname = re.compile(r'\s*Name\s*:\s*(.*)')
foundname = re.findall(pname,file)
print "........."
for name in foundname:
	print name


#psk

ppsk = re.compile(r'\s*PSK\s*:\s*(.*)')
foundpsk = re.findall(ppsk,file)
print "........."
for psk in foundpsk:
	print psk


#state

pstate = re.compile(r'\s*State\s*:\s*(.*)')
foundstate = re.findall(pstate,file)
print "........."
for state in foundstate:
	print state


#mesh_role

pmesh_role = re.compile(r'\s*Mesh Role\s*:\s*(.*)')
foundmesh_role = re.findall(pmesh_role,file)
print "........."
for mesh_role in foundmesh_role:
	print mesh_role

#timer

ptimer = re.compile(r'\s*Timer\s*:\s*(.*)')
foundtimer = re.findall(ptimer,file)
print "........."
for timer in foundtimer:
	print timer

#tunnel

ptunnel = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)/')
foundtunnel = re.findall(ptunnel,file)
print "........."
for tunnel in foundtunnel:
	print tunnel

#sec mode

psec = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)')
foundsec = re.findall(psec,file)

print "........."

for sec in foundsec:
	ssec = sec.split("/")
	print ssec[1]



#HW

pHW = re.compile(r'\s*HW/SW Version\s*:\s*(.*)/')
foundHW = re.findall(pHW,file)
print "........."
for HW in foundHW:
	print HW

#SW

pSW = re.compile(r'\s*HW/SW Version\s*:\s*(.*)')
foundSW = re.findall(pSW,file)
print "........."
for SW in foundSW:
	sSW = SW.split("/")
	print sSW[1]


#Model

pModel = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)/')
foundModel = re.findall(pModel,file)
print "........."
for Model in foundModel:
	print Model

#Serial

pSerial = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)')
foundSerial = re.findall(pSerial,file)
print "........."
for Serial in foundSerial:
	sSerial = Serial.split("/")
	print sSerial[1]














