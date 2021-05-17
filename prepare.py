import os,sys
os.system('systemctl disable NetworkManager')
os.system('stop NetworkManager')
os.system('disable firewalld')
os.system('stop firewalld')
os.system('swapoff -a')
os.system('''echo "10.113.2.250    docker-registry.openstack.cn.oracle.com">>/etc/hosts''')
os.system('''echo "10.113.69.82    registry-domain-nj.oracle.com">>/etc/hosts''')
os.system('echo>/etc/resolv.conf')
os.system('''echo "search openstacklocal">>/etc/resolv.conf''')
os.system('''echo "nameserver 10.182.244.34">>/etc/resolv.conf''')
os.system('''echo "nameserver 146.56.237.50">>/etc/resolv.conf''')
os.system('''echo "nameserver 192.135.82.76">>/etc/resolv.conf''')
os.system('''echo "search localdomain">>/etc/resolv.conf''')
os.system('''echo "nameserver 10.233.0.3">>/etc/resolv.conf''')
os.system('''echo "DNS1=10.182.244.34">>/etc/sysconfig/network-scripts/ifcfg-eno1.523''')
os.system('''sed -i 's/0.ol.pool.ntp.org/144.20.102.252/g' /etc/chrony.conf ''')
os.system('systemctl restart chronyd.service)
os.system('chronyc sources -v')
os.system('ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime')
os.system('date')
os.system('cat /etc/resolv.conf')
os.system('cat /etc/hosts')
os.system('cat /etc/sysconfig/network-scripts/ifcfg-eno1.523')
os.system('echo done!')




