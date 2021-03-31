#!/bin/bash
echo "Start working on Session!"
ha.mystate
echo "The blade must be active then the script run OK!" 
sed -i 's/key=//g' $1
sleep 30s
sed -i 's/value=//g' $1
sleep 30s
echo "Session dump step1!"
/opt/camiant/rc/bin/rcmgr execute -clazz=msc.rcmgr.tools.ImportIqtDump -arg0=dump-file -val0=/var/camiant/$1 -arg1=db-name -val1=DiameterSession -arg2=report-step -val2=1 -arg3=clear-db -quiet=on
echo "Session dump step2!"
sleep 2m
/opt/camiant/rc/bin/rcmgr execute -clazz=msc.rcmgr.tools.ConvertDatabase -arg0=db-name -val0=DiameterSession -arg1=log-file -val1=/var/camiant/convert_session.log -arg2=key-convert-type -val2=string -arg3=value-convert-type -val3=deserial -arg4=tostr-method -val4=toStringDetails -quiet=on
echo "Done!"

