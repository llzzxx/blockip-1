import os
import re
num='\\b([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\b'
file1=open("ip.txt")
while  1:
    line = file1.readline()
    if not line:
        break
    url=line.split()[-1]
    result = os.popen("ping -c 1 " + url)
    pattern = re.compile(r'\d+.\d+.\d+.\d+')
    str=result.read() 
    s = 'sadf12.2.1.2fds1.1.1.1;asdf'      
    tempip=re.findall(r'\d+.\d+.\d+.\d+',str)[0]
    print tempip
    cmd = 'iptables -I INPUT -s '+ tempip + ' -j DROP'
    os.system(cmd)
