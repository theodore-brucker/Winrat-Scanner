def __setIP(target, args):
    target.setIP(args[0])

def __addPorts(target, args):
    target.addPorts(*args)

def __ping(target, args):
    target.pingConnectivity()

def __ssh(target, args):
    if len(args) == 1:
        target.checkSSH(args[0])
    else:
        target.checkSSH()

def __quit(target, args):
    quit()

getCommand = {
    "setip": (__setIP, 1, 1),
    "addports": (__addPorts, 1, None),
    "ping": (__ping, 0, 0),
    "ssh": (__ssh, 0, 1),
    "quit": (__quit, 0, 0),
}