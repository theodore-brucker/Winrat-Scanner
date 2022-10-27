import os
import paramiko
from telnetlib import Telnet

class Target:
    def __init__(self, ip, ports=[]):
        self.setIP(ip)
        self.ports = ports

    def setIP(self, ip):
        self.ip = ip

    def addPorts(self, *ports):
        self.ports.extends(ports)

    def pingConnectivity(self):
        response = os.popen(f"ping {self.ip}").read()
        print(response)
        if "Received = 4" in response:
            print(f"Ping to {self.ip} successful")

    def SSH(self, port=22):
        ssh_client = paramiko.SSHClient()
        try:
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect('10.3.32.32', port=port,
                               username='amumu', password='amumu')
        except paramiko.SSHException:
            print("Login attempt failed")
            return
        stdin, stdout, stderr = ssh_client.exec_command('ls')
        output = stdout.readlines()
        for item in output:
            print(item)

    def Telnet(self, ports):
        
        for port in ports:
            tn = Telnet(self.ip, port)
            tn.write(b'guido\r\n')
            print(tn.read_all())
        return self

    def RDP(self, ports):
        return self

    def POP3(self, ports):
        return self
        
