import os
import commands
from target import Target

#Main 
def main():
    os.system('cls')
    targetIP, *targetPorts = input("Input ip and ports separated by a space, ex (ip port1 port2 port3): ").split(" ")
    target = Target(targetIP, targetPorts)
    run(target)

def checkArgnum(minArgs, maxArgs, args):
    if maxArgs is None:
        return minArgs <= len(args)
    return minArgs <= len(args) <= maxArgs

def run(target):
    while True:
        print("------------------------------------------")

        commandInput = input("Type a command to run: ").split(" ")
        command, args = commandInput[0], commandInput[1:]
        fn, minArgs, maxArgs = commands.getCommand[command]

        if not checkArgnum(minArgs, maxArgs, args):
            print("Unexpected number of arguments")
            continue

        fn(target, args)

#Calls main when main.py is executed
if __name__ == "__main__":
    main()
