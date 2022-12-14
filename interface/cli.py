import os
import scanner.target as target
import interface.commands as commands


def checkArgnum(minArgs, maxArgs, args):
    if maxArgs is None:
        return minArgs <= len(args)
    return minArgs <= len(args) <= maxArgs


def createTarget():
    os.system("cls")
    print(
        "#####################################\n###########-WINRAT--SCANNER-#########\n#####################################\n")
    targetIP, *targetPorts = input(
        "Input ip and ports separated by a space, ex (ip port1 port2 port3): ").split(" ")
    return target.Target(targetIP, targetPorts)


def run(t):
    while True:
        print("------------------------------------------")

        command, *args = input("Type a command to run: ").split(" ")
        fn, minArgs, maxArgs = commands.getCommand.get(
            command, (None, None, None))

        if fn is None:
            print("Unexpected command")
            continue

        if not checkArgnum(minArgs, maxArgs, args):
            print("Unexpected number of arguments")
            continue

        fn(t, args)
