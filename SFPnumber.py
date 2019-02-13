
import pprint
import pyeapi

switches =[]
i=101
while i<137:
    fourh_octet=i
    IP= "x.x.x."+str(fourh_octet)
    i = i+1
    switches.append(IP)

genel=0


for i in switches:
    node = pyeapi.connect(transport="https", host=i, username="xxx", password="xxx", port=None)
    showinterface= node.execute(["show interfaces  status"])
    print i
    switchsum = 0
    for intf in showinterface['result'][0]['interfaceStatuses']:
        print showinterface['result'][0]['interfaceStatuses'][intf]['interfaceType']
        if showinterface['result'][0]['interfaceStatuses'][intf]['interfaceType']=='10GBASE-SR':
            switchsum=switchsum+1
    genel=genel+switchsum

    print i,switchsum
print genel








