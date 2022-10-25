import os
from target import Target


def main():
    os.system('cls')
    targetIP = "1.1.1.1"
    targetPorts = []
    target = Target(targetIP, targetPorts)
    target.run()


if __name__ == "__main__":
    main()
