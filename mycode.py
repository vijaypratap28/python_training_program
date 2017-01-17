import re
import MySQLdb
conn = MySQLdb.connect(host= "localhost",user="root",passwd="asm123",db="accesspoint_database")

file = open('/home/asm/vijay/diag3.out','r').read()

cursor = conn.cursor()
#mac
pma = re.compile(r'(?:[0-9a-fA-F]:?){12}')
foundma = re.findall(pma,file)
print "...*********************************.All mac address....."
for mac in foundma:
	
	
	print mac



#ipv4

pip = re.compile(r'(?:[\d][1-9]{2,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})')
foundip = re.findall(pip,file)
print "...************************************.All ipv4 address....."
for ip in foundip:
	print ip


#ipv6

pip6 = re.compile(r'[a-fA-FA-F\d]{4}:\d{1}')
foundip6 = re.findall(pip6,file)
print "..*******************************...All ipv6 address...."
for ipv6 in foundip6:
	print ipv6

#name

pname = re.compile(r'\s*Name\s*:\s*(.*)')
foundname = re.findall(pname,file)
print "..*********************************.All name......"
for name in foundname:
	print name


#psk

ppsk = re.compile(r'\s*PSK\s*:\s*(.*)')
foundpsk = re.findall(ppsk,file)
print "....All psk....."
for psk in foundpsk:
	print psk


#state

pstate = re.compile(r'\s*State\s*:\s*(.*)')
foundstate = re.findall(pstate,file)
print "..*******************************..All state....."
for state in foundstate:
	print state


#mesh_role

pmesh_role = re.compile(r'\s*Mesh Role\s*:\s*(.*)')
foundmesh_role = re.findall(pmesh_role,file)
print "...**********************************.ll mesh role....."
for mesh_role in foundmesh_role:
	print mesh_role

#timer

ptimer = re.compile(r'\s*Timer\s*:\s*(.*)')
foundtimer = re.findall(ptimer,file)
print "....************************************All timer....."
for timer in foundtimer:
	print timer

#tunnel

ptunnel = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)/')
foundtunnel = re.findall(ptunnel,file)
print "...**********************************.All timer....."
for tunnel in foundtunnel:
	

	print tunnel

#sec mode

psec = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)')
foundsec = re.findall(psec,file)

print "...*******************************.All sec mode....."

for sec in foundsec:
	ssec = sec.split("/")
	print ssec[1]




#HW

pHW = re.compile(r'\s*HW/SW Version\s*:\s*(.*)/')
foundHW = re.findall(pHW,file)
print "...***************************************.All HW....."
for HW in foundHW:
	print HW

#SW

pSW = re.compile(r'\s*HW/SW Version\s*:\s*(.*)')
foundSW = re.findall(pSW,file)
print "....*****************************************.All SW...."
for SW in foundSW:
	sSW = SW.split("/")
	print sSW[1]



#Model

pModel = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)/')
foundModel = re.findall(pModel,file)
print "....**************************************.All model...."
for Model in foundModel:
	print Model

#Serial

pSerial = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)')
foundSerial = re.findall(pSerial,file)
print "....**************************************All serial....."
for Serial in foundSerial:
	sSerial = Serial.split("/")
	print sSerial[1]


if len(foundip) == len(foundname) == len(foundpsk) == len(foundstate) == len(foundmesh_role) == len(foundtimer) == len(foundtunnel) == len(foundsec) == len(foundSW) == len(foundHW) == len(foundModel) == len(foundSerial):
	

	for i in range(len(foundip)):
		
			
		cursor.execute("""insert into information (IPv4Address,Name,State,Tunnel,Sec_Mode,Mesh_Role,PSK,Timer,HW_Version,SW_Version,Model,Serial_number)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');""" %(foundip[i],foundname[i],foundpsk[i],foundstate[i],foundmesh_role[i],foundtimer[i],foundtunnel[i],foundsec[i],foundSW[i],foundHW[i],foundModel[i],foundSerial[i]))





#file.close()














