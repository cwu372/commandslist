import os,string
cmd1='''/usr/bin/python /home/admusr/tools/CMCCSoapSim.py http://10.113.13.73:80/mediation/pcrf?wsdl addSubscriber header.Username=admin header.Password=admin header.Address=10.113.76.112    header.serial=BJPCRF01B01 header.time=20180104152026 subscriber.usrBillCycleDate=1 subscriber.operateTime=20190115000000 -p 9.9 subscriber.usrIdentifier='''
cmd2='''/usr/bin/python /home/admusr/tools/spr_opt.py add_entity 10.113.76.112 8787 Comer=Comer usrStatus=2 usrNextResetTime=20190101000000 MSISDN='''
for i in range(8615212340001,8615212540001):
    os.system(cmd1+str(i))
    os.system(cmd2+str(i))
print "Done now!\n"
