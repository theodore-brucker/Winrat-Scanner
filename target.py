import os
import paramiko
from setuptools import Command

#Class for the Target
class Target:

    #Constructor with self and an ip
    def __init__(self, ip, ports=[]):
        self.setIP(ip)
        self.ports = ports

    def setIP(self, ip):
        self.ip = ip

    def addPorts(self, *ports):
        self.ports.extends(ports)

    #Pings using ICMP protocol, does not use a port
    def pingConnectivity(self):
        response = os.popen(f"ping {self.ip}").read()
        print(response)
        if "Received = 4" in response:
            print(f"Ping to {self.ip} successful")

    #SSH login to port 22
    def checkSSH(self, port=22):
        # self.ports = input("Port ranges (separated by ,): ") 
        ssh_client = paramiko.SSHClient()
        try:
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect('10.3.32.32', port=22, username='amumu', password='amumu')
        except paramiko.SSHException:
            print("Login attempt failed")
            return
        stdin,stdout,stderr=ssh_client.exec_command('ls')
        output = stdout.readlines()
        for item in output:
            print(item)

