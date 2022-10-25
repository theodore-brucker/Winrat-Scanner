import os


class Target:
    def __init__(self, ip, ports):
        self.ip = ip
        self.ports = ports

    def ping(self):
        response = os.popen(f"ping {self.ip}").read()
        print(response)
        if "Received = 4" in response:
            print(f"Ping to {self.ip} successful")

    def run(self):
        while True:
            print("------------------------------------------")
            command = input("Type a command to run: ").lower()
            if command == "ping":
                self.ping()
            elif command == "quit":
                quit()
