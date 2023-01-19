import os

def main():
    commands = {}
    for module in os.listdir('modules'):
        exec(f"""commands["{module}"] = __import__("modules.{module}.run").{module}.run.run""")
    commands.get(input("gib input: "))()

if __name__ == '__main__':
    main()