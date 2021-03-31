#!/bin/bash
echo "Start working on User!"
ha.mystate
echo "The blade must be active then the script run OK!"
#mv $1 Users.dump
sleep 30s
sed -i 's/key=//g' $1
sleep 30s
sed -i 's/value=//g' $1
sleep 30s
echo "User dump step1!"
/opt/camiant/rc/bin/rcmgr execute -clazz=msc.rcmgr.tools.ImportIqtDump -arg0=dump-file -val0=/var/camiant/Users.dump  -arg1=db-name -val1=Users -arg2=report-step -val2=1 -arg3=clear-db -quiet=on

sleep 2m
echo "User dump step2!"
/opt/camiant/rc/bin/rcmgr execute -clazz=msc.rcmgr.tools.ConvertDatabase -arg0=db-name -val0=Users -arg1=log-file -val1=/var/camiant/convert_users.log -arg2=key-convert-type -val2=string -arg3=value-convert-type -val3=deserial -arg4=tostr-method -val4=toDetailedString -quiet=on
sleep 30s

echo "Start to grep now!"
grep -ac 'Associated session count:32' convert_users.log