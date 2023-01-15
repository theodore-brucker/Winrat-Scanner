def __setIP(target, args):
    target.setIP(args[0])


def __addPorts(target, args):
    target.addPorts(*args)

def __help(target, args):
    print(
        "help\nquit\nsetip {ip}            - designate a new target\naddports {port range} - add another port range\nping                  - ping target ip on unspecified port\nssh {port}            - ssh to port on target ip\ntelnet {port}         - telnet to port on target ip"
    )

def __ping(target, args):
    target.pingConnectivity()

def __telnet(target, args):
    if len(args) == 1:
        target.Telnet(args[0])
    else:
        target.Telnet()

def __ssh(target, args):
    if len(args) == 1:
        target.SSH(args[0])
    else:
        target.SSH()

def __findopen(target, args):
    if len(args) == 1:
        target.findOpenPorts(args[0])
    else:
        target.findOpenPorts()


def __quit(target, args):
    quit()

getCommand = {
    "help": (__help, 0, 0),
    "setip": (__setIP, 1, 1),
    "addports": (__addPorts, 1, None),
    "ping": (__ping, 0, 0),
    "ssh": (__ssh, 0, 1),
    "quit": (__quit, 0, 0),
    "telnet": (__telnet, 1, 1),
    "findopen": (__findopen, 1, 1)
}
