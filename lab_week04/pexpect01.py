import pexpect
""" 
Create loopback 0 
    ip is router ip
    num is io loobback 172.20.180.num
"""
def create_lo(ip, num):
    prompt = '#'
    username = 'admin'
    password = 'cisco'

    child = pexpect.spawn('telnet ' + ip, timeout=60)
    child.expect('Username')
    child.sendline(username)
    child.expect('Password')
    child.sendline(password)
    child.expect(prompt)
    child.sendline('conf t')
    child.expect(prompt)
    child.sendline('int lo 0')
    child.expect(prompt)
    child.sendline('ip add 172.20.180.'+str(num)+ ' 255.255.255.255')
    child.expect(prompt)
    child.sendline('end')
    child.expect(prompt)
    child.sendline('sh ip int br')
    child.expect(prompt)
    result = child.before
    child.close()
    print(result)
listIp = ['172.31.180.4', '172.31.180.5']
for i in range(len(listIp)):
    create_lo(listIp[i], 4+i)


"""
from multiprocessing.dummy import Pool as ThreadPool
num_thread = 2
threads = ThreadPool(num_thread)
def f(a):
    return a+2
result = threads.map(f, range(3))

threads.close()
threads.join()
"""