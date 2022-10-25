import os
from target import Target

#Main 
def main():
    os.system('cls')
    targetIP, *targetPorts = input("Input ip and ports separated by a space, ex (ip port1 port2 port3): ").split(" ")
    target = Target(targetIP, targetPorts)
    run(target)

commandArgNums = {
    "setip": (1, 1),
    "addports": (1, None),
    "ping": (0, 0),
    "ssh": (0, 1),
    "quit": (0, 0),
}

def checkArgnum(command, args):
    minArgs, maxArgs = commandArgNums[command]
    if maxArgs is None:
        return minArgs <= len(args)
    return minArgs <= len(args) <= maxArgs

def run(target):
    while True:
        print("------------------------------------------")

        hello = input("Type a command to run: ").split(" ")
        command, args = hello[0], hello[1:]
        
        if not checkArgnum(command, args):
            print("Unexpected number of arguments")
            continue

        if command == "setip":
            target.setIP(args[0])
        if command == "addports":
            target.addPorts(*args)
        if command == "ping":
            target.pingConnectivity()
        elif command == "ssh":
            if len(args) == 1:
                target.checkSSH(args[0])
            else:
                target.checkSSH()
        elif command == "quit":
            quit()

#Calls main when main.py is executed
if __name__ == "__main__":
    main()
