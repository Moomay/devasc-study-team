import paramiko
import getpass
import time
 
username = 'admin'
password = 'cisco'
secret = 'secret'
username_with_key = 'root'
 
devices_ip = ["172.31.180."+i for i in range(1,10)]

public_key = """AAAAB3NzaC1yc2EAAAABJQAAAQEA4IfG8a+ISIA01SOpJ7+QpmolBgOw6QF
/ak9NRasVuJ9XDXp7ICSZxMtuRIyaeiarh2HXP/pp4pWWrB6d8As1J3wW
bO6aZQ0dugOESA2C8tMAn8SJT15wmmZ2ItIuwT25miq/+NO7AsvfrxUx6
o9BDz8dNac3lEW6GGUn920xneFL/2XW8KvLt96uHFHyO77xhnK/8UG6Lg
2iFT2UIoWKvuLl49wXmearIPooj5uEnd5VZ2fNyHIUlgEwTFtN1a1tk8N
QONFImnNzfExFkaQ8O/2SJ6Z0TAoTBWrPrLi0ArVYNeIxEG9c+zcuk9mz
c0fT/LWT8YWABYxQReSo1sV1NQ=="""


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=ip, username=username, password=password, look_for_keys=False, allow_agent=False)

with client.invoke_shell() as ssh:
    ssh.send("conf t\n")
    time.sleep(1)
    ssh.send("router ospf 0")
    time.sleep(1)
    ssh.send("network 172.31.180.{} 0.0.0.15 area 0".format(16))
    time.sleep(1)
    #loopback
    ssh.send("network 172.20.20.{} 0.0.0.0 area 0")
    time.sleep(1)
    