import os,string

cmd1='''/usr/bin/python /home/admusr/tools/CMCCSoapSim.py http://10.113.13.73:80/mediation/pcrf?wsdl subscribeService header.Username=admin header.Password=admin header.Address=10.113.76.112 header.serial=BJPCRF01B01 header.time=20180104152026  subscribedService.ServiceCode=1 subscribedService.operateTime=20181224152026 subscribedService.ServiceEndDateTime=20181224233000  -p 9.9  subscriber.usrIdentifier='''

cmd2='''/usr/bin/python /home/admusr/tools/CMCCSoapSim.py http://10.113.13.73:80/mediation/pcrf?wsdl subscribeService header.Username=admin header.Password=admin header.Address=10.113.76.112 header.serial=BJPCRF01B01 header.time=20180104152026  subscribedService.ServiceCode=3 subscribedService.operateTime=20181224152026   -p 9.9  subscriber.usrIdentifier='''

cmd3='''/usr/bin/python /home/admusr/tools/CMCCSoapSim.py http://10.113.13.73:80/mediation/pcrf?wsdl subscribeService header.Username=admin header.Password=admin header.Address=10.113.76.112 header.serial=BJPCRF01B01 header.time=20180104152026  subscribedService.ServiceCode=2 subscribedService.operateTime=20181224152026   -p 9.9  subscriber.usrIdentifier='''

cmd6='''/usr/bin/python /home/admusr/tools/CMCCSoapSim.py http://10.113.13.73:80/mediation/pcrf?wsdl subscribeUsrSessionPolicy header.Username=admin header.Password=admin header.Address=10.113.76.112 header.serial=BJPCRF01B01 header.time=20180104152026 subscribedSessionPolicy.usrSessionPolicyCode=10  subscribedSessionPolicy.operateTime=20181224152026 subscribedSessionPolicy.SessionPolicyEndDateTime=20181224233000 -p 9.9 subscriber.usrIdentifier='''
cmd7='''/usr/bin/python /home/admusr/tools/CMCCSoapSim.py http://10.113.13.73:80/mediation/pcrf?wsdl subscribeUsrSessionPolicy header.Username=admin header.Password=admin header.Address=10.113.76.112 header.serial=BJPCRF01B01 header.time=20180104152026 subscribedSessionPolicy.usrSessionPolicyCode=6  subscribedSessionPolicy.operateTime=20181224152026  -p 9.9 subscriber.usrIdentifier='''
cmd8='''/usr/bin/python /home/admusr/tools/CMCCSoapSim.py http://10.113.13.73:80/mediation/pcrf?wsdl subscribeUsrSessionPolicy header.Username=admin header.Password=admin header.Address=10.113.76.112 header.serial=BJPCRF01B01 header.time=20180104152026 subscribedSessionPolicy.usrSessionPolicyCode=7  subscribedSessionPolicy.operateTime=20181224152026  -p 9.9 subscriber.usrIdentifier='''

for i in range(8615211110000,8615211110500):
    os.system(cmd1+str(i))
    os.system(cmd2+str(i))
    os.system(cmd3+str(i))
    os.system(cmd6+str(i))
    os.system(cmd7+str(i))
    os.system(cmd8+str(i))
print "Done now!\n"
