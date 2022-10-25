import os
from target import Target

#Main 
def main():
    os.system('cls')
    targetIP = input("IP: ")
    targetPorts = input("Ports separated by ',': ").replace(" ", "").split(",")
    target = Target(targetIP, targetPorts)
    print()
    target.run()

#Calls main when main.py is executed
if __name__ == "__main__":
    main()
