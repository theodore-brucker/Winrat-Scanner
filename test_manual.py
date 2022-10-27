import interface.cli as cli
import scanner.target as target


def main():
    t = target.Target("1.1.1.1")
    cli.run(t)


if __name__ == "__main__":
    main()
