import os
from target import Target


def main():
    os.system('cls')
    targetIP = input("IP: ")
    targetPorts = input("Ports separated by ',': ").replace(" ", "").split(",")
    target = Target(targetIP, targetPorts)
    print()
    target.run()


if __name__ == "__main__":
    main()
