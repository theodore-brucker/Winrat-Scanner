import os

def main():
    os.system('cls')
    targetIP = input("Give target, retard\n")

    os.system('cls')
    targetPorts = input("Give target ports separated by ','\n").replace(" ", "").split(",")
    
    os.system('cls')
    print("Target ip: ", targetIP)
    print("Target ports: ", targetPorts)

    response = os.popen(f"ping {targetIP}").read()
    if "Received = 4" in response:
        print(f"UP {targetIP} Ping Successful")

if __name__ == "__main__":
    main()