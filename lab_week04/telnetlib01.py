import telnetlib
import time
from multiprocessing.dummy import Pool as ThreadPool

host_list = ['172.31.180.'+str(i) for i in range(1,10)]
lo0Ip_list = ['172.20.180.'+str(i) for i in range(1,10)]
def worker(index):
    create_lo(host_ip[index], lo0_ip[index])

def create_lo(host_ip, lo0_ip):

    username = 'admin'
    password = 'cisco'

    tn = telnetlib.Telnet(host_ip, 23, 10)
    tn.read_until(b"Username:")
    tn.write(username.encode('ascii')+ b"\n")
    time.sleep(1)
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii')+ b"\n")
    time.sleep(1)

    tn.write(b"conf t\n")
    time.sleep(2)
    tn.read_until(b"#")
    tn.write(b"int lo 0\n")
    time.sleep(5)
    tn.read_until(b"#")

    lo0_ip = " "+lo0_ip
    tn.write(b"ip add " + lo0_ip.encode('ascii') + b" 255.255.255.255\n")
    tn.read_until(b"#")

    time.sleep(5)
    tn.read_until(b"#")
    tn.write(b"do sh ip int br\n")
    time.sleep(5)
    print(tn.read_until(b"#").decode('ascii'))
    tn.write(b"end")

    tn.close()
def run_multi():
    num_thread = 2
    threads = ThreadPool(num_thread)
    result = threads.map(worker, range(len(host_ip)))

    threads.close()
    threads.join()
#for i in range(len(host_list)):
#    create_lo(host_list[i], lo0Ip_list[i])
create_lo(host_list[0], lo0Ip_list[0])
#print(host_list)