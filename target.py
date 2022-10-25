import os

#Class for the Target
class Target:

    #Constructor with self and an ip
    def __init__(self, ip):
        self.ip = ip

    #Constructor with self, an ip, and ports
    def __init__(self, ip, ports):
        self.ip = ip
        self.ports = ports

    #Pings using ICMP protocol, does not use a port
    def ping(self):
        response = os.popen(f"ping {self.ip}").read()
        print(response)
        if "Received = 4" in response:
            print(f"Ping to {self.ip} successful")

    #Run self
    def run(self):
        while True:
            print("------------------------------------------")
            command = input("Type a command to run: ").lower()
            if command == "ping":
                self.ping()
            elif command == "quit":
                quit()
