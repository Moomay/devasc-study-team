import paramiko
import time

ip = "172.31.180.1"
username = "admin"
password = "cisco"

username_with_key = "root"
key = """AAAAB3NzaC1yc2EAAAADAQABAAABAQDkI86fzumvsfN4NSrZjwKxz/+Jk7GBySRlDrfrgKn
c7f/PHud6X8RLOxaOxAcMvDshNb/ihQwPKcP1OTvXeyCsiQA9e2oTIqRx6ssNT9lGp/UlHNYz
t4OYPMyFDaBjnhZu9uERx+sot7WH51x0CUVxCEWyxz7XMkPwy08nJTj9Yik
z16tyCeU3cIBqfdunH4eUAVtIWO1OcqYKjByg5ZJ+LsDPeyZchv/Ghk+KQIANBZWEeFqOGZP377VahU
lAFVT2vGYNGsQcBXAULP4OuxK3UacLxKcQFJSkgrG3VJenjAMruQ7yTjwF2w6fiHRvqBsRU+v4KTt+I5vdVEGuUZpJ"""
key2 = """ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDkI86fzumvsfN4NSrZjwKxz/+Jk7GBySRlDrfrgKnc7f/
PHud6X8RLOxaOxAcMvDshNb/ihQwPKcP1OTvXeyCsiQA9e2oTIqRx6ssNT9lGp/UlHNYzt4OYPMyFDaBjnhZu9uERx+so
t7WH51x0CUVxCEWyxz7XMkPwy08nJTj9Yikz16tyCeU3cIBqfdunH4eUAVtIWO1OcqYKjByg5ZJ+LsDPeyZchv/Ghk+KQ
IANBZWEeFqOGZP377VahUlAFVT2vGYNGsQcBXAULP4OuxK3UacLxKcQFJSkgrG3VJenjAMruQ7yTjwF2w6fiHRvqBsRU+
v4KTt+I5vdVEGuUZpJ devasc@labvm"""
#print(key)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=ip, username=username, password=password, look_for_keys=False, allow_agent=False)

with client.invoke_shell() as ssh:
    print("connected to %s ..." %ip)

    ssh.send("conf t\n")
    time.sleep(1)
    #result = ssh.recv(1000).decode('ascii')
    #print(result)
    ssh.send("ip ssh pubkey-chain\n")
    time.sleep(1)

    ssh.send("username {}\n".format(username_with_key))
    time.sleep(1)

    ssh.send("key-string\n")
    time.sleep(1)

    ssh.send(key2 + "\n")
    time.sleep(1)

    ssh.send('exit\n')
    time.sleep(1)
    ssh.send('exit\n')
    time.sleep(1)
    ssh.send('exit\n')
        
    result = ssh.recv(10000).decode('ascii')
    print(result)
